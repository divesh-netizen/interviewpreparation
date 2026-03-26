# Week 1 Notes

## Goal

Build the smallest working LLM app and understand the core building blocks behind it.

## Topics To Understand

## 1. Tokens

- Models read and generate tokens, not plain words.
- More input and output tokens usually means more cost and more latency.
- Context window means how much information the model can handle in one request.

Interview-style explanation:

- A token is a small unit of text processed by the model. Prompt size and response size both affect cost, latency, and context usage.

## 2. Prompt Roles

- `system`: high-level behavior and rules
- `user`: the actual request
- `assistant`: previous model responses when continuing a conversation

Interview-style explanation:

- Prompt roles help separate instructions, user intent, and conversation history so the model behaves more predictably.

## 3. Structured Output

- Instead of asking for free-form text only, ask for predictable JSON.
- This helps backend systems consume LLM output safely.

Why it matters:

- easier parsing
- easier validation
- better API integration

## 4. Tool Calling

- The model can decide when to use an external tool.
- A tool can be a function, database lookup, calculator, API, or search step.

Important idea:

- The model should not guess when a tool can provide a reliable answer.

## 5. Embeddings

- Embeddings convert text into vectors.
- Similar meaning ends up closer in vector space.
- Embeddings are the base of most RAG systems.

Interview-style explanation:

- Embeddings help retrieve semantically similar content, which is why they are used in document search and RAG pipelines.

## 6. Responses API

- The Responses API is the modern OpenAI API for model responses and tool-oriented workflows.
- It is a good default starting point for new LLM app development.

## This Week's Build

Project:

- `basic-llm-fastapi-app`

Endpoints:

- `/health`
- `/chat`
- `/extract`

What each endpoint teaches:

- `/health`: confirms app is running
- `/chat`: basic prompt to response flow
- `/extract`: structured JSON output from unstructured text

## Revision Questions

1. What is the difference between prompt text length and token count?
2. Why is structured output useful in backend systems?
3. When should a model call a tool instead of answering directly?
4. What is the role of embeddings in RAG?
5. Why is the Responses API a good default for modern LLM apps?

## Practical Reminders

- Keep prompts simple at first.
- Do not over-engineer the first app.
- Focus on one clean working flow.
- Save every useful learning as a short note.

## End Of Week Success Check

By the end of this week, I should have:

- one working FastAPI app
- one OpenAI API integration
- one structured extraction endpoint
- one notes file
- one GitHub commit with clear progress
