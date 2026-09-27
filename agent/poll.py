import os, requests
from pathlib import Path
from orchestrator import handle_message

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
OWNER = int(os.environ["OWNER_CHAT_ID"])
STATE = Path("state.txt")

offset = int(STATE.read_text().strip()) if STATE.exists() else 0
updates = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates",
                        params={"offset": offset + 1}).json().get("result", [])

for u in updates:
    offset = u["update_id"]
    msg = u.get("message", {})
    if msg.get("chat", {}).get("id") == OWNER and "text" in msg:
        reply = handle_message(msg["text"])
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                       json={"chat_id": OWNER, "text": reply})

STATE.write_text(str(offset))
