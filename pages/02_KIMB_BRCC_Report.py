from __future__ import annotations

from io import BytesIO
from pathlib import Path
from datetime import date

import pandas as pd
import streamlit as st
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT / "KIMB" / "BRCC_Report" / "BRCC_Report_Template.pdf"

st.set_page_config(page_title="KIMB BRCC Report", page_icon="📊", layout="wide")
st.title("📊 KIMB BRCC Report Builder")
st.caption("Compliance & Risk | Quarterly Board Risk, Compliance and Governance Committee pack")
st.info(
    "Built around KIMB's BRCC reporting framework and benchmarked to Basel/FATF principles and public DIB/SIB governance practices. "
    "Illustrative thresholds must always be replaced by current CBY requirements and Board-approved limits."
)

if not TEMPLATE_PATH.exists():
    st.error("BRCC PDF template was not found in KIMB/BRCC_Report.")
    st.stop()
TEMPLATE_BYTES = TEMPLATE_PATH.read_bytes()

COMP_METRICS = [
    ["Regulatory submissions delivered on time", "KPI", "100%", "", "", "", ""],
    ["Critical/High compliance issues overdue", "KRI", "0", "", "", "", ""],
    ["High-risk KYC/UBO/PEP reviews overdue", "KRI", "Board-approved", "", "", "", ""],
    ["Sanctions alerts beyond approved SLA", "KRI", "0 / within SLA", "", "", "", ""],
    ["AML alerts/investigations beyond SLA", "KRI", "Board-approved", "", "", "", ""],
    ["Internal suspicion/STR decision timeliness", "KPI", "100% within SLA", "", "", "", ""],
    ["Role-based compliance training completion", "KPI", ">= 95%", "", "", "", ""],
    ["Branch/agent compliance review coverage", "KPI", "Plan target", "", "", "", ""],
    ["Repeat compliance findings", "KRI", "Downward trend", "", "", "", ""],
    ["Policies/obligations overdue for review", "KRI", "0 material", "", "", "", ""],
]
RISK_METRICS = [
    ["Capital adequacy vs regulatory/internal minimum", "KRI", "Board / CBY limit", "", "", "", ""],
    ["Leverage ratio (internal benchmark where applicable)", "KRI", "Board benchmark", "", "", "", ""],
    ["Legal liquidity / internal liquidity buffer", "KRI", "Above floor + buffer", "", "", "", ""],
    ["LCR / NSFR internal benchmark", "KRI", "Board benchmark", "", "", "", ""],
    ["NPF/NPL ratio and watchlist migration", "KRI", "Board appetite", "", "", "", ""],
    ["Top single / connected exposure utilisation", "KRI", "Within limit", "", "", "", ""],
    ["Aggregate FX open position utilisation", "KRI", "Within CBY/internal limit", "", "", "", ""],
    ["Operational losses and near misses", "KRI", "Within appetite", "", "", "", ""],
    ["Critical system/cyber/BCP incidents", "KRI", "0 unresolved critical", "", "", "", ""],
    ["High/critical risk actions overdue", "KRI", "0 overdue critical", "", "", "", ""],
]
COLS = ["Metric", "Type", "Target / Trigger", "Actual", "Status", "Trend", "Comment / Action"]

if "brcc_comp_metrics" not in st.session_state:
    st.session_state.brcc_comp_metrics = pd.DataFrame(COMP_METRICS, columns=COLS)
if "brcc_risk_metrics" not in st.session_state:
    st.session_state.brcc_risk_metrics = pd.DataFrame(RISK_METRICS, columns=COLS)


def txt(label: str, key: str, height: int = 105) -> str:
    return st.text_area(label, key=key, height=height)


def metric_values(df: pd.DataFrame, prefix: str) -> dict[str, str]:
    values: dict[str, str] = {}
    clean = df.fillna("").astype(str)
    for r in range(10):
        row = clean.iloc[r].tolist() if r < len(clean) else [""] * 7
        for c in range(7):
            values[f"{prefix}_{r}_{c}"] = row[c] if c < len(row) else ""
    return values


