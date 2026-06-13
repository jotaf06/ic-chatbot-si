import json
import os
from groq import Groq
from src.ai.prompts import SYSTEM_PROMPT

_client = None


def _get_client() -> Groq:
    global _client
    if _client is None:
        _client = Groq(api_key=os.environ["GROQ_API_KEY"])
    return _client


def _extract_json(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[-1]
        text = text.rsplit("```", 1)[0]
    return text.strip()


def parse_intent(user_message: str) -> dict:
    try:
        response = _get_client().chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
        )
        text = response.choices[0].message.content
        print(f"[llm] raw: {text!r}")
        result = json.loads(_extract_json(text))
        print(f"[llm] parsed: {result}")
        return result
    except json.JSONDecodeError as e:
        print(f"[llm] JSON error: {e}")
        return {"intent": "unknown", "term": ""}
    except Exception as e:
        print(f"[llm] Error: {e}")
        return {"intent": "unknown", "term": ""}
