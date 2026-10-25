# Item 11 · Model trailer audit (ES: auditoría del tráiler Model)

**State:** read-only history audit; no commit history rewritten.

The six observed default-branch histories contain 2,999 commits. The parser found at most one `Model` value per commit. Missing values are `NO_DATA`, cause: no `Model` trailer is present. Historical commits are left unchanged; the merged X2 hook proposal remains unimplemented pending HITL.

| Exact value | Count | Mapping |
|---|---:|---|
| `GPT-6` | 3 | ChatGPT (OpenAI) |
| `GPT-6.1-Sol` | 7 | ChatGPT (OpenAI) |
| `gpt-6.1-sol` | 13 | ChatGPT (OpenAI) |
| `Codex` | 6 | ChatGPT/OpenAI product; underlying model `NO_DATA` |
| `GLM (Vibe)` | 68 | `NO_DATA`: exact value not mapped to either allowed provider |
| `Vibe` | 17 | `NO_DATA`: value alone does not identify a provider |

OpenAI’s official [model catalog](https://developers.openai.com/api/docs/models) identifies GPT-6 and GPT-6.1 Sol. Its [Codex guidance](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan) says the underlying model depends on version and configuration. The [Mistral catalog](https://docs.mistral.ai/models) lists Z.ai GLM as third-party; no exact `GLM (Vibe)` or `Vibe` mapping is established here. No `Mistral` value was observed.

## Receipt

source=study#61/11; date=2026-10-25; parser=standalone+compact Model labels; duplicate_model=0; study=176:29:147@b9a420b; lab=175:16:159@a60908d; app=464:11:453@a88bf42; web=1251:39:1212@2d880ab; p0x=864:15:849@9656ff3; buzon=69:4:65@472caf9; totals=2999:114:2885; tuple=commits:present:missing; missing_cause=no Model trailer; history_changes=0; state=proposal
