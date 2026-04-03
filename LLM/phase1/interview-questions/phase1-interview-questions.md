# Phase 1 Interview Questions

## Core Questions

1. What is the role of FastAPI in your Phase 1 projects?
2. Why did you lock both projects to `gpt-5-mini`?
3. What is the difference between plain text output and structured output?
4. Why is structured output important for backend systems?
5. What is the benefit of using a shared OpenAI client helper?
6. Why did you separate schemas from endpoint logic?
7. What are the risks of trusting model output directly?
8. Why is prompt design important even for small apps?
9. What does request validation protect you from?
10. Why is code organization already important in a small LLM project?

## Project-Specific Questions

### `basic-llm-fastapi-app`

1. What does the `/chat` endpoint teach you?
2. What does the `/extract` endpoint teach you?
3. Why is JSON parsing a useful exercise in the first project?
4. What problems can happen if the model does not return valid JSON?

### `career-roadmap-api`

1. Why did you split this project into `main.py`, `schemas.py`, and `openai_client.py`?
2. What is the purpose of the `/analyze-profile` endpoint?
3. How is `/generate-plan` different from `/review-answer` from a prompt-design perspective?
4. Why does this second project represent a step up from the first one?

## Interview-Style Answers To Practice

### Why `gpt-5-mini`?

Use answer:

`I fixed the model to gpt-5-mini so early learning stayed consistent in terms of cost, behavior, and debugging. I wanted to focus first on backend patterns and prompt quality instead of mixing provider and model variability.`

### Why structured output?

Use answer:

`Structured output makes the LLM response easier for backend systems to consume, validate, and reuse. Plain text is readable, but JSON is much more useful for APIs and downstream workflows.`

### Why build two projects in Phase 1?

Use answer:

`The first project taught the minimum end-to-end flow. The second project introduced better code organization, multiple endpoints, reusable helpers, and stronger schema-based design.`
