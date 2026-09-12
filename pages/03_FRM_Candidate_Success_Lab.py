import math
from datetime import date, timedelta

import pandas as pd
import streamlit as st

st.set_page_config(page_title="FRM Candidate Success Lab", page_icon="🎯", layout="wide")

st.markdown(
    """
    <style>
    .main .block-container {max-width: 1180px; padding-top: 1.4rem;}
    .hero {padding: 1.35rem 1.5rem; border-radius: 18px; background: linear-gradient(135deg,#101828,#344054); color:white; margin-bottom:1rem;}
    .hero h1 {margin:0 0 .35rem 0; font-size:2.2rem;}
    .hero p {margin:.2rem 0; color:#EAECF0;}
    .good {padding:.75rem 1rem; border-radius:12px; background:#ECFDF3; border:1px solid #ABEFC6;}
    .warn {padding:.75rem 1rem; border-radius:12px; background:#FFFAEB; border:1px solid #FEDF89;}
    .risk {padding:.75rem 1rem; border-radius:12px; background:#FEF3F2; border:1px solid #FECDCA;}
    .ip {padding:1rem; border-radius:14px; background:#F9FAFB; border:1px solid #D0D5DD;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
      <h1>🎯 FRM Candidate Success Lab</h1>
      <p>An independent study-process diagnostic for candidates who want to improve the way they prepare, revise, practise and manage exam time.</p>
      <p><b>Not a question bank.</b> No copied exam questions, provider content, logos, textbook pages or proprietary curriculum text are used here.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption(
    "FRM® is a registered trademark of the Global Association of Risk Professionals (GARP). "
    "This independent educational tool is not affiliated with, endorsed by, or sponsored by GARP."
)

MARKET_FACTS = {
    "Part I pass rate": "47% (Nov 2025)",
    "Part II pass rate": "50% (Nov 2025)",
    "Certified professionals": "100,000+",
    "Countries / regions": "190+",
}

THEMES = [
    {
        "theme": "Starting too late or studying inconsistently",
        "evidence": "Recurring candidate reports + learning science",
        "why": "Large syllabi punish stop-start preparation. Cramming also reduces the benefit of spaced retrieval.",
        "solution": "Use a weekly minimum-hours floor, fixed study blocks, and a catch-up rule before backlog becomes unmanageable.",
    },
    {
        "theme": "Too much passive reading; too little retrieval",
        "evidence": "Strong learning-science evidence",
        "why": "Rereading can feel fluent without proving that knowledge can be recalled and applied under pressure.",
        "solution": "Convert every study block into recall, explanation, calculation, mixed practice, or an error-repair activity.",
    },
    {
        "theme": "Mocks and timed practice begin too late",
        "evidence": "Recurring candidate reports",
        "why": "Candidates may know concepts but discover pacing, stamina and application problems only in the final week.",
        "solution": "Introduce timed sets early; reserve a substantial final phase for mixed sets, mocks and review of errors.",
    },
    {
        "theme": "Repeating the same question bank creates false confidence",
        "evidence": "Recurring candidate reports",
        "why": "Recognition of familiar questions can masquerade as mastery.",
        "solution": "Track first-attempt performance, explain the reason for every error, and use fresh/mixed practice where legally available.",
    },
    {
        "theme": "Weak error analysis",
        "evidence": "Candidate reports + self-regulated learning principles",
        "why": "A score alone does not reveal whether the problem was concept, formula, reading, calculation, judgement or time.",
        "solution": "Maintain an error log with cause, fix, retest date and evidence that the weakness is actually closed.",
    },
    {
        "theme": "Exam-time pacing and decision rules are not trained",
        "evidence": "Exam format + candidate reports",
        "why": "A difficult item can consume the time needed for several easier items.",
        "solution": "Practise a skip/return rule, checkpoints and a final review reserve under realistic timed conditions.",
    },
    {
        "theme": "Rushing into a retake without diagnosing the prior attempt",
        "evidence": "Recurring retaker reports",
        "why": "More of the same method can reproduce the same result, especially when the retake window is short.",
        "solution": "Complete a post-attempt diagnosis first; change the process before changing only the number of study hours.",
    },
    {
        "theme": "Fatigue, stress and test anxiety",
        "evidence": "Academic meta-analyses + candidate reports",
        "why": "Stress can undermine preparation quality and, in some studies, performance; fatigue also reduces disciplined practice.",
        "solution": "Protect sleep, simulate the exam, reduce uncertainty with routines, and treat anxiety as a preparation variable—not the whole explanation.",
    },
]

SOURCE_ROWS = [
    ["GARP", "FRM exam information and pass rates", "Official program facts", "https://www.garp.org/frm/program-exams"],
    ["GARP", "FRM certification overview", "Scale: 100,000+ certified, 190+ countries/regions", "https://www.garp.org/frm"],
    ["GARP", "FRM study materials", "Official practice resources and EPP ecosystem", "https://www.garp.org/frm/study-materials"],
    ["GARP", "Terms of Use", "Copyright, trademarks and restrictions on automated/AI use of site content", "https://www.garp.org/terms-of-use"],
    ["Frontiers in Psychology (2026)", "Time management meta-analysis", "Time management and student learning outcomes", "https://doi.org/10.3389/fpsyg.2026.1700298"],
    ["Learning and Instruction (2022)", "Spacing study", "Spaced retrieval practice predicted higher course performance", "https://doi.org/10.1016/j.learninstruc.2021.101538"],
    ["Psychological Science in the Public Interest (2013)", "Effective learning techniques", "Practice testing and distributed practice rated high utility", "https://doi.org/10.1177/1529100612453266"],
    ["PubMed / Journal of Affective Disorders", "Test anxiety meta-analysis", "Test anxiety negatively associated with educational performance outcomes", "https://pubmed.ncbi.nlm.nih.gov/29156362/"],
    ["PLOS ONE (2021)", "Time management meta-analysis", "Time management associated with academic achievement and wellbeing", "https://doi.org/10.1371/journal.pone.0245066"],
    ["Reddit r/FRM (2026)", "Failed Part I discussion", "Candidate-reported late mock practice", "https://www.reddit.com/r/FRM/comments/1ufywxw/"],
    ["Reddit r/FRM (2026)", "Failed Part II twice discussion", "Candidate-reported limits of repeating one q-bank", "https://www.reddit.com/r/FRM/comments/1upno5s/"],
    ["Reddit r/FRM (2026)", "Passed Part II on third attempt", "Candidate-reported rushed retake and later reorganization", "https://www.reddit.com/r/FRM/comments/1w3eb2b/"],
]


def clamp(x, lo=0, hi=100):
    return max(lo, min(hi, x))


def score_band(score):
    if score >= 80:
        return "Strong", "good"
    if score >= 65:
        return "Workable", "warn"
    return "High risk", "risk"


def build_recommendations(scores, attempts, mock_count, passive_pct, timed_sessions, error_log, weeks):
    recs = []
    for name, score in sorted(scores.items(), key=lambda kv: kv[1])[:3]:
        if name == "Consistency":
            recs.append("Set a non-negotiable weekly study floor and use fixed calendar blocks. Track completed hours, not intended hours.")
        elif name == "Active learning":
            recs.append("Reduce passive reading. Finish each session with closed-book recall, self-explanation, calculations or mixed practice.")
        elif name == "Practice":
            recs.append("Start timed question sets now. Build from short sets to full-length simulations; analyse every miss before adding more volume.")
        elif name == "Error repair":
            recs.append("Create an error log: category → root cause → corrected rule → retest date → closed/open status.")
        elif name == "Pacing":
            recs.append("Train checkpoints and a skip/return rule. A single stubborn question must not consume the time budget of several others.")
        elif name == "Readiness":
            recs.append("Use full simulations to calibrate readiness. Do not rely on familiarity with repeated questions as proof of mastery.")
        elif name == "Recovery":
            recs.append("Protect sleep and recovery, and rehearse exam conditions so the day itself feels routine rather than novel.")
    if attempts >= 2:
        recs.append("As a repeat candidate, do a post-mortem before adding hours: identify what changed between attempts and what must change this time.")
    if mock_count < 2 and weeks <= 6:
        recs.append("Your mock exposure is low for the remaining time. Put a full simulation on the calendar soon, then spend equal effort reviewing it.")
    if passive_pct > 55:
        recs.append("More than half of your study is passive. Move toward an active-heavy mix: recall, practice, explanation and error repair.")
    if timed_sessions == 0:
        recs.append("Add timed practice this week; speed is a trained skill, not something to discover on exam day.")
    if not error_log:
        recs.append("Start an error log today. The objective is not merely to collect mistakes, but to stop the same mistake from recurring.")
    seen, out = set(), []
    for r in recs:
        if r not in seen:
            out.append(r)
            seen.add(r)
    return out[:7]


tabs = st.tabs([
    "📊 Market & research",
    "🩺 Diagnose me",
    "🗓️ Recovery plan",
    "⏱️ Exam pacing",
    "🛡️ Copyright-safe design",
    "📚 Sources",
])

with tabs[0]:
    st.subheader("What the market tells us")
    c1, c2, c3, c4 = st.columns(4)
    for col, (label, value) in zip([c1, c2, c3, c4], MARKET_FACTS.items()):
        with col:
            st.metric(label, value)
    st.caption("The annual number of active candidates is not stated here; this page avoids inventing a market-size number that the cited sources do not establish.")

    st.markdown("### The practical opportunity")
    st.write(
        "The FRM preparation market already has official materials and many exam-preparation providers. "
        "The gap this tool targets is different: **study execution**. A candidate can own excellent material and still fail if the plan, recall practice, mock timing, error analysis or exam pacing is weak."
    )

    st.markdown("### Recurring failure themes and the product response")
    st.dataframe(pd.DataFrame(THEMES), use_container_width=True, hide_index=True)

    st.markdown("### Research conclusion")
    st.markdown(
        """
        **Repeated failure appears to be multi-factor, not a single-cause problem.** The strongest product thesis is therefore an adaptive study operating system rather than a generic calendar. It should continuously answer four questions:

        1. **Am I actually studying consistently?**
        2. **Am I retrieving and applying, or only rereading?**
        3. **Do my errors show a knowledge problem, a process problem, or a pacing problem?**
        4. **Is my current evidence of readiness strong enough to justify the next attempt?**

        Community reports are used only to identify recurring experiences; they are not treated as statistically representative causes of failure.
        """
    )

with tabs[1]:
    st.subheader("Candidate failure-risk diagnostic")
    st.write("This assessment evaluates your **study process**, not your intelligence and not proprietary FRM content.")

    left, right = st.columns(2)
    with left:
        part = st.radio("Exam", ["Part I", "Part II"], horizontal=True)
        attempts = st.number_input("How many attempts have you already made for this part?", min_value=0, max_value=10, value=0, step=1)
        weeks = st.slider("Weeks until your exam", 1, 32, 12)
        hours_week = st.slider("Realistic study hours per week", 2, 40, 12)
        consistency = st.slider("In the last 4 weeks, how consistently did you hit your planned study time?", 0, 10, 6)
        passive_pct = st.slider("Approx. % of study time spent mainly reading/watching/highlighting", 0, 100, 45, step=5)
    with right:
        mock_count = st.number_input("Full-length mocks completed under timed conditions", min_value=0, max_value=30, value=1, step=1)
        mock_avg = st.slider("Average score on your most recent fresh timed sets/mocks (%)", 0, 100, 55)
        timed_sessions = st.number_input("Timed practice sessions completed in the last 2 weeks", min_value=0, max_value=30, value=2, step=1)
        error_log = st.checkbox("I maintain an error log and retest mistakes", value=False)
        repeats = st.slider("How often do the SAME mistake types reappear? (0 = rarely, 10 = constantly)", 0, 10, 5)
        sleep = st.slider("Average sleep / recovery quality during preparation", 0, 10, 6)

    active_score = clamp(100 - passive_pct)
    consistency_score = consistency * 10
    practice_score = clamp(mock_count * 10 + timed_sessions * 5 + mock_avg * 0.35)
    error_score = clamp((60 if error_log else 20) + (10 - repeats) * 4)
    pacing_score = clamp(timed_sessions * 10 + mock_count * 12)
    readiness_score = clamp(mock_avg * 0.8 + min(mock_count, 4) * 5)
    recovery_score = sleep * 10

    scores = {
        "Consistency": round(consistency_score),
        "Active learning": round(active_score),
        "Practice": round(practice_score),
        "Error repair": round(error_score),
        "Pacing": round(pacing_score),
        "Readiness": round(readiness_score),
        "Recovery": round(recovery_score),
    }

    overall = round(
        0.16 * scores["Consistency"]
        + 0.16 * scores["Active learning"]
        + 0.18 * scores["Practice"]
        + 0.14 * scores["Error repair"]
        + 0.12 * scores["Pacing"]
        + 0.16 * scores["Readiness"]
        + 0.08 * scores["Recovery"]
    )

    st.markdown("### Your process score")
    band, css = score_band(overall)
    st.markdown(f'<div class="{css}"><b>{overall}/100 — {band}</b><br>This is a coaching indicator, not a probability of passing.</div>', unsafe_allow_html=True)
    st.progress(overall / 100)

    score_df = pd.DataFrame({"Dimension": list(scores.keys()), "Score": list(scores.values())})
    st.bar_chart(score_df.set_index("Dimension"))

    st.markdown("### Highest-priority changes")
    for i, rec in enumerate(build_recommendations(scores, attempts, mock_count, passive_pct, timed_sessions, error_log, weeks), 1):
        st.write(f"**{i}. {rec}**")

    capacity = weeks * hours_week
    st.info(f"At your current realistic capacity, you have about **{capacity} study hours** available over the next {weeks} weeks. Treat this as a planning budget, not a guarantee.")

with tabs[2]:
    st.subheader("Build a recovery plan")
    st.write("Use this after a failed attempt or as a preventive plan for a first attempt.")

    c1, c2, c3 = st.columns(3)
    with c1:
        plan_weeks = st.slider("Plan length (weeks)", 4, 28, 12, key="planweeks")
    with c2:
        plan_hours = st.slider("Hours/week", 4, 35, 12, key="planhours")
    with c3:
        exam_date = st.date_input("Target exam date", value=date.today() + timedelta(weeks=plan_weeks))

    total_hours = plan_weeks * plan_hours
    if plan_weeks >= 12:
        shares = [("Repair & learn", 0.35), ("Active recall & targeted practice", 0.25), ("Mixed/timed practice", 0.22), ("Mocks & final review", 0.18)]
    elif plan_weeks >= 8:
        shares = [("Repair & learn", 0.28), ("Active recall & targeted practice", 0.27), ("Mixed/timed practice", 0.25), ("Mocks & final review", 0.20)]
    else:
        shares = [("Repair only critical gaps", 0.20), ("Active recall & targeted practice", 0.25), ("Mixed/timed practice", 0.30), ("Mocks & final review", 0.25)]

    rows = []
    cumulative = 0
    for phase, share in shares:
        h = round(total_hours * share)
        w = max(1, round(plan_weeks * share))
        rows.append([phase, f"{round(share*100)}%", h, w])
        cumulative += h
    rows[-1][2] += total_hours - cumulative
    st.dataframe(pd.DataFrame(rows, columns=["Phase", "Share", "Target hours", "Approx. weeks"]), use_container_width=True, hide_index=True)

    weak = st.text_area("Your weak areas / recurring mistake types (use your own words)", placeholder="Example: probability, regression interpretation, duration/convexity, reading long qualitative questions, calculator speed...")
    st.markdown("### Weekly operating rules")
    st.markdown(
        """
        - **Minimum floor:** define the minimum number of hours you will complete even in a bad week.
        - **Every session ends actively:** recall, solve, explain, or retest—never stop at passive reading only.
        - **Every error gets classified:** knowledge / formula / interpretation / calculator / reading / time / careless decision.
        - **Every week includes mixed work:** do not keep topics permanently isolated once the basics are understood.
        - **Every 1–2 weeks includes timed evidence:** measure whether speed and accuracy are improving together.
        - **The final phase is not for first exposure:** it is for simulation, repair and confidence calibration.
        """
    )
    if weak.strip():
        st.success("Good. Keep that list dynamic: remove an item only after you can demonstrate the fix on a later, fresh attempt—not because you reread the chapter.")

with tabs[3]:
    st.subheader("Exam-day pacing calculator")
    p = st.radio("Select exam", ["Part I — 100 questions / 4 hours", "Part II — 80 questions / 4 hours"], horizontal=True)
    questions = 100 if p.startswith("Part I") else 80
    total_minutes = 240
    reserve = st.slider("Minutes you want to reserve for final review", 0, 45, 20)
    working = total_minutes - reserve
    avg = working / questions

    a, b, c = st.columns(3)
    a.metric("Questions", questions)
    b.metric("Working time", f"{working} min")
    c.metric("Avg. working time / question", f"{avg:.2f} min")

    checkpoints = []
    for frac in [0.25, 0.50, 0.75, 1.00]:
        q = round(questions * frac)
        mins_used = round(working * frac)
        mins_left = total_minutes - mins_used
        checkpoints.append([f"{int(frac*100)}%", q, mins_used, mins_left])
    st.dataframe(pd.DataFrame(checkpoints, columns=["Checkpoint", "Question target", "Working minutes used", "Clock minutes remaining"]), use_container_width=True, hide_index=True)

    st.markdown("### A trainable three-pass rule")
    st.markdown(
        """
        **Pass 1:** take the questions you can solve efficiently and mark time-consuming ones for return.  
        **Pass 2:** return to questions that need deeper calculation or judgement.  
        **Pass 3:** use the final reserve for flagged items and answer review.

        The exact thresholds should be trained in mocks. The important principle is to **pre-decide** when to move on, rather than negotiate with yourself under pressure.
        """
    )

with tabs[4]:
    st.subheader("Copyright- and trademark-safe product design")
    st.markdown('<div class="ip"><b>This app is deliberately designed around the candidate\'s process, not proprietary content.</b></div>', unsafe_allow_html=True)
    st.markdown(
        """
        **What this project can safely create itself**
        - Original diagnostics, schedules, dashboards, trackers, coaching rules and study analytics.
        - Original explanations of general learning science, time management and test-taking strategy.
        - User-entered weak areas, performance history and self-assessment data.
        - Original generic practice on foundational mathematics/statistics/risk concepts when authored independently and not copied or reconstructed from protected questions.

        **What should not be uploaded or reproduced without permission**
        - Actual or recalled FRM exam questions, answer choices, screenshots or reconstructed exam items.
        - GARP textbook pages, Learning Objectives text, proprietary practice exams or substantial extracts from GARP's site.
        - Kaplan/Schweser, Bionic Turtle, AnalystPrep or other provider question banks, notes, videos or paid materials.
        - GARP/provider logos or branding that could imply endorsement.

        **Recommended operating model**
        - Link candidates to official resources rather than mirroring them.
        - Keep the product visibly independent and use a trademark/non-affiliation disclaimer.
        - Make the core intellectual property your own: diagnostics, algorithms, study plans, analytics and original educational content.
        - If you later commercialize the platform at scale, obtain legal review for branding, trademark use and content licensing.
        """
    )
    st.warning("GARP's current Terms of Use include restrictions on reproducing site materials and on automated/AI use of its site content. This project therefore avoids importing, scraping or embedding GARP site/curriculum content and relies on original coaching features plus external links.")

with tabs[5]:
    st.subheader("Research sources")
    st.write("Official sources establish exam facts and IP boundaries; academic sources support the learning-design principles; community sources identify recurring candidate experiences.")
    src = pd.DataFrame(SOURCE_ROWS, columns=["Source", "Item", "Why used", "Link"])
    st.dataframe(src, use_container_width=True, hide_index=True, column_config={"Link": st.column_config.LinkColumn("Link")})
    st.markdown("### Research limitations")
    st.markdown(
        """
        - GARP publishes pass rates, but pass/fail outcomes alone do not identify *why* an individual failed.
        - Reddit and forum posts are self-selected anecdotes, so they are useful for discovering pain points but not for estimating prevalence.
        - General learning-science findings are not FRM-specific randomized trials; they inform product design rather than prove an FRM pass-rate uplift.
        - The diagnostic score in this app is a coaching heuristic, not a validated psychometric instrument and not a predicted probability of passing.
        """
    )

st.divider()
st.caption("Built as an independent, copyright-conscious study-process tool. Educational use only; no pass guarantee.")
