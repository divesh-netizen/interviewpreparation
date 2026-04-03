# Basic LLM FastAPI App Notes

## Goal

Build the smallest possible useful LLM backend.

## Main Endpoints

- `GET /health`
- `POST /chat`
- `POST /extract`

## What I Learn Here

- how to make the first API call to the model
- how to pass a system prompt and a user prompt
- how to return model output through FastAPI
- how to parse JSON output from the model

## Important Observation

- plain response generation is easier than JSON extraction
- extraction is more sensitive to prompt wording
- model output should not be trusted blindly

## Why This Project Matters

This project removes fear from the first AI backend build. It proves that I can:

- run a real app
- call a real model
- return useful output

## Weak Spots To Improve Later

- stronger JSON validation
- retry logic
- better error handling
- prompt versioning
