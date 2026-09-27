import os
from anthropic import Anthropic

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
MODEL = "claude-haiku-4-5-20251001"

def call_claude(system_prompt: str, user_message: str, max_tokens: int = 400) -> str:
    resp = client.messages.create(
        model=MODEL, max_tokens=max_tokens,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )
    return "\n".join(b.text for b in resp.content if getattr(b, "type", "") == "text").strip()
