import os, requests
from agents import planner

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
OWNER = int(os.environ["OWNER_CHAT_ID"])

text = planner.run("Дай короткий план на сегодня.")
t = requests.get("https://api.aladhan.com/v1/timingsByCity",
                  params={"city": "Almaty", "country": "Kazakhstan", "method": 2}).json()["data"]["timings"]
text += f"\n\nНамаз: Фаджр {t['Fajr']}, Зухр {t['Dhuhr']}, Аср {t['Asr']}, Магриб {t['Maghrib']}, Иша {t['Isha']}"
requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": OWNER, "text": text})
