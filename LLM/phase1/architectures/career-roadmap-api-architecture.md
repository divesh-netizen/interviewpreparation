# Career Roadmap API Architecture

## Purpose

This project uses a slightly more realistic backend layout to teach cleaner API design for LLM applications.

## Main Components

- FastAPI app entrypoint
- request schemas in `schemas.py`
- reusable OpenAI logic in `openai_client.py`
- multiple endpoint handlers
- fixed model policy with `gpt-5-mini`

## Request Flow

1. Client sends request to one of the endpoints.
2. FastAPI validates the input using Pydantic schemas.
3. Endpoint creates a use-case-specific system prompt.
4. Shared OpenAI helper sends the prompt and user content to `gpt-5-mini`.
5. The response is parsed as JSON.
6. Parsed output is returned to the API caller.

## Strengths

- cleaner separation of concerns
- less duplicate code
- better maintainability than a single-file app
- easier to extend with more endpoints later

## Limitations

- response validation is still lightweight
- prompts are still inline strings
- no persistence layer
- no test suite yet
- no observability or cost controls yet

## Why This Architecture Is Good For Phase 1

It introduces better backend structure without becoming too complex for a beginner learning phase.
