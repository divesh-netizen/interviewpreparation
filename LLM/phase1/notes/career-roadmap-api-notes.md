# Career Roadmap API Notes

## Goal

Build a more practical LLM API with multiple endpoints and cleaner code organization.

## Main Endpoints

- `GET /health`
- `POST /analyze-profile`
- `POST /generate-plan`
- `POST /review-answer`

## What I Learn Here

- how to split logic across files
- how to reuse model-calling code
- how to use Pydantic schemas for request validation
- how prompts change based on endpoint purpose
- how structured output becomes more important as the app grows

## Important Observation

- a single helper for model calls reduces duplication
- endpoint-specific prompts make output more focused
- schema-based request validation improves API reliability

## Why This Project Matters

This project is closer to a real AI backend than the first one.

It teaches:

- code organization
- practical API design
- multiple use cases in one app

## Weak Spots To Improve Later

- response schema validation
- stronger prompt templates
- logging
- cost tracking
- tests
