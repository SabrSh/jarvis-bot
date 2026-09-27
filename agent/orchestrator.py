from agents.base import call_claude
from agents import planner, study, lawyer, critic

ROUTER_SYSTEM = """Определи, к какому агенту относится сообщение пользователя.
Ответь ОДНИМ словом: planner, study, lawyer или other."""

AGENTS = {"planner": planner.run, "study": study.run, "lawyer": lawyer.run}

def classify(user_message: str) -> str:
    label = call_claude(ROUTER_SYSTEM, user_message, max_tokens=10).strip().lower()
    return label if label in AGENTS else "other"

def handle_message(user_message: str) -> str:
    route = classify(user_message)
    if route == "other":
        return call_claude("Ты — Jarvis, личный помощник. Отвечай кратко.", user_message)
    draft = AGENTS[route](user_message)
    return critic.review(draft)
