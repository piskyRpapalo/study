# Item 11 · Model trailer audit (ES: auditoría del tráiler Model)

**State:** read-only history audit; no commit history rewritten.

Six default histories: 2,999 commits; 114 with one `Model` value; 2,885 missing it (`NO_DATA`, cause: no trailer). No duplicate fields. History is unchanged; the X2 hook still awaits HITL.

Mapping and counts are in the receipt. OpenAI’s [model catalog](https://developers.openai.com/api/docs/models) identifies GPT-6 and GPT-6.1 Sol. OpenAI’s [Codex guidance](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan) says its underlying model varies by version/configuration. The [Mistral catalog](https://docs.mistral.ai/models) lists Z.ai GLM as third-party; the exact `GLM (Vibe)` value remains unmapped. No `Mistral` value was observed.

## Receipt

source=study#61/11; date=2026-10-25; parser=standalone+compact Model labels; map=GPT-6:ChatGPT/3,GPT-6.1-Sol:ChatGPT/7,gpt-6.1-sol:ChatGPT/13,Codex:ChatGPT-product+base-NO_DATA/6,GLM-(Vibe):NO_DATA/68,Vibe:NO_DATA/17; study=176:29:147@b9a420b; lab=175:16:159@a60908d; app=464:11:453@a88bf42; web=1251:39:1212@2d880ab; p0x=864:15:849@9656ff3; buzon=69:4:65@472caf9; totals=2999:114:2885; tuple=commits:present:missing; missing_cause=no Model trailer; history_changes=0; state=proposal
