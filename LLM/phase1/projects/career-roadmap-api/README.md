# Career Roadmap API

This is the second project for `Phase 1`.

It is more practical than the first app and teaches a few more backend patterns while still staying small enough for beginner-friendly learning.

## What This Project Teaches

- multiple API endpoints
- reusable OpenAI client logic
- stronger structured output handling
- Pydantic request and response schemas
- prompt design for different use cases
- validation and error handling

## Model Policy

- this project is locked to `gpt-5-mini`
- request payloads do not allow model selection

## Endpoints

- `GET /health`
- `POST /analyze-profile`
- `POST /generate-plan`
- `POST /review-answer`

## Use Cases

### `POST /analyze-profile`

Analyze a profile and target role.

Example:

```json
{
  "profile_summary": "Python backend developer with FastAPI, Docker, AWS, and CI/CD experience.",
  "target_role": "AI Backend Engineer"
}
```

### `POST /generate-plan`

Generate a weekly learning plan.

Example:

```json
{
  "current_skills": ["Python", "FastAPI", "AWS", "Docker", "CI/CD"],
  "target_role": "LLM Application Engineer",
  "duration_weeks": 6
}
```

### `POST /review-answer`

Review an interview answer.

Example:

```json
{
  "question": "Explain what RAG is and why it is useful.",
  "answer": "RAG combines retrieval with generation so the model can answer using external documents."
}
```

## Setup

```bash
cd /mnt/e/study/interviewpreparation/LLM/phase1/projects/career-roadmap-api
uv sync
export OPENAI_API_KEY="your_api_key_here"
uv run uvicorn app.main:app --reload
```

## Why This Is A Good Phase 1 Project

This project is still simple enough to understand, but it starts teaching how to build an LLM-backed backend around:

- career planning
- structured responses
- prompt reuse
- practical output validation

It is a better bridge from a toy app to a more realistic AI backend.
