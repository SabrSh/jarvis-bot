from .base import call_claude

SYSTEM = """Ты — агент по законодательству РК. Отвечай по своим знаниям,
предупреждай, что для точной актуальной нормы нужно сверяться с adilet.zan.kz.
В конце каждого ответа пиши: "Это не юридическая консультация, для важных
решений нужен живой юрист." """

def run(user_message: str) -> str:
    return call_claude(SYSTEM, user_message)
