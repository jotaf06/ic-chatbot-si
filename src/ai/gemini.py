import json
import os
import google.generativeai as genai
from src.ai.prompts import SYSTEM_PROMPT

_model = None


def _get_model():
    global _model
    if _model is None:
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        _model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=SYSTEM_PROMPT,
        )
    return _model


def parse_intent(user_message: str) -> dict:
    try:
        response = _get_model().generate_content(user_message)
        return json.loads(response.text.strip())
    except (json.JSONDecodeError, Exception):
        return {"intent": "unknown", "term": ""}
