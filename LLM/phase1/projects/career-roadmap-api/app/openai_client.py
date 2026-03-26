import json
import os

from fastapi import HTTPException
from openai import OpenAI


LOCKED_MODEL = "gpt-5-mini"


def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY is not set")
    return OpenAI(api_key=api_key)


def create_text_response(system_prompt: str, user_prompt: str) -> str:
    client = get_client()
    response = client.responses.create(
        model=LOCKED_MODEL,
        input=[
            {
                "role": "system",
                "content": [{"type": "input_text", "text": system_prompt}],
            },
            {
                "role": "user",
                "content": [{"type": "input_text", "text": user_prompt}],
            },
        ],
    )
    return response.output_text


def create_json_response(system_prompt: str, user_prompt: str) -> dict:
    output = create_text_response(system_prompt=system_prompt, user_prompt=user_prompt)
    try:
        return json.loads(output)
    except json.JSONDecodeError as exc:
        raise HTTPException(
            status_code=500,
            detail={
                "message": "Model did not return valid JSON",
                "raw_output": output,
            },
        ) from exc
