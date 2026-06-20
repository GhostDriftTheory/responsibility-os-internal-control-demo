# Responsibility OS Internal Control Demo

Streamlit demo for one simple question:

**Can the company own this AI-assisted decision?**

Repository:
[GhostDriftTheory/responsibility-os-internal-control-demo](https://github.com/GhostDriftTheory/responsibility-os-internal-control-demo)

## Core Message

Before managing the risk of a decision, a company must know whether it can own the decision.

Risk classification, approval, and logs are useful. They can show that a process happened. They do not always show that the company can accept the decision as its own business action.

## The Priority Shift

Current governance often starts with:

1. What risk class is this AI or system?
2. Was it approved?
3. Are logs available?
4. Did the operation complete?

Responsibility OS / ADIC starts with:

1. Can the company own this decision?
2. Who accepted responsibility?
3. What evidence was attached to the decision?
4. What condition would have stopped it?
5. Only then: classify and manage the remaining risk.

The problem is not that risk classification is useless. The problem is that risk classification is being asked before the company knows whether the decision can become its accountable action.

## What The Demo Shows

- A normal governance dashboard can look green.
- The work can be completed, approved, and logged.
- The company may still be unable to say who accepted responsibility, what was checked, or what should have stopped the handoff.
- ADIC acts as an upstream gate before risk management meaningfully begins.

## Management Output

The app turns the scenario into a plain management card:

- Operational status
- Governance status
- Accountability status
- Management action

This is the point of the demo: ADIC is not a paperwork checklist. It is a pass-or-stop gate for deciding whether an AI-assisted decision can become a company action.

## What This Is Not

- Not a Lean demo.
- Not a math demo.
- Not a risk scoring app.
- Not an academic UI.

The Lean background is only conceptual: if the evidence and responsibility layer is forgotten, different responsibility stories can look like the same business result.

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Community Cloud

Use these settings when deploying:

- Repository: `GhostDriftTheory/responsibility-os-internal-control-demo`
- Branch: `main`
- Main file path: `app.py`
- Python dependencies: `requirements.txt`

After deployment, add the public Streamlit URL near the top of this README.

## App Flow

1. Priority shift: risk-first governance vs responsibility-first control.
2. Scenario: cold-chain logistics handoff.
3. Current governance view: risk class, approval, logs, and completion all appear green.
4. Control gap: the company still cannot own the decision.
5. Collapse demo: accountable and non-accountable handoffs both appear as `Delivery completed`.
6. Company action gate: check whether the decision can pass, must stop, or needs evidence.
7. Management output: clear business action for leaders.

## File Structure

```text
.
|-- app.py
|-- requirements.txt
|-- README.md
`-- .streamlit/
    `-- config.toml
```
