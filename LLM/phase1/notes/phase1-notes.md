# Phase 1 Notes

Phase 1 is about becoming comfortable with the basics of LLM application development.

The focus is not advanced AI theory. The focus is learning how to build small, reliable AI-backed APIs.

## What Phase 1 Covers

- calling a hosted LLM from code
- understanding request to response flow
- using FastAPI as the backend layer
- writing better prompts
- returning structured JSON
- validating and organizing backend code

## Projects In This Phase

### `basic-llm-fastapi-app`

Main learning:

- first OpenAI integration
- basic chat endpoint
- JSON extraction endpoint
- fixed model usage with `gpt-5-mini`

Key lesson:

- LLM output is useful, but it still needs instructions and validation.

### `career-roadmap-api`

Main learning:

- multi-endpoint LLM API
- reusable OpenAI client helper
- Pydantic request schemas
- stronger prompt design per endpoint

Key lesson:

- once an app grows beyond one endpoint, code organization starts to matter a lot.

## Important Concepts

### Prompting

- better prompts usually produce more reliable output
- tighter instructions often improve structure
- vague prompts often create vague responses

### Structured output

- plain text is easy to read
- structured JSON is easier for backend systems to use
- JSON output is more fragile and should be validated

### Model policy

- both projects are locked to `gpt-5-mini`
- keeping one model fixed makes early learning simpler
- reducing model variation also helps control cost and behavior

## Main Takeaways

- FastAPI is a good first backend framework for LLM projects.
- Small projects are enough to learn the fundamentals.
- Reusable client helpers are worth adding early.
- Structured output is one of the most important backend skills in LLM application work.

## What Phase 1 Should Give Me

By the end of this phase, I should be able to:

- create and run a small LLM backend
- write prompts for different API use cases
- return useful JSON instead of only plain text
- think about reliability, not just raw output
