import json
import os

from fastapi import FastAPI, HTTPException
from openai import OpenAI
from pydantic import BaseModel


LOCKED_MODEL = "gpt-5-mini"


class ChatRequest(BaseModel):
    message: str


class ExtractRequest(BaseModel):
    text: str


app = FastAPI(title="Basic LLM FastAPI App")


def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY is not set")
    return OpenAI(api_key=api_key)


@app.get("/health")
async def health() -> dict:
    return {
        "status": "ok",
        "project": "basic-llm-fastapi-app",
        "model": LOCKED_MODEL,
        "model_selection": "locked",
    }


@app.post("/chat")
async def chat(request: ChatRequest) -> dict:
    client = get_client()

    response = client.responses.create(
        model=LOCKED_MODEL,
        input=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "input_text",
                        "text": "You are a clear and concise teaching assistant for beginner LLM developers.",
                    }
                ],
            },
            {
                "role": "user",
                "content": [{"type": "input_text", "text": request.message}],
            },
        ],
    )

    return {"model": LOCKED_MODEL, "answer": response.output_text}


@app.post("/extract")
async def extract(request: ExtractRequest) -> dict:
    client = get_client()

    response = client.responses.create(
        model=LOCKED_MODEL,
        input=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "input_text",
                        "text": (
                            "Extract structured career information from the user text. "
                            "Return valid JSON only with keys: summary, skills, role_fit."
                        ),
                    }
                ],
            },
            {
                "role": "user",
                "content": [{"type": "input_text", "text": request.text}],
            },
        ],
    )

    try:
        parsed = json.loads(response.output_text)
    except json.JSONDecodeError as exc:
        raise HTTPException(
            status_code=500,
            detail={
                "message": "Model did not return valid JSON",
                "raw_output": response.output_text,
            },
        ) from exc

    return {"model": LOCKED_MODEL, "data": parsed}
