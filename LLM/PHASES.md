# Phase Guide

This file is the execution guide for the LLM roadmap.

It answers two questions for every phase:

1. What are we going to build?
2. What will each project teach us?

The idea is simple:

- every phase has a clear learning goal
- every phase has project work
- every project should level up one or more real skills

## Phase 1

Theme:

- LLM fundamentals for builders

Goal:

- understand how to call an LLM from code
- learn prompt structure
- learn structured output
- get comfortable building small FastAPI-based AI backends

Projects:

### 1. `basic-llm-fastapi-app`

What it is:

- a very small FastAPI app with `chat` and `extract` endpoints

What it teaches:

- OpenAI API integration
- request to response flow
- fixed model usage
- simple prompting
- basic structured JSON extraction
- first local LLM backend setup

Why it matters:

- this is the first working bridge between theory and implementation

### 2. `career-roadmap-api`

What it is:

- a multi-endpoint API for profile analysis, plan generation, and interview answer review

What it teaches:

- multiple endpoints in one LLM app
- reusable OpenAI client logic
- better schema design with Pydantic
- stronger structured output handling
- prompt specialization by use case
- backend code organization

Why it matters:

- this moves us from toy app level to more practical API design

Expected outcome of Phase 1:

- confidence with basic LLM app building
- ability to use `gpt-5-mini` from FastAPI
- understanding of prompt sensitivity
- comfort with structured output and response validation

## Phase 2

Theme:

- RAG systems

Goal:

- learn how to use external documents as grounded context
- understand embeddings, retrieval, chunking, and citation-based answering

Projects:

### 1. `resume-and-interview-rag-assistant`

What it is:

- a document-grounded assistant using resume files, interview notes, and topic documents

What it teaches:

- file ingestion
- text chunking
- embeddings
- vector storage
- retrieval pipelines
- grounded answer generation
- citation-style output

Why it matters:

- this is the first step from plain prompting to context-aware AI systems

### 2. `topic-revision-rag-api`

What it is:

- an API that answers revision questions using your study notes and recap material

What it teaches:

- multi-document retrieval
- retrieval quality tuning
- prompt design for grounding
- answer evaluation for hallucination control

Why it matters:

- this project makes your own repository part of your learning system

Expected outcome of Phase 2:

- ability to build a useful RAG application
- understanding of retrieval tradeoffs
- stronger grounding and evaluation habits

## Phase 3

Theme:

- agents and workflows

Goal:

- learn how to build multi-step systems where the model reasons across tasks and tools

Projects:

### 1. `interview-coach-agent`

What it is:

- an agent that asks interview questions, scores answers, gives follow-ups, and suggests next study topics

What it teaches:

- workflow design
- multi-step reasoning
- answer review loops
- memory and state passing
- prompt chaining

Why it matters:

- this introduces agent-style orchestration without jumping straight into complex autonomous systems

### 2. `learning-roadmap-agent`

What it is:

- an agent that turns goals, skill gaps, and available time into a practical study plan

What it teaches:

- tool selection logic
- structured planning output
- stateful workflows
- user-goal decomposition

Why it matters:

- this develops the thinking needed for higher-value assistant systems

Expected outcome of Phase 3:

- ability to design workflows beyond one-shot prompts
- understanding of when an agent is useful and when it is not

## Phase 4

Theme:

- LLMOps and production readiness

Goal:

- learn how to make LLM apps reliable, observable, testable, and cost-aware

Projects:

### 1. `production-ready-ai-backend`

What it is:

- one of the earlier projects upgraded with logging, config, cost controls, and deployment support

What it teaches:

- prompt versioning
- request logging
- output monitoring
- cost awareness
- failure handling
- configuration management
- deployment basics

Why it matters:

- many people can demo an AI app, fewer can make one stable enough to ship

### 2. `llm-eval-suite`

What it is:

- a small evaluation framework for testing prompts and response quality on fixed test cases

What it teaches:

- eval design
- regression checks
- quality measurement
- comparison between prompt versions

Why it matters:

- this is where backend maturity starts to show

Expected outcome of Phase 4:

- ability to talk about production concerns in interviews
- ability to improve reliability, not just features

## Phase 5

Theme:

- open-source models and local serving

Goal:

- understand how hosted and local model setups differ in cost, speed, and control

Projects:

### 1. `dual-model-ai-backend`

What it is:

- one API app that can work with hosted models and local/open models

What it teaches:

- provider abstraction
- config-based model switching
- hosted vs local tradeoffs
- response quality comparison

Why it matters:

- this gives practical flexibility beyond one provider

### 2. `local-model-serving-lab`

What it is:

- a small project using Ollama or another local serving stack for experiments

What it teaches:

- local model setup
- inference workflow
- resource tradeoffs
- latency and quality comparison

Why it matters:

- it helps you understand infrastructure choices, not just API calls

Expected outcome of Phase 5:

- ability to compare hosted and local serving
- better platform thinking for AI systems

## How To Use This File

Before starting a new phase:

- read the phase goal
- understand the projects in that phase
- know what each project is supposed to teach

After finishing a phase:

- update notes
- update revision docs
- add interview questions
- write down what felt easy and what felt hard

## Current Status

Current phase:

- `Phase 1`

Current completed or started projects:

- `basic-llm-fastapi-app`
- `career-roadmap-api`
