# KIMB BRCC Report Builder

This module provides a quarterly **Board Risk, Compliance and Governance Committee (BRCC)** reporting pack with separate Compliance and Risk sections.

## Deliverables

- `template_data.py` - embeds the verified 11-page fillable PDF template (154 interactive fields) so Streamlit can reconstruct it without a separate binary-file dependency.
- Streamlit page: `pages/02_KIMB_BRCC_Report.py` - enter report data, edit Compliance and Risk KPI/KRI matrices, download the blank fillable PDF, or generate a completed PDF reflecting the entered fields.
- A standalone `KIMB_BRCC_Report_Template.pdf` is also supplied with the project delivery for direct use outside Streamlit.

## Design basis

The structure reflects KIMB's existing Compliance Policy and Risk Management Framework and is benchmarked to:

- Basel Committee corporate governance and compliance-function principles.
- FATF Recommendations and risk-based AML/CFT/CPF controls.
- Public governance and risk reporting practices of Dubai Islamic Bank (BRCC) and Sharjah Islamic Bank (Board Risk Committee).

The included KPI/KRI targets are illustrative starting points. Current regulatory limits and Board-approved thresholds must always prevail.
