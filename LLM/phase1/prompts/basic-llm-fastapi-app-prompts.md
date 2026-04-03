# Basic LLM FastAPI App Prompts

## Purpose

This file captures the prompt intent used in the first project.

## Chat Prompt

System prompt intent:

- act like a clear and concise teaching assistant for beginner LLM developers

Why it works:

- it keeps the tone simple
- it keeps answers beginner-friendly
- it matches the learning goal of the project

Possible improvements:

- ask for shorter answers
- ask for examples
- ask for answer structure like definition plus example plus limitation

## Extract Prompt

System prompt intent:

- extract career information from user text
- return valid JSON only
- use the keys `summary`, `skills`, and `role_fit`

Why it works:

- it teaches structured output
- it keeps output shape predictable

Possible improvements:

- define exact JSON schema more clearly
- define the expected type for each field
- add examples of good and bad extraction behavior
