#!/usr/bin/env bash
# Instaluje monitor iDream Rumia na serwerze (Linux) i uruchamia go co 5 minut z crona.
# Użycie na serwerze:
#   bash <(curl -fsSL https://raw.githubusercontent.com/Felixor69/filmgenesis/claude/brave-einstein-lqmbpf/idream-monitor/install.sh)
set -euo pipefail

DIR="$HOME/idream"
RAW="https://raw.githubusercontent.com/Felixor69/filmgenesis/claude/brave-einstein-lqmbpf/idream-monitor/check.py"

command -v python3 >/dev/null || { echo "Instaluję python3..."; apt-get update -qq && apt-get install -y -qq python3; }
command -v crontab >/dev/null || { echo "Instaluję crona..."; apt-get update -qq && apt-get install -y -qq cron; systemctl enable --now cron; }

mkdir -p "$DIR"
curl -fsSL "$RAW" -o "$DIR/check.py"

if [ ! -f "$DIR/env" ]; then
  read -rp "Adres Gmaila, z którego idą maile [felixor69@gmail.com]: " user </dev/tty
  user="${user:-felixor69@gmail.com}"
  read -rsp "Hasło do aplikacji Google (16 znaków, nie będzie widoczne): " pass </dev/tty; echo
  cat > "$DIR/env" <<EOF
export GMAIL_USER='$user'
export GMAIL_APP_PASSWORD='$pass'
export MAIL_TO='felixor69@gmail.com'
export STATE_FILE='$DIR/state.json'
EOF
  chmod 600 "$DIR/env"
fi

echo "Test: sprawdzam iDream i wysyłam maila próbnego..."
( . "$DIR/env" && TEST_EMAIL=true python3 "$DIR/check.py" )

LINE="*/5 * * * * . $DIR/env && python3 $DIR/check.py >> $DIR/log.txt 2>&1"
( crontab -l 2>/dev/null | grep -v 'idream/check.py' || true; echo "$LINE" ) | crontab -
echo
echo "Gotowe. Monitor działa co 5 minut. Log: $DIR/log.txt"
echo "Wyłączenie: crontab -l | grep -v idream/check.py | crontab -"
