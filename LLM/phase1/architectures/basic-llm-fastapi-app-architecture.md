# Basic LLM FastAPI App Architecture

## Purpose

This project is the smallest architecture that still demonstrates a useful LLM backend flow.

## Main Components

- FastAPI app
- request models
- OpenAI client creation
- fixed model selection
- chat endpoint
- extraction endpoint

## Request Flow

1. Client sends HTTP request to FastAPI.
2. FastAPI validates the request body.
3. The app creates an OpenAI client using `OPENAI_API_KEY`.
4. The app sends the system prompt and user input to `gpt-5-mini`.
5. The model returns output text.
6. The app returns plain text or parses JSON before responding.

## Strengths

- simple and easy to understand
- low code complexity
- good for first end-to-end learning

## Limitations

- model output validation is basic
- prompts live inline in code
- no logging or retries
- no testing or monitoring

## Why This Architecture Is Good For Phase 1

It keeps the moving parts small enough to learn the fundamentals without hiding them behind abstractions.
