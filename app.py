import streamlit as st


GITHUB_URL = "https://github.com/GhostDriftTheory/responsibility-os-internal-control-demo"


st.set_page_config(
    page_title="ADIC Internal Control Demo",
    page_icon="R",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
    :root {
        --ink: #202124;
        --muted: #667085;
        --line: #d8dee8;
        --panel: #f7f9fc;
        --blue: #2563eb;
        --blue-bg: #eef4ff;
        --green-bg: #eaf7ef;
        --green-border: #3fa66b;
        --green-text: #17613a;
        --yellow-bg: #fff6dc;
        --yellow-border: #d99b19;
        --yellow-text: #755000;
        --red-bg: #fdecec;
        --red-border: #d94a4a;
        --red-text: #8c1f1f;
    }
    .main .block-container {
        max-width: 1160px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    h1, h2, h3 {
        color: var(--ink);
        letter-spacing: 0;
    }
    .hero {
        border: 1px solid var(--line);
        border-left: 7px solid var(--blue);
        border-radius: 8px;
        padding: 1.45rem 1.55rem;
        background: linear-gradient(90deg, #ffffff 0%, var(--blue-bg) 100%);
        margin-bottom: 1.2rem;
    }
    .eyebrow {
        color: var(--blue);
        font-size: 0.82rem;
        font-weight: 800;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 0.35rem;
    }
    .hero-title {
        color: var(--ink);
        font-size: 2.25rem;
        line-height: 1.05;
        font-weight: 850;
        margin-bottom: 0.45rem;
    }
    .hero-subtitle {
        color: var(--muted);
        font-size: 1.08rem;
        max-width: 820px;
    }
    .spine {
        color: var(--ink);
        font-size: 1.1rem;
        font-weight: 850;
        margin-top: 0.9rem;
    }
    .section-note {
        color: var(--muted);
        margin-top: -0.35rem;
        margin-bottom: 0.8rem;
    }
    .mini-card, .status-card, .case-box, .box, .path-box, .decision-card {
        border-radius: 8px;
    }
    .mini-card {
        border: 1px solid var(--line);
        background: #ffffff;
        padding: 0.95rem 1rem;
        min-height: 118px;
    }
    .mini-title {
        color: var(--ink);
        font-weight: 800;
        margin-bottom: 0.35rem;
    }
    .mini-copy {
        color: var(--muted);
        font-size: 0.93rem;
    }
    .box {
        border: 1px solid var(--line);
        background: var(--panel);
        color: var(--ink);
        padding: 1rem 1.15rem;
        margin: 0.75rem 0;
    }
    .blue-box {
        border-color: var(--blue);
        background: var(--blue-bg);
    }
    .green-box {
        border-color: var(--green-border);
        background: var(--green-bg);
        color: var(--green-text);
    }
    .yellow-box {
        border-color: var(--yellow-border);
        background: var(--yellow-bg);
        color: var(--yellow-text);
    }
    .red-box {
        border-color: var(--red-border);
        background: var(--red-bg);
        color: var(--red-text);
    }
    .path-box {
        border: 1px solid var(--line);
        background: #ffffff;
        padding: 1rem 1.15rem;
        min-height: 370px;
    }
    .path-risk {
        border-top: 5px solid var(--yellow-border);
    }
    .path-responsibility {
        border-top: 5px solid var(--blue);
    }
    .path-title {
        color: var(--ink);
        font-size: 1.05rem;
        font-weight: 850;
        margin-bottom: 0.55rem;
    }
    .path-step {
        border: 1px solid var(--line);
        border-radius: 8px;
        padding: 0.58rem 0.7rem;
        margin-bottom: 0.48rem;
        color: var(--ink);
        background: var(--panel);
    }
    .path-result {
        margin-top: 0.8rem;
        padding: 0.8rem;
        border-radius: 8px;
        font-weight: 750;
    }
    .status-card {
        border: 1px solid var(--green-border);
        background: var(--green-bg);
        padding: 0.9rem;
        min-height: 105px;
    }
    .status-label {
        color: var(--muted);
        font-size: 0.84rem;
        margin-bottom: 0.22rem;
    }
    .status-value {
        color: var(--green-text);
        font-size: 1.15rem;
        font-weight: 800;
    }
    .case-box {
        border: 1px solid var(--line);
        background: #ffffff;
        padding: 1rem 1.15rem;
        min-height: 300px;
    }
    .case-good {
        border-top: 5px solid var(--green-border);
    }
    .case-bad {
        border-top: 5px solid var(--red-border);
    }
    .case-title {
        color: var(--ink);
        font-size: 1.05rem;
        font-weight: 850;
        margin-bottom: 0.55rem;
    }
    .collapse-result {
        text-align: center;
        border: 2px solid var(--line);
        border-radius: 8px;
        background: #ffffff;
        padding: 1rem;
        font-size: 1.25rem;
        font-weight: 850;
        color: var(--ink);
        margin-top: 0.9rem;
    }
    .verdict {
        border-radius: 8px;
        padding: 1.05rem 1.2rem;
        font-size: 1.08rem;
        font-weight: 850;
        margin-top: 0.8rem;
    }
    .pill {
        display: inline-block;
        border: 1px solid var(--line);
        border-radius: 999px;
        padding: 0.22rem 0.55rem;
        margin: 0.14rem;
        background: #ffffff;
        color: var(--muted);
        font-size: 0.82rem;
    }
    .decision-card {
        border: 1px solid var(--line);
        background: #ffffff;
        padding: 1rem 1.15rem;
    }
    .decision-row {
        display: flex;
        justify-content: space-between;
        gap: 1rem;
        border-bottom: 1px solid var(--line);
        padding: 0.65rem 0;
    }
    .decision-row:last-child {
        border-bottom: 0;
    }
    .decision-label {
        color: var(--muted);
        font-weight: 700;
    }
    .decision-value {
        color: var(--ink);
        font-weight: 850;
        text-align: right;
    }
    .footer-link {
        color: var(--blue);
        font-weight: 700;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def html_block(body: str, extra_class: str = "") -> None:
    st.markdown(f'<div class="box {extra_class}">{body}</div>', unsafe_allow_html=True)


def mini_card(title: str, copy: str) -> None:
    st.markdown(
        f"""
        <div class="mini-card">
            <div class="mini-title">{title}</div>
            <div class="mini-copy">{copy}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def path_box(title: str, steps: list[str], result: str, path_class: str, result_class: str) -> None:
    step_html = "".join(f'<div class="path-step">{index}. {step}</div>' for index, step in enumerate(steps, 1))
    st.markdown(
        f"""
        <div class="path-box {path_class}">
            <div class="path-title">{title}</div>
            {step_html}
            <div class="path-result {result_class}">{result}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def status_card(label: str, value: str) -> None:
    st.markdown(
        f"""
        <div class="status-card">
            <div class="status-label">{label}</div>
            <div class="status-value">&check; {value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def decide_gate(checks: dict[str, bool]) -> tuple[str, str, str]:
    missing = [label for label, checked in checks.items() if not checked]
    critical = {
        "Decision maker is named",
        "Receiving party is named",
        "Stop condition is defined",
        "Stop condition was checked at the handoff",
        "Accept or refuse result is recorded",
    }

    if not missing:
        return (
            "PASS",
            "green",
            "The company can treat this as its accountable business action.",
        )
    if any(item in critical for item in missing):
        return (
            "STOP",
            "red",
            "Do not treat this as a company decision yet.",
        )
    return (
        "NEEDS EVIDENCE",
        "yellow",
        "Hold the decision until the missing evidence is added.",
    )


def executive_summary(verdict: str) -> str:
    if verdict == "PASS":
        return (
            "This AI-recommended handoff can be treated as a company action because "
            "the responsible people, checked evidence, stop condition, and handoff "
            "result are preserved."
        )
    if verdict == "STOP":
        return (
            "This AI-recommended handoff was operationally possible, but the company "
            "should not own it as a business decision yet because the handoff condition "
            "was not established."
        )
    return (
        "This AI-recommended handoff needs more evidence before the company can own it "
        "as a business decision."
    )


def management_values(verdict: str) -> tuple[str, str]:
    if verdict == "PASS":
        return "Established", "Treat as a responsible business decision."
    if verdict == "STOP":
        return "Not established", "Do not treat this as a responsible business decision yet."
    return "Needs evidence", "Hold until missing evidence is added."


def management_card(verdict: str) -> None:
    accountability_status, action = management_values(verdict)
    st.markdown(
        f"""
        <div class="decision-card">
            <div class="decision-row">
                <div class="decision-label">Operational status</div>
                <div class="decision-value">Completed</div>
            </div>
            <div class="decision-row">
                <div class="decision-label">Governance status</div>
                <div class="decision-value">Approved</div>
            </div>
            <div class="decision-row">
                <div class="decision-label">Accountability status</div>
                <div class="decision-value">{accountability_status}</div>
            </div>
            <div class="decision-row">
                <div class="decision-label">Management action</div>
                <div class="decision-value">{action}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


with st.sidebar:
    st.markdown("### Responsibility OS")
    st.markdown("A simple demo for one question:")
    st.markdown("**Can the company own this AI-assisted decision?**")
    st.markdown(f"[GitHub repository]({GITHUB_URL})")
    st.divider()
    st.markdown("**What this is**")
    st.markdown("An upstream gate before risk management begins.")
    st.markdown("**What this is not**")
    st.markdown("- Not a Lean UI\n- Not a math demo\n- Not a risk scoring app")


st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">Responsibility OS / ADIC</div>
        <div class="hero-title">Can the company own this decision?</div>
        <div class="hero-subtitle">
            This demo shows why a green governance dashboard can still leave a company
            unable to accept an AI-assisted decision as its own business action.
        </div>
        <div class="spine">
            Before managing the risk of a decision, a company must know whether it can own the decision.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.header("The Priority Shift")
st.markdown(
    '<div class="section-note">The problem is not risk management. The problem is asking the risk question too early.</div>',
    unsafe_allow_html=True,
)
left, right = st.columns(2)
with left:
    path_box(
        "Current governance priority",
        [
            "What risk class is this AI or system?",
            "Was it approved?",
            "Are logs available?",
            "Did the operation complete?",
        ],
        "Result: The dashboard looks green, but the company may still be unable to own the decision.",
        "path-risk",
        "yellow-box",
    )
with right:
    path_box(
        "Responsibility OS priority",
        [
            "Can the company own this decision?",
            "Who accepted responsibility?",
            "What evidence was attached to the decision?",
            "What condition would have stopped it?",
            "Only then: classify and manage the remaining risk.",
        ],
        "Result: Risk management starts after the decision becomes accountable.",
        "path-responsibility",
        "green-box",
    )

html_block(
    """
    <strong>Key point:</strong> Risk classification is useful. It is just the wrong
    first question if the company does not yet know whether the decision can become
    its accountable action.
    """,
    "blue-box",
)

top_cols = st.columns(4)
with top_cols[0]:
    mini_card("First question", "Can we own this decision as a company?")
with top_cols[1]:
    mini_card("Green is not enough", "Done, approved, and logged does not always mean accountable.")
with top_cols[2]:
    mini_card("ADIC is upstream", "It decides whether risk management can meaningfully begin.")
with top_cols[3]:
    mini_card("Simple output", "Pass, stop, or add evidence before the company owns the action.")

st.header("Scenario")
html_block(
    """
    <strong>Cold-chain logistics handoff.</strong><br>
    An AI optimization system recommends transferring refrigerated goods at
    Warehouse A because it improves delivery time, cost, and inventory efficiency.
    """
)

st.header("Current Governance View")
st.markdown(
    '<div class="section-note">Everything below looks green in a normal governance dashboard.</div>',
    unsafe_allow_html=True,
)
card_cols = st.columns(5)
with card_cols[0]:
    status_card("Risk class", "Medium")
with card_cols[1]:
    status_card("Approval", "Approved")
with card_cols[2]:
    status_card("Temperature log", "Available")
with card_cols[3]:
    status_card("Delivery", "Completed")
with card_cols[4]:
    status_card("Audit log", "Available")

html_block(
    """
    <strong>What this proves:</strong> the process happened.<br>
    <strong>What it does not prove:</strong> the company can accept the decision as
    its own business action.
    """,
    "yellow-box",
)

html_block(
    """
    <strong>Can the company answer these questions?</strong>
    <ul>
        <li>Who accepted responsibility at the handoff?</li>
        <li>What exactly was checked before accepting the goods?</li>
        <li>What condition should have stopped the handoff?</li>
        <li>Can shipping, QA, legal, and management read the same explanation later?</li>
    </ul>
    <strong>Current result:</strong> The work is completed, but the company cannot
    yet own the decision.
    """,
    "red-box",
)

st.header("Collapse Demo")
st.markdown(
    '<div class="section-note">Two different responsibility stories can look like the same business result.</div>',
    unsafe_allow_html=True,
)
left, right = st.columns(2)
with left:
    st.markdown(
        """
        <div class="case-box case-good">
            <div class="case-title">Case A: Accountable handoff</div>
            <ul>
                <li>Carrier presents temperature evidence</li>
                <li>Warehouse checks it</li>
                <li>Stop condition is checked</li>
                <li>Warehouse accepts the handoff</li>
                <li>Responsibility moves without a gap</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
with right:
    st.markdown(
        """
        <div class="case-box case-bad">
            <div class="case-title">Case B: Non-accountable handoff</div>
            <ul>
                <li>AI recommends transfer</li>
                <li>Temperature data exists somewhere</li>
                <li>Warehouse receives the goods</li>
                <li>No clear acceptance condition is recorded</li>
                <li>Stop condition was not checked at the handoff</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="collapse-result">Both appear as: Delivery completed</div>',
    unsafe_allow_html=True,
)
html_block(
    "<strong>Same visible result. Different accountability status. This is the internal control failure.</strong>",
    "red-box",
)

st.header("Can This Become A Company Action?")
st.markdown(
    '<div class="section-note">This is not a checklist for extra paperwork. It is a pass-or-stop gate before the company owns the decision.</div>',
    unsafe_allow_html=True,
)

items = [
    "Decision maker is named",
    "Receiving party is named",
    "Evidence checked at the handoff is recorded",
    "Stop condition is defined",
    "Stop condition was checked at the handoff",
    "Accept or refuse result is recorded",
    "Same explanation can be read later by shipping, QA, legal, and management",
]

defaults = {
    "Decision maker is named": True,
    "Receiving party is named": True,
    "Evidence checked at the handoff is recorded": False,
    "Stop condition is defined": False,
    "Stop condition was checked at the handoff": False,
    "Accept or refuse result is recorded": False,
    "Same explanation can be read later by shipping, QA, legal, and management": False,
}

check_cols = st.columns(2)
checks: dict[str, bool] = {}
for index, item in enumerate(items):
    with check_cols[index % 2]:
        checks[item] = st.checkbox(item, value=defaults[item])

score = sum(1 for checked in checks.values() if checked)
st.progress(score / len(items), text=f"{score} of {len(items)} ownership conditions preserved")

verdict, color, message = decide_gate(checks)
html_block(f"<strong>{verdict}:</strong> {message}", f"{color}-box verdict")

missing_items = [item for item, checked in checks.items() if not checked]
if missing_items:
    st.markdown("**Missing proof before the company can own the decision**")
    st.markdown(
        " ".join(f'<span class="pill">{item}</span>' for item in missing_items),
        unsafe_allow_html=True,
    )

st.header("Management Decision Output")
management_card(verdict)

st.header("Executive Summary")
html_block(executive_summary(verdict), f"{color}-box")

st.header("ADIC Is Not Risk Management")
left, right = st.columns(2)
with left:
    html_block(
        """
        <strong>Risk management asks:</strong><br>
        What could go wrong after we act?
        """,
        "yellow-box",
    )
with right:
    html_block(
        """
        <strong>ADIC asks:</strong><br>
        Can this decision become our accountable business action in the first place?
        """,
        "blue-box",
    )

html_block(
    """
    ADIC is not an extra control after risk classification. It is the upstream
    internal control gate that decides whether risk classification and risk
    management can meaningfully begin.
    """
)

st.markdown(
    f'<a class="footer-link" href="{GITHUB_URL}" target="_blank">View project on GitHub</a>',
    unsafe_allow_html=True,
)
