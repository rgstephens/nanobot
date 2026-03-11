# Model Cost

- Top [OpenClaw Models](https://openrouter.ai/apps?url=https%3A%2F%2Fopenclaw.ai%2F)
- [Free OpenClaw Models](https://openrouter.ai/models?max_price=0&utm_campaign=Welcome+Email+Campaign+%232&utm_content=Welcome-email&utm_medium=email_action&utm_source=customer.io)
- [Poe Model List & Pricing](https://poe.com/api/models)
- [Poe Model List in JSON](https://api.poe.com/v1/models)

## Model Shortlist

- Minimax is good except for complex, multi-step
- Trinity is also pretty good for a simple model
- glm-5
- claude-sonnet-4.5

## Model Pricing

Pricing sourced from `poe_models.json`. All costs in USD per 1M tokens.

| Provider   | ID                                  | Input | Output | Email | Images | Notes                                           |
| ---------- | ----------------------------------- | ----: | -----: | :---: | :----: | ----------------------------------------------- |
| OpenRouter | arcee-ai/trinity-large-preview:free | $0.00 |  $0.00 |       |        | infinite loop deleting skill                    |
| OpenRouter | stepfun/step-3.5-flash:free         | $0.00 |  $0.00 |       |        | can't install skill                             |
| Poe        | glm-4.7-flash                       | $0.07 |  $0.40 |       |   No   |                                                 |
| Poe        | glm-4.6v                            | $0.30 |  $0.90 |   F   |  Yes   | fargo tool infinite loop                        |
| OpenRouter | minimax/minimax-m2.5                | $0.27 |  $0.95 |       |        | Daily email forgets                             |
| Poe        | gpt-4o-mini                         | $0.14 |  $0.54 |   F   |  Yes   | Failed finding skills                           |
| Poe        | gemini-2.5-flash                    | $0.21 |  $1.80 |       |  Yes   | Infinite loop                                   |
| OpenRouter | stepfun/step-3.5-flash              | $0.10 |  $0.30 |       |        |                                                 |
| Poe        | gpt-5-mini                          | $0.22 |  $1.80 |   D   |  Yes   | Asked to confirm and for permission, too chatty |
| Poe        | gpt-5.1-codex-mini                  | $0.22 |  $1.80 |       |   No   | Why does it hit max tool calls?                 |
| OpenAI     | gpt-5.1-codex-mini                  | $0.25 |  $2.00 |       |   No   | need key for OpenAICodex                        |
| Poe        | gemini-3-flash                      | $0.40 |  $2.40 |       |  Yes   |                                                 |
| OpenRouter | google/gemini-2.5-flash             | $0.30 |  $2.50 |       |  Yes   |                                                 |
| OpenRouter | google/gemini-3-flash-preview       | $0.50 |  $3.00 |       |  Yes   |                                                 |
| Poe        | kimi-k2.5                           | $0.06 |  $3.00 |   C   |  Yes   | Poor formatting and rate limit handling         |
| GLM-5      | glm-5                               | $1.00 |  $3.20 |   B   |   No   | Good, no images                                 |
| Poe        | qwen3.5-397b-a17b                   | $0.60 |  $3.60 |  B-   |  Yes   |
| Poe        | claude-haiku-4.5                    | $0.85 |  $4.30 |   C   |  Yes   |                                                 |
| Poe        | gemini-2.5-pro                      | $0.87 |  $7.00 |       |  Yes   |                                                 |
| OpenAI     | gpt-5-search-api                    | $1.25 | $10.00 |       |        |                                                 |
| Poe        | claude-sonnet-4.5                   | $2.60 | $13.00 |   A   |  Yes   | Excellent                                       |
