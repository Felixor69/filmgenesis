#!/usr/bin/env python3
"""
Jednorazowe sprawdzenie iPhone'a 18 Pro Max 512 GB (wszystkie kolory)
w salonie iDream Rumia. Uruchamiane co ~10 min przez GitHub Actions
(.github/workflows/idream-monitor.yml).

Wysyła maila przez Gmaila, gdy:
  - któryś kolor pojawi się do odbioru w salonie w Rumii,
  - zmieni się termin wysyłki na stronie produktu.

Stan z poprzedniego sprawdzenia trzymany jest w pliku STATE_FILE,
żeby ta sama zmiana nie przychodziła mailem co 10 minut.

Zmienne środowiskowe (sekrety w GitHubie):
  GMAIL_USER          adres Gmaila, z którego idzie mail
  GMAIL_APP_PASSWORD  hasło do aplikacji Google (nie zwykłe hasło)
  MAIL_TO             adres odbiorcy (domyślnie GMAIL_USER)
  TEST_EMAIL          "true" = wyślij testowego maila
"""

import html
import json
import os
import re
import smtplib
import sys
import urllib.request
from email.message import EmailMessage

PRODUCTS = [
    "iphone-18-pro-max-512gb-czarny-mjxt4hx-a",
    "iphone-18-pro-max-512gb-srebrny-mjxu4hx-a",
    "iphone-18-pro-max-512gb-blekit-lodowca-mjxw4hx-a",
    "iphone-18-pro-max-512gb-burgund-mjxv4hx-a",
]
STORE_CITY = "Rumia"
SITE = "https://idream.pl"
STATE_FILE = os.environ.get("STATE_FILE", "state.json")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0 Safari/537.36")

QUERY = """
query($h: String!) @inContext(language: PL) {
  product(handle: $h) {
    title
    variants(first: 1) {
      edges { node {
        storeAvailability(first: 100) {
          edges { node {
            available
            quantityAvailable
            pickUpTime
            location { address { city } }
          } }
        }
      } }
    }
  }
}
"""


def http(url, data=None, headers=None):
    h = {"User-Agent": UA}
    h.update(headers or {})
    req = urllib.request.Request(url, data=data, headers=h)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def check(handle):
    """Zwraca stan jednego modelu: tytuł, czy jest w salonie, opis, termin wysyłki."""
    raw = http(f"{SITE}/products/{handle}")
    token = re.search(r'data-storefront-api-access-token="([^"]+)"', raw)
    shop = re.search(r'Shopify\.shop\s*=\s*"([^"]+)"', raw)
    if not token or not shop:
        raise RuntimeError("nie znalazłem danych API na stronie (zmienili stronę?)")

    text = re.sub(r"<script.*?</script>|<style.*?</style>", "", raw, flags=re.S)
    text = html.unescape(re.sub(r"<[^>]+>", "\n", text))
    shipping = re.search(r"Wysyłka[^\n]{0,100}", text)
    shipping = shipping.group(0).strip() if shipping else "(brak informacji)"

    body = json.dumps({"query": QUERY, "variables": {"h": handle}}).encode()
    resp = json.loads(http(
        f"https://{shop.group(1)}/api/2024-07/graphql.json",
        data=body,
        headers={"Content-Type": "application/json",
                 "X-Shopify-Storefront-Access-Token": token.group(1)},
    ))
    if resp.get("errors"):
        raise RuntimeError(resp["errors"][0].get("message"))
    product = resp["data"]["product"]

    store = None
    for edge in product["variants"]["edges"][0]["node"]["storeAvailability"]["edges"]:
        if (edge["node"]["location"]["address"] or {}).get("city") == STORE_CITY:
            store = edge["node"]

    if store is None:
        in_store = False
        salon = f"{STORE_CITY}: brak odbioru w salonie"
    else:
        qty = store["quantityAvailable"] or 0
        in_store = bool(store["available"]) and qty > 0
        salon = (f"{STORE_CITY}: {'DOSTĘPNY' if in_store else 'niedostępny'}"
                 f" (sztuk: {qty}, odbiór: {store['pickUpTime'] or '-'})")

    return {"title": product["title"], "in_store": in_store,
            "salon": salon, "shipping": shipping}


def send_mail(subject, body):
    user = os.environ.get("GMAIL_USER")
    password = os.environ.get("GMAIL_APP_PASSWORD")
    to = os.environ.get("MAIL_TO") or user
    if not user or not password:
        raise RuntimeError("brak sekretów GMAIL_USER / GMAIL_APP_PASSWORD")
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = user
    msg["To"] = to
    msg.set_content(body)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30) as smtp:
        smtp.login(user, password.replace(" ", ""))
        smtp.send_message(msg)
    print(f"Wysłano maila do {to}: {subject}")


def main():
    try:
        with open(STATE_FILE, encoding="utf-8") as f:
            last = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        last = {}

    new_state, alerts, lines = {}, [], []
    for handle in PRODUCTS:
        url = f"{SITE}/products/{handle}"
        prev = last.get(handle)
        try:
            cur = check(handle)
        except Exception as e:
            print(f"Błąd przy {handle}: {e}")
            if prev:
                new_state[handle] = prev
            continue

        new_state[handle] = cur
        line = f"{cur['title']} | {cur['salon']} | {cur['shipping']}"
        lines.append(f"- {line}\n  {url}")
        print(line)

        if cur["in_store"] and not (prev or {}).get("in_store"):
            alerts.append(f"JEST W SALONIE W RUMII: {cur['title']}\n"
                          f"{cur['salon']}\n{url}")
        if prev and prev["shipping"] != cur["shipping"]:
            alerts.append(f"Zmiana terminu wysyłki: {cur['title']}\n"
                          f"Było: {prev['shipping']}\nJest: {cur['shipping']}\n{url}")

    if os.environ.get("TEST_EMAIL") == "true":
        alerts.append("To jest testowy mail – monitor iDream Rumia działa.")

    if alerts:
        in_store = any(s["in_store"] for s in new_state.values())
        subject = ("iPhone 18 Pro Max 512 GB JEST w iDream Rumia!" if in_store
                   else "iDream Rumia – zmiana przy iPhone 18 Pro Max 512 GB")
        body = ("\n\n".join(alerts)
                + "\n\nAktualny stan wszystkich kolorów:\n" + "\n".join(lines))
        try:
            send_mail(subject, body)
        except Exception as e:
            # Nie zapisujemy nowego stanu, żeby alert poszedł przy następnym razie.
            print(f"Nie udało się wysłać maila: {e}")
            sys.exit(1)

    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(new_state, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
