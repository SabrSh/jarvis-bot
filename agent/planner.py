from .base import call_claude

SYSTEM = """Ты — агент-планировщик. Разбирай сообщения о делах на события
с названием, временем, местом. Если данных не хватает — спроси."""

def run(user_message: str) -> str:
    return call_claude(SYSTEM, user_message)
