import streamlit as st

st.set_page_config(
    page_title="FRM ML — Confusion Matrix",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 FRM Part I — Machine Learning Challenge")
st.caption("Quantitative Analysis • Machine Learning and Prediction • Confusion Matrix")

st.info(
    "A bank uses a machine-learning classifier to identify borrowers who will default. "
    "The model is tested on 1,000 borrowers."
)

st.markdown(
    """
|                        | Predicted Default | Predicted Non-default |
|------------------------|------------------:|----------------------:|
| **Actual Default**     | 72                | 18                    |
| **Actual Non-default** | 90                | 820                   |
"""
)

st.subheader("Question")
st.write(
    "What is the model's **recall (sensitivity) for the default class**, "
    "and what does it mean?"
)

choices = {
    "A": "44.4% — 44.4% of predicted defaults actually defaulted",
    "B": "80.0% — 80.0% of actual defaults were correctly identified",
    "C": "90.1% — 90.1% of actual non-defaults were correctly identified",
    "D": "8.0% — 8.0% of all borrowers were correctly identified as defaults",
}

answer = st.radio(
    "Choose the best answer:",
    options=list(choices.keys()),
    format_func=lambda key: f"{key}. {choices[key]}",
    index=None,
)

if "ml_submitted" not in st.session_state:
    st.session_state.ml_submitted = False

if st.button("Submit Answer", type="primary", use_container_width=True):
    if answer is None:
        st.warning("⚠️ Please choose an answer first.")
    else:
        st.session_state.ml_submitted = True
        st.session_state.ml_answer = answer

if st.session_state.ml_submitted:
    selected = st.session_state.get("ml_answer")

    if selected == "B":
        st.success("✅ Correct! Recall = 80.0% 🔥")
        st.balloons()
    else:
        st.error("❌ Incorrect. The correct answer is B: 80.0%.")

    st.latex(
        r"\text{Recall} = \frac{TP}{TP+FN} = \frac{72}{72+18} = 0.80 = 80\%"
    )

    st.write(
        "Interpretation: among borrowers who **actually defaulted**, the model correctly "
        "classified **80%** of them as defaults."
    )

    with st.expander("💡 FRM exam trap"):
        st.markdown(
            """
- **Recall / Sensitivity** = TP / (TP + FN): *Of actual defaults, how many did the model catch?*
- **Precision** = TP / (TP + FP): *Of predicted defaults, how many truly defaulted?*
- **Specificity** = TN / (TN + FP): *Of actual non-defaults, how many did the model correctly reject?*
- **Accuracy** = (TP + TN) / Total: can look strong even when the event of interest is rare.
"""
        )

    tp, fn, fp, tn = 72, 18, 90, 820
    precision = tp / (tp + fp)
    specificity = tn / (tn + fp)
    accuracy = (tp + tn) / (tp + tn + fp + fn)

    with st.expander("📊 Check the other metrics"):
        st.metric("Recall / Sensitivity", f"{tp / (tp + fn):.1%}")
        st.metric("Precision", f"{precision:.1%}")
        st.metric("Specificity", f"{specificity:.1%}")
        st.metric("Accuracy", f"{accuracy:.1%}")

st.divider()
st.caption(
    "Original FRM-style practice question aligned with binary-classification performance concepts."
)
