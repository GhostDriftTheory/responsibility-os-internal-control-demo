import streamlit as st


GITHUB_URL = "https://github.com/GhostDriftTheory/responsibility-os-internal-control-demo"


st.set_page_config(
    page_title="ADIC 内部統制デモ",
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
        font-size: 2.2rem;
        line-height: 1.12;
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
        "判断した人がわかる",
        "受け入れた側がわかる",
        "止める条件が決まっている",
        "受け渡し時に止める条件を見た",
        "受け入れたか断ったかが残っている",
    }

    if not missing:
        return (
            "PASS",
            "green",
            "会社の判断として通してよい状態です。",
        )
    if any(item in critical for item in missing):
        return (
            "STOP",
            "red",
            "まだ会社の判断として扱ってはいけません。",
        )
    return (
        "NEEDS EVIDENCE",
        "yellow",
        "足りない証拠を足してから判断してください。",
    )


def executive_summary(verdict: str) -> str:
    if verdict == "PASS":
        return (
            "このAIの提案による受け渡しは、会社の判断として扱えます。"
            "誰が関わり、何を見て、どの条件なら止めるべきだったか、"
            "そして受け入れ結果が残っているためです。"
        )
    if verdict == "STOP":
        return (
            "このAIの提案による受け渡しは、作業としては可能でした。"
            "しかし、受け渡しの条件がはっきり残っていないため、"
            "まだ会社の判断として扱うべきではありません。"
        )
    return (
        "このAIの提案による受け渡しは、会社の判断として扱う前に、"
        "足りない証拠を追加する必要があります。"
    )


def management_values(verdict: str) -> tuple[str, str]:
    if verdict == "PASS":
        return "成立", "会社の判断として扱う。"
    if verdict == "STOP":
        return "未成立", "まだ会社の判断として扱わない。"
    return "証拠不足", "足りない証拠を足すまで保留する。"