def completed_pdf(field_values: dict[str, str]) -> bytes:
    reader = PdfReader(BytesIO(TEMPLATE_BYTES))
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    writer.update_page_form_field_values(None, field_values, auto_regenerate=False, flatten=True)
    out = BytesIO()
    writer.write(out)
    return out.getvalue()


with st.sidebar:
    st.header("Report controls")
    reporting_period = st.text_input("Reporting period", placeholder="e.g., Q3 2026")
    meeting_date = st.date_input("BRCC meeting date", value=date.today())
    prepared_by = st.text_input("Prepared by")
    reviewed_by = st.text_input("Reviewed by")
    overall_status = st.selectbox("Overall BRCC status / RAG", ["", "Green", "Amber", "Red"])
    st.divider()
    st.download_button(
        "⬇️ Download fillable PDF template",
        data=TEMPLATE_BYTES,
        file_name="KIMB_BRCC_Fillable_Template.pdf",
        mime="application/pdf",
        use_container_width=True,
    )

exec_tab, comp_tab, risk_tab, metrics_tab, action_tab = st.tabs(
    ["Executive", "Compliance", "Risk", "KPI / KRI", "Actions & PDF"]
)

with exec_tab:
    a, b = st.columns(2)
    with a:
        txt("Executive summary - key changes since prior quarter", "executive_summary", 150)
        txt("Top matters requiring BRCC decision / challenge", "brcc_decisions_required", 150)
    with b:
        txt("Material breaches / incidents / regulatory deadlines at risk", "material_escalations", 150)
        txt("Top critical/high issues - owner, due date, status, blockers", "integrated_issues", 150)

with comp_tab:
    st.subheader("Compliance executive dashboard")
    a, b = st.columns(2)
    with a:
        txt("Compliance risk profile and quarter-on-quarter movement", "compliance_profile")
        txt("Material regulatory changes and implementation status", "regulatory_changes")
        txt("Monitoring / testing and thematic findings", "compliance_testing")
        txt("Critical / High issue ageing and accountability", "compliance_issues")
        txt("Regulatory / FIU inspections, requests and remediation", "regulatory_interactions")
        txt("Resources, systems and capacity constraints", "compliance_resources")
    with b:
        txt("AML/CFT/CPF risk assessment changes and typologies", "aml_risk")
        txt("Transaction monitoring - volumes, ageing, effectiveness", "tm_summary")
        txt("Internal suspicion / STR governance", "str_summary")
        txt("Sanctions / TFS - list updates, alerts, matches, system issues", "sanctions_summary")
        txt("PF / sanctions-evasion risk and controls", "pf_summary")
        txt("AML / sanctions management actions", "aml_actions")
    st.subheader("CDD, correspondents, conduct and culture")
    a, b = st.columns(2)
    with a:
        txt("CDD / KYC / UBO / PEP quality and overdue reviews", "cdd_summary")
        txt("Correspondent banking and high-risk counterparties", "correspondent_summary")
        txt("Branch / agent compliance reviews", "branch_reviews")
    with b:
        txt("Customer protection, complaints, fraud / conduct, whistleblowing", "conduct_summary")
        txt("Policy review and training completion / effectiveness", "training_policy")
        txt("New products / systems / outsourcing compliance assessment", "new_products_compliance")

with risk_tab:
    st.subheader("Risk executive dashboard")
    a, b = st.columns(2)
    with a:
        txt("Enterprise risk profile and quarter-on-quarter movement", "risk_profile")
        txt("Risk appetite / limits - breaches, amber triggers, waivers", "risk_appetite")
        txt("Emerging risks and external environment", "emerging_risks")
        txt("Top management actions / BRCC challenge points", "risk_actions")
        txt("Audit / regulatory findings and remediation ageing", "risk_findings")
        txt("Policy exceptions / material new products / outsourcing", "risk_exceptions")
    with b:
        txt("Capital adequacy and buffers", "capital_summary")
        txt("Liquidity & funding", "liquidity_summary")
        txt("Credit / financing risk", "credit_summary")
        txt("Market / FX risk", "market_summary")
        txt("Country / counterparty / correspondent concentration", "concentration_summary")
        txt("Financial risk actions / escalation", "financial_risk_actions")
    st.subheader("Operational resilience and stress")
    a, b = st.columns(2)
    with a:
        txt("Operational losses, incidents and near misses", "operational_summary")
        txt("IT / cyber / system availability", "cyber_summary")
        txt("BCP / disaster recovery / critical services", "bcp_summary")
    with b:
        txt("Third-party / outsourcing / vendor risk", "third_party_summary")
        txt("Stress / sensitivity / reverse-stress testing", "stress_testing")
        txt("Operational resilience actions / escalation", "operational_actions")

