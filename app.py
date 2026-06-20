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
    .box, .path-box, .status-card, .inspection-panel, .node, .decision-card {
        border-radius: 8px;
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
        min-height: 285px;
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
        min-height: 100px;
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
    .inspection-panel {
        border: 1px solid var(--line);
        background: #ffffff;
        padding: 1.1rem;
        min-height: 600px;
    }
    .panel-title {
        color: var(--ink);
        font-size: 1.08rem;
        font-weight: 850;
        margin-bottom: 0.65rem;
    }
    .green-strip {
        border-top: 5px solid var(--green-border);
    }
    .red-strip {
        border-top: 5px solid var(--red-border);
    }
    .dashboard-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        border: 1px solid var(--green-border);
        background: var(--green-bg);
        color: var(--green-text);
        border-radius: 8px;
        padding: 0.76rem 0.85rem;
        margin-bottom: 0.55rem;
        font-weight: 800;
    }
    .looks-ok {
        text-align: center;
        border: 1px solid var(--yellow-border);
        background: var(--yellow-bg);
        color: var(--yellow-text);
        border-radius: 8px;
        padding: 0.9rem;
        margin-top: 1rem;
        font-weight: 850;
    }
    .node {
        border: 1px solid var(--green-border);
        background: var(--green-bg);
        color: var(--green-text);
        padding: 0.8rem 0.9rem;
    }
    .node-broken {
        border: 2px solid var(--red-border);
        background: var(--red-bg);
        color: var(--red-text);
        box-shadow: 0 0 0 4px rgba(217, 74, 74, 0.08);
    }
    .node-title {
        font-weight: 850;
        color: var(--ink);
        margin-bottom: 0.25rem;
    }
    .node-broken .node-title {
        color: var(--red-text);
    }
    .node-copy {
        font-size: 0.93rem;
    }
    .arrow {
        text-align: center;
        color: var(--muted);
        font-weight: 850;
        font-size: 1.35rem;
        line-height: 1.45;
    }
    .break-label {
        border: 1px solid var(--red-border);
        background: #ffffff;
        color: var(--red-text);
        border-radius: 8px;
        padding: 0.7rem 0.85rem;
        font-weight: 800;
        margin: 0.55rem 0;
    }
    .stop-card {
        border: 2px solid var(--red-border);
        background: var(--red-bg);
        color: var(--red-text);
        border-radius: 8px;
        padding: 1.2rem;
        text-align: center;
        margin: 1rem 0;
    }
    .stop-title {
        font-size: 1.7rem;
        font-weight: 900;
        margin-bottom: 0.3rem;
    }
    .stop-copy {
        font-weight: 800;
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
    .decision-value-red {
        color: var(--red-text);
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


def dashboard_item(label: str) -> None:
    st.markdown(
        f'<div class="dashboard-item"><span>{label}</span><span>OK</span></div>',
        unsafe_allow_html=True,
    )


def inspection_node(title: str, copy: str, broken: bool = False) -> None:
    klass = "node node-broken" if broken else "node"
    st.markdown(
        f"""
        <div class="{klass}">
            <div class="node-title">{title}</div>
            <div class="node-copy">{copy}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def arrow() -> None:
    st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)


def conventional_panel() -> None:
    items = ["リスク分類", "承認", "温度ログ", "監査ログ", "配送完了"]
    item_html = "".join(
        f'<div class="dashboard-item"><span>{item}</span><span>OK</span></div>'
        for item in items
    )
    st.markdown(
        f"""
        <div class="inspection-panel green-strip">
            <div class="panel-title">従来管理</div>
            {item_html}
            <div class="looks-ok">一見、本番運用できそう</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def adic_inspection_panel() -> None:
    st.markdown(
        """
        <div class="inspection-panel red-strip">
            <div class="panel-title">ADIC / 責任OSの検査</div>
            <div class="node">
                <div class="node-title">荷主</div>
                <div class="node-copy">何を渡すかが決まっている</div>
            </div>
            <div class="arrow">↓</div>
            <div class="node">
                <div class="node-title">配送会社</div>
                <div class="node-copy">温度証拠を渡す相手とタイミングが決まっている</div>
            </div>
            <div class="arrow">↓</div>
            <div class="node node-broken">
                <div class="node-title">中継倉庫</div>
                <div class="node-copy">受け入れ条件と停止条件が、責任の移り方に結びついていない</div>
            </div>
            <div class="break-label">
                ここで切れる: 誰が、どの条件で責任を受け取ったかを後から説明できない
            </div>
            <div class="arrow">↓</div>
            <div class="node node-broken">
                <div class="node-title">納品先</div>
                <div class="node-copy">前の受け渡しが切れているため、正式運用の検査を先に進めない</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def management_card() -> None:
    st.markdown(
        """
        <div class="decision-card">
            <div class="decision-row">
                <div class="decision-label">業務フロー案</div>
                <div class="decision-value">作成済み</div>
            </div>
            <div class="decision-row">
                <div class="decision-label">リスク分類</div>
                <div class="decision-value">実施済み</div>
            </div>
            <div class="decision-row">
                <div class="decision-label">ログ設計</div>
                <div class="decision-value">あり</div>
            </div>
            <div class="decision-row">
                <div class="decision-label">正式運用してよいか</div>
                <div class="decision-value decision-value-red">不可</div>
            </div>
            <div class="decision-row">
                <div class="decision-label">経営としての対応</div>
                <div class="decision-value">本番運用に入れず、中継倉庫の責任条件を直す。</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


with st.sidebar:
    st.markdown("### Responsibility OS")
    st.markdown("このデモで見る問いは1つです。")
    st.markdown("**その仕組み、本番運用に入れてよいですか？**")
    st.markdown(f"[GitHub repository]({GITHUB_URL})")
    st.divider()
    st.markdown("**これは何か**")
    st.markdown("業務フローを順にたどり、責任のつながりが切れる場所を見つける検査です。")
    st.markdown("**これは何ではないか**")
    st.markdown("- Leanの画面ではありません\n- 数学の説明ではありません\n- リスク点数を出すアプリではありません")


st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">Responsibility OS / ADIC</div>
        <div class="hero-title">その仕組み、本番運用に入れてよいですか？</div>
        <div class="hero-subtitle">
            リスク分類・承認・ログ設計がそろっていても、
            会社の正式な業務として運用してよいとは限りません。
        </div>
        <div class="spine">
            ADIC / 責任OSは、業務フローを順にたどり、責任のつながりが切れる場所を検査します。
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.header("見る順番を変える")
left, right = st.columns(2)
with left:
    path_box(
        "よくある順番",
        [
            "このシステムのリスクは何か",
            "承認されたか",
            "ログは取れるか",
            "運用開始できるか",
        ],
        "本番運用できそうに見える。でも、責任のつながりはまだ見えていない。",
        "path-risk",
        "yellow-box",
    )
with right:
    path_box(
        "ADIC / 責任OSの順番",
        [
            "業務フローを順にたどる",
            "誰が何を渡すかを見る",
            "何を確認して渡すかを見る",
            "どこで止められるかを見る",
            "責任が切れた場所で止める",
        ],
        "正式運用に耐える仕組みかを先に見る。",
        "path-responsibility",
        "green-box",
    )

st.header("シナリオ")
html_block(
    """
    <strong>冷蔵品の受け渡し業務。</strong><br>
    会社は、冷蔵品の受け渡しに新しい自動化フローを入れようとしています。
    この仕組みでは、配送時間・コスト・在庫効率をよくするため、
    倉庫Aでの受け渡しを標準フローに組み込みます。
    """
)

st.header("従来の管理画面は全部グリーン")
st.markdown(
    '<div class="section-note">ここだけ見ると、本番運用できそうに見えます。</div>',
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
    status_card("監査ログ", "あり")
with card_cols[4]:
    status_card("配送", "完了")

st.header("ADIC / 責任OSの検査結果")
st.markdown(
    '<div class="section-note">説明ではなく、検査結果として見せます。切れる場所は1か所だけです。</div>',
    unsafe_allow_html=True,
)

left, right = st.columns([0.92, 1.08])
with left:
    conventional_panel()

with right:
    adic_inspection_panel()

st.markdown(
    """
    <div class="stop-card">
        <div class="stop-title">STOP</div>
        <div class="stop-copy">
            責任のつながりが中継倉庫で切れているため、この仕組みは本番運用に入れてはいけません。
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

html_block(
    """
    <strong>ADIC / 責任OSが見ていること:</strong><br>
    ログがあるかではありません。受け渡しごとに、
    誰が何を受け取り、何を確認し、どこで止められるかを順にたどります。
    つながりが切れる場所があれば、管理画面が全部緑でも本番運用には入れません。
    """,
    "blue-box",
)

st.header("経営向けの出力")
management_card()

st.header("ADICはリスク管理ではない")
left, right = st.columns(2)
with left:
    html_block(
        """
        <strong>リスク管理が聞くこと:</strong><br>
        この仕組みを運用したあと、何が悪くなり得るか。
        """,
        "yellow-box",
    )
with right:
    html_block(
        """
        <strong>ADICが聞くこと:</strong><br>
        そもそも、この仕組みを会社の正式運用にしてよいか。
        """,
        "blue-box",
    )

html_block(
    """
    小さな補足: これは形式検証の考え方を、業務向けに見せたものです。
    難しい数式ではなく、業務フローを順にたどり、切れ目を見つける検査として使います。
    """
)

st.markdown(
    f'<a class="footer-link" href="{GITHUB_URL}" target="_blank">View project on GitHub</a>',
    unsafe_allow_html=True,
)
