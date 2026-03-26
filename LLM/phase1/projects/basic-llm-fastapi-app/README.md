# Basic LLM FastAPI App

This is the first hands-on project in the LLM roadmap.

The goal is to build a very small but clean LLM backend that teaches:

- basic OpenAI API usage
- FastAPI integration
- structured output handling
- local development workflow

Model policy:

- this project is locked to `gpt-5-mini`
- request payloads do not allow changing the model
- if another model is mentioned in code changes later, it should not be used unless we intentionally update the app

## What This App Does

Endpoints:

- `GET /health`
- `POST /chat`
- `POST /extract`

## Learning Goals

- send a prompt to a model
- return a normal text response
- return structured JSON from model output
- keep the code small and easy to understand

## Project Structure

- `app/main.py`
- `pyproject.toml`
- `run.md`

## Setup

1. Sync dependencies with `uv`:

```bash
uv sync
```

2. Set your API key:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

3. Run the app:

```bash
uv run uvicorn app.main:app --reload
```

## Endpoints

## `GET /health`

Returns basic app status.

## `POST /chat`

Example body:

```json
{
  "message": "Explain RAG in simple words"
}
```

## `POST /extract`

Example body:

```json
{
  "text": "Divesh worked on FastAPI, AWS, Docker, and CI/CD automation."
}
```

Expected behavior:

- return structured fields like `skills`, `summary`, and `role_fit`

## Next Improvements

- add request validation
- add error logging
- add prompt versioning
- add simple tests
- add Docker support

## Notes

- Keep the first version intentionally small.
- We can improve prompts, validation, and deployment after the app works end to end.

## References

- OpenAI Responses API: https://platform.openai.com/docs/guides/migrate-to-responses
- OpenAI structured outputs: https://platform.openai.com/docs/guides/structured-outputs
- OpenAI tools: https://platform.openai.com/docs/guides/tools
