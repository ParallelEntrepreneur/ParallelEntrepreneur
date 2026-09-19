<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.png">
  <img src="assets/header-light.png" alt="Parallel Entrepreneur. I build companies that run on agents. Several at once." width="100%">
</picture>

<p align="center">
  <a href="https://factory0.ventures"><img src="https://img.shields.io/badge/STUDIO-FACTORY0.VENTURES-F5A524?style=for-the-badge&labelColor=0A0B0D" alt="Studio: factory0.ventures"></a>
  <img src="https://img.shields.io/badge/BASE-BALI%20%C2%B7%20UTC%2B8-EEEBE3?style=for-the-badge&labelColor=0A0B0D" alt="Base: Bali, UTC+8">
</p>

## Several companies, one operating system

Most founders give one company a decade. I start several at the same time.

That only works because none of them is built from scratch. Every company sits on
one shared operating system: identity, payments, deployment, observability, agent
orchestration and knowledge are written once and inherited. Each company keeps its
own product, customers, data and P&L. Agents do the work of running them, from
research and engineering to support, content and growth. People set the direction,
hold the boundaries and make the calls that need a person.

The studio this runs in is [Factory Zero](https://factory0.ventures): one operator
and a network of agents. The claim being tested is that a studio that size can hold
this many companies at once. Nine are in the pipeline today, between validation and
launch. Judge it on the outputs.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/operating-model-dark.png">
  <img src="assets/operating-model-light.png" alt="One system, many companies. People set direction and taste. A control surface of permission scopes, spend caps, tool schemas, evaluation rubrics, escalation rules and an append-only ledger. Agents across discover, build, operate, distribute and learn. A shared foundation written once. Nine companies running in parallel." width="100%">
</picture>

## The nine

Numbered as they appear on the traces above, at the stage each one has actually
reached in the [Factory Zero registry](https://factory0.ventures/ventures/).

| Company | What it is | Stage |
| :--- | :--- | :--- |
| <img src="assets/companies/kontinuum.svg" width="48" alt="Kontinuum"><br>**[Kontinuum](https://kontinuum.audio)**<br><sub>`01` · Music</sub> | An AI composer on a deterministic real-time engine: music written and performed continuously, personalised to the listener and playable offline. | `PROTOTYPE` |
| <img src="assets/companies/undercover-rockstars.svg" width="48" alt="Undercover Rockstars"><br>**[Undercover Rockstars](https://undercoverrockstars.com)**<br><sub>`02` · Apparel</sub> | A clothing house where every piece is a matched day-and-night pair. People cut the garments; agents are meant to run stock, orders, support and the next drop's brief. | `LAUNCH` |
| <img src="assets/companies/yoginini.svg" width="48" alt="Yoginini"><br>**[Yoginini](https://yoginini.us)**<br><sub>`03` · Wellness</sub> | Building a yoga teacher that can see you: an on-device pose model with one calm correction at a time, and no video leaving the phone. | `VALIDATION` |
| <img src="assets/companies/cratefield.svg" width="48" alt="Cratefield"><br>**[Cratefield](https://cratefield.com)**<br><sub>`04` · Infrastructure</sub> | A backend you compile rather than configure. The open-source Rust harness underneath it is already public. | `VALIDATION` |
| <img src="assets/companies/vibecaddie.svg" width="48" alt="VibeCaddie"><br>**[VibeCaddie](https://vibecaddie.com)**<br><sub>`05` · Devtools</sub> | Building a code review agent for code you didn't fully write: it loads only the review skills that apply and ranks findings by severity. | `VALIDATION` |
| <img src="assets/companies/colonizer.svg" width="48" alt="Colonizer"><br>**[Colonizer](https://colonizer.dev)**<br><sub>`06` · Devtools</sub> | Turns GitHub issues into pull requests, with each task's coding agent in its own disposable microVM. Runs locally today. | `PROTOTYPE` |
| <img src="assets/companies/findsyou.svg" width="48" alt="FindsYou.work"><br>**[FindsYou.work](https://findsyou.work)**<br><sub>`07` · Careers</sub> | Building a job search that runs without you, where the product is the rejection: every role you could never take is discarded, with the reason shown. | `VALIDATION` |
| <img src="assets/companies/supportgenius.svg" width="48" alt="SupportGenius"><br>**[SupportGenius](https://supportgeni.us)**<br><sub>`08` · Support</sub> | Building a support agent that answers from a company's own docs and, when it cannot, writes the ticket for it: one model drafts, an independent one checks it, and it is filed where that team already works. | `VALIDATION` |
| <img src="assets/companies/promptdecode.svg" width="48" alt="promptdecode"><br>**[promptdecode](https://promptdeco.de)**<br><sub>`09` · Security</sub> | Finds text a reviewer cannot see and a model reads anyway. The decoder runs in the browser today; the scanners that would catch it in CI are being built. | `VALIDATION` |

## Agent-native, in production

The model had a proving ground before the studio existed. I have run the same company
since 2017, and it is now built so that anything a person can do in the operator
console, an agent can do through a CLI, an MCP server or a typed SDK. It is live in
six countries, with real money moving through it.

- About a hundred agents cover engineering, operations and go-to-market.
- Human headcount went from 25+ to four operators, while shipping roughly three times faster.
- I don't hold the CEO title there. I manage the CEO agent.

## What makes autonomy safe to ship

Handing work to an agent is the easy part. Keeping it safe in production is the job,
and most of that job is writing.

- **Scoped authority.** Per-agent permission scopes, scoped API tokens and spend caps.
  An agent can do what its role allows and nothing beside it.
- **A ledger, not a log.** Every agent action lands in an append-only ledger, so it can
  be audited and reversed.
- **Written specification.** Tool schemas, evaluation rubrics and escalation rules
  decide what an agent may do and when a person takes over.
- **Evaluation before exposure.** Models fine-tuned on domain data, self-learning loops
  that feed each run into the next, and a readiness review before any agent capability
  reaches a customer.

<p align="center">
  <img src="assets/traces.svg" alt="" width="100%">
</p>

## How I got here

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/timeline-dark.png">
  <img src="assets/timeline-light.png" alt="Timeline. 2002: digitised a paper-based claims process and moved into engineering. 2012: machine learning in production. 2015: the question of what can safely be delegated. 2017: an agent-native platform. 2026: many companies in parallel." width="100%">
</picture>

I put machine learning in front of customers for the first time in 2012: automated
advice built on the data people chose to share, in a market where automated advice
is supervised advice. Every recommendation had to be explainable and auditable, and
I owned the tradeoffs between automation, explainability and coverage.

Reading Bostrom's *Superintelligence* in 2015 sharpened that into the question I have
worked on ever since: what can safely be delegated to a system, and what has to stay
with a person? Everything on this page is my answer, tested in production rather than
in argument.

## Toolbox

**Agents** &nbsp; MCP servers · tool schemas · custom CLIs · OpenAPI-generated typed SDKs · scoped permissions · audit trails<br>
**Models** &nbsp; RAG · fine-tuning on domain data · self-learning loops · evaluation rubrics · local inference on owned GPUs<br>
**Build** &nbsp; TypeScript · Node.js · Rust · iOS, Android and PWA · cloud-agnostic deployment · agentic coding

## Say hello

Alongside the studio I take on a few side roles in applied AI, up to 20 hours a week
and remote, because they are how I keep learning. I work from Bali (UTC+8) and overlap
comfortably with European mornings.

[Get in touch through Factory Zero](https://factory0.ventures/enter/)

<sub>Enjoying the simulation.</sub>