def management_card(verdict: str) -> None:
    accountability_status, action = management_values(verdict)
    st.markdown(
        f"""
        <div class="decision-card">
            <div class="decision-row">
                <div class="decision-label">作業の状態</div>
                <div class="decision-value">完了</div>
            </div>
            <div class="decision-row">
                <div class="decision-label">承認の状態</div>
                <div class="decision-value">承認済み</div>
            </div>
            <div class="decision-row">
                <div class="decision-label">会社が引き受けられるか</div>
                <div class="decision-value">{accountability_status}</div>
            </div>
            <div class="decision-row">
                <div class="decision-label">経営としての対応</div>
                <div class="decision-value">{action}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


with st.sidebar:
    st.markdown("### Responsibility OS")
    st.markdown("このデモで見る問いは1つです。")
    st.markdown("**会社として、この判断を引き受けてよいか？**")
    st.markdown(f"[GitHub repository]({GITHUB_URL})")
    st.divider()
    st.markdown("**これは何か**")
    st.markdown("リスク管理の前に置く、会社の判断として通せるかを見る入口です。")
    st.markdown("**これは何ではないか**")
    st.markdown("- Leanの画面ではありません\n- 数学の説明ではありません\n- リスク点数を出すアプリではありません")


st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">Responsibility OS / ADIC</div>
        <div class="hero-title">会社として、この判断を引き受けてよいか？</div>
        <div class="hero-subtitle">
            このデモは、画面が全部「緑」でも、会社がAIの提案を
            自分たちの判断として受け止められないことがある、という話です。
        </div>
        <div class="spine">
            判断のリスクを見る前に、会社がその判断を引き受けられるかを見る。
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.header("見る順番を変える")
st.markdown(
    '<div class="section-note">問題はリスク管理そのものではありません。リスクを最初に聞いてしまう順番です。</div>',
    unsafe_allow_html=True,
)
left, right = st.columns(2)
with left:
    path_box(
        "よくある順番",
        [
            "このAIやシステムのリスクは何か",
            "承認されたか",
            "ログはあるか",
            "作業は終わったか",
        ],
        "結果: 画面は緑。でも、会社がその判断を引き受けられるとは限らない。",
        "path-risk",
        "yellow-box",
    )
with right:
    path_box(
        "ADICの順番",
        [
            "会社としてこの判断を引き受けてよいか",
            "誰が受け入れたか",
            "何を見て判断したか",
            "どんな時なら止めるべきだったか",
            "その後で、残るリスクを分類して管理する",
        ],
        "結果: 会社が引き受けられる状態になってから、リスク管理が始まる。",
        "path-responsibility",
        "green-box",
    )

html_block(
    """
    <strong>大事な点:</strong> リスク分類は役に立ちます。
    ただし、会社がその判断を引き受けられるかが分からないうちに、
    最初の問いにしてしまうと順番が違います。
    """,
    "blue-box",
)

top_cols = st.columns(4)
with top_cols[0]:
    mini_card("最初の問い", "会社として、この判断を引き受けてよいか。")
with top_cols[1]:
    mini_card("緑でも足りない", "完了、承認、ログあり。でも引き受けられるとは限りません。")
with top_cols[2]:
    mini_card("ADICは前段", "リスク管理を始めてよいかを見る入口です。")
with top_cols[3]:
    mini_card("出力はシンプル", "通す、止める、証拠を足す。この3つです。")

st.header("シナリオ")
html_block(
    """
    <strong>冷蔵品の受け渡し。</strong><br>
    AIが、配送時間・コスト・在庫効率をよくするために、
    冷蔵品を倉庫Aで受け渡すことを提案しました。
    """
)

st.header("今の管理画面ではこう見える")
st.markdown(
    '<div class="section-note">ふつうの管理画面では、下の項目はすべて緑に見えます。</div>',
    unsafe_allow_html=True,
)
card_cols = st.columns(5)
with card_cols[0]:
    status_card("リスク分類", "中")
with card_cols[1]:
    status_card("承認", "済み")
with card_cols[2]:
    status_card("温度ログ", "あり")
with card_cols[3]:
    status_card("配送", "完了")
with card_cols[4]:
    status_card("監査ログ", "あり")

html_block(
    """
    <strong>これで分かること:</strong> 作業が行われたこと。<br>
    <strong>まだ分からないこと:</strong> 会社がその判断を自分たちの判断として
    引き受けてよいか。
    """,
    "yellow-box",
)

html_block(
    """
    <strong>会社はこの質問に答えられますか？</strong>
    <ul>
        <li>誰が受け渡しの責任を引き受けたか。</li>
        <li>受け入れる前に、何を確認したか。</li>
        <li>どんな状態なら止めるべきだったか。</li>
        <li>出荷、品質、法務、経営があとで同じ説明を読めるか。</li>
    </ul>
    <strong>今の結果:</strong> 作業は終わっています。でも、会社の判断としては
    まだ引き受けられません。
    """,
    "red-box",
)

st.header("同じ結果に見えてしまう例")
st.markdown(
    '<div class="section-note">責任の流れが違っても、画面上は同じ結果に見えることがあります。</div>',
    unsafe_allow_html=True,
)
left, right = st.columns(2)
with left:
    st.markdown(
        """
        <div class="case-box case-good">
            <div class="case-title">ケースA: 引き受けられる受け渡し</div>
            <ul>
                <li>運送会社が温度の証拠を出す</li>
                <li>倉庫がそれを確認する</li>
                <li>止める条件を確認する</li>
                <li>倉庫が受け入れる</li>
                <li>責任が空白なく移る</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
with right:
    st.markdown(
        """
        <div class="case-box case-bad">
            <div class="case-title">ケースB: 引き受けられない受け渡し</div>
            <ul>
                <li>AIが受け渡しを提案する</li>
                <li>温度データはどこかにある</li>
                <li>倉庫が品物を受け取る</li>
                <li>受け入れ条件がはっきり残っていない</li>
                <li>その場で止める条件を確認していない</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="collapse-result">どちらも画面上は「配送完了」に見える</div>',
    unsafe_allow_html=True,
)
html_block(
    "<strong>見える結果は同じ。でも、会社が引き受けられるかは違います。ここが内部統制の失敗点です。</strong>",
    "red-box",
)

st.header("会社の判断として通してよいか")
st.markdown(
    '<div class="section-note">これは書類を増やすチェックリストではありません。会社がその判断を引き受ける前の、通すか止めるかの判定です。</div>',
    unsafe_allow_html=True,
)

items = [
    "判断した人がわかる",
    "受け入れた側がわかる",
    "受け渡し時に見た証拠が残っている",
    "止める条件が決まっている",
    "受け渡し時に止める条件を見た",
    "受け入れたか断ったかが残っている",
    "出荷、品質、法務、経営があとで同じ説明を読める",
]

defaults = {
    "判断した人がわかる": True,
    "受け入れた側がわかる": True,
    "受け渡し時に見た証拠が残っている": False,
    "止める条件が決まっている": False,
    "受け渡し時に止める条件を見た": False,
    "受け入れたか断ったかが残っている": False,
    "出荷、品質、法務、経営があとで同じ説明を読める": False,
}

check_cols = st.columns(2)
checks: dict[str, bool] = {}
for index, item in enumerate(items):
    with check_cols[index % 2]:
        checks[item] = st.checkbox(item, value=defaults[item])

score = sum(1 for checked in checks.values() if checked)
st.progress(score / len(items), text=f"{score} / {len(items)} 個の条件がそろっています")

verdict, color, message = decide_gate(checks)
html_block(f"<strong>{verdict}:</strong> {message}", f"{color}-box verdict")

missing_items = [item for item, checked in checks.items() if not checked]
if missing_items:
    st.markdown("**会社が引き受ける前に足りないもの**")
    st.markdown(
        " ".join(f'<span class="pill">{item}</span>' for item in missing_items),
        unsafe_allow_html=True,
    )

st.header("経営向けの出力")
management_card(verdict)

st.header("短い説明")
html_block(executive_summary(verdict), f"{color}-box")

st.header("ADICはリスク管理ではない")
left, right = st.columns(2)
with left:
    html_block(
        """
        <strong>リスク管理が聞くこと:</strong><br>
        実行したあと、何が悪くなり得るか。
        """,
        "yellow-box",
    )
with right:
    html_block(
        """
        <strong>ADICが聞くこと:</strong><br>
        そもそも、この判断を会社の判断として引き受けてよいか。
        """,
        "blue-box",
    )

html_block(
    """
    ADICは、リスク分類のあとに足す管理ではありません。
    リスク分類やリスク管理を始めてよいかを先に見る、内部統制の入口です。
    """
)

st.markdown(
    f'<a class="footer-link" href="{GITHUB_URL}" target="_blank">View project on GitHub</a>',
    unsafe_allow_html=True,
)