with metrics_tab:
    st.subheader("Compliance KPI / KRI matrix")
    st.caption("Targets are starting points only. Replace them with current regulatory or Board-approved thresholds.")
    st.session_state.brcc_comp_metrics = st.data_editor(
        st.session_state.brcc_comp_metrics,
        num_rows="dynamic",
        use_container_width=True,
        hide_index=True,
        key="brcc_comp_editor",
    )
    txt("Head of Compliance commentary", "compliance_commentary", 140)
    st.subheader("Risk KPI / KRI matrix")
    st.session_state.brcc_risk_metrics = st.data_editor(
        st.session_state.brcc_risk_metrics,
        num_rows="dynamic",
        use_container_width=True,
        hide_index=True,
        key="brcc_risk_editor",
    )
    txt("CRO / Risk Head commentary", "risk_commentary", 140)

with action_tab:
    txt("BRCC decisions / approvals / challenges / conditions", "brcc_decisions", 130)
    txt("Actions agreed - owner and due date", "agreed_actions", 130)
    txt("Matters escalated to Board / Audit Committee / other forum", "board_escalations", 110)
    st.subheader("Sign-off")
    a, b, c, d = st.columns(4)
    with a:
        st.text_input("Head of Compliance", key="signoff_compliance")
    with b:
        st.text_input("Head of Risk / CRO", key="signoff_risk")
    with c:
        st.text_input("CEO / Senior Management", key="signoff_ceo")
    with d:
        st.text_input("BRCC Chair / Secretary", key="signoff_brcc")

    fields = {
        "reporting_period": reporting_period,
        "meeting_date": meeting_date.strftime("%d %b %Y") if meeting_date else "",
        "prepared_by": prepared_by,
        "reviewed_by": reviewed_by,
        "overall_status": overall_status,
    }
    text_keys = [
        "executive_summary", "brcc_decisions_required", "material_escalations",
        "compliance_profile", "regulatory_changes", "compliance_testing", "compliance_issues",
        "regulatory_interactions", "compliance_resources", "aml_risk", "tm_summary", "str_summary",
        "sanctions_summary", "pf_summary", "aml_actions", "cdd_summary", "correspondent_summary",
        "branch_reviews", "conduct_summary", "training_policy", "new_products_compliance",
        "compliance_commentary", "risk_profile", "risk_appetite", "emerging_risks", "risk_actions",
        "risk_findings", "risk_exceptions", "capital_summary", "liquidity_summary", "credit_summary",
        "market_summary", "concentration_summary", "financial_risk_actions", "operational_summary",
        "cyber_summary", "bcp_summary", "third_party_summary", "stress_testing", "operational_actions",
        "risk_commentary", "integrated_issues", "brcc_decisions", "agreed_actions", "board_escalations",
        "signoff_compliance", "signoff_risk", "signoff_ceo", "signoff_brcc",
    ]
    fields.update({k: str(st.session_state.get(k, "")) for k in text_keys})
    fields.update(metric_values(st.session_state.brcc_comp_metrics, "comp_metric"))
    fields.update(metric_values(st.session_state.brcc_risk_metrics, "risk_metric"))

    report_bytes = completed_pdf(fields)
    safe_period = reporting_period.strip().replace(" ", "_") or "Draft"
    st.success("The downloadable PDF below reflects the fields entered in this Streamlit page.")
    st.download_button(
        "📄 Generate / Download completed BRCC PDF",
        data=report_bytes,
        file_name=f"KIMB_BRCC_Report_{safe_period}.pdf",
        mime="application/pdf",
        use_container_width=True,
    )

st.caption(
    "Reference basis: KIMB Compliance Policy / Risk Management Framework; Basel Committee governance and compliance principles; "
    "FATF Recommendations; and public governance disclosures of Dubai Islamic Bank and Sharjah Islamic Bank."
)
