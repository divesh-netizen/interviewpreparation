# Career Roadmap API Prompts

## Purpose

This file captures the prompt strategy for each endpoint in the second project.

## `analyze-profile`

Prompt intent:

- analyze the learner profile
- identify strengths
- identify gaps
- estimate role fit
- suggest next focus areas

Why it works:

- it turns open-ended career advice into structured backend output

## `generate-plan`

Prompt intent:

- generate a realistic weekly plan
- keep the output structured
- turn current skills plus target role into steps

Why it works:

- it teaches planning-style prompts
- it teaches array and object style JSON output

## `review-answer`

Prompt intent:

- review a technical answer
- give strengths
- give weaknesses
- provide an improved answer

Why it works:

- it teaches evaluation prompts
- it is practical for interview preparation

## General Prompt Design Notes

- each endpoint has its own purpose
- each endpoint needs a more focused system prompt
- tighter instructions usually improve JSON reliability
- prompt specialization is better than reusing one generic prompt everywhere
