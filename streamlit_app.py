import streamlit as st
import streamlit.components.v1 as components

st.title("🔥 HASAN'S FRM EXAM MEMORY REVIEW 🔥")
st.caption("Questions created from key topics remembered after the FRM exam.")

# -----------------------------
# QUESTION BANK
# -----------------------------

questions = [

    {
        "category": "Machine Learning vs. Econometrics",
        "question": """A bank wants to analyze corporate loan defaults. Management has two objectives:

1. Predict which current borrowers are most likely to default.
2. Determine whether increasing the collateral requirement would cause a reduction in default probability, while quantifying statistical uncertainty.

Which approach is most appropriate?""",
        "options": [
            "A. Use conventional econometrics for the first objective and machine learning for the second, because econometric models maximize predictive accuracy while machine-learning models establish causality.",
            "B. Use only machine learning for both objectives, because cross-validation can establish whether changing the collateral requirement causes lower defaults.",
            "C. Use a validated machine-learning model primarily for the prediction objective and a properly specified econometric or causal-inference framework for the causal objective.",
            "D. Use only conventional econometrics for both objectives, because machine-learning models cannot analyze default probabilities when explanatory variables are correlated."
        ],
        "answer": "C. Use a validated machine-learning model primarily for the prediction objective and a properly specified econometric or causal-inference framework for the causal objective.",
        "explanation": "Machine learning is often designed for strong out-of-sample prediction and can capture nonlinearities and complex interactions. A causal policy question requires a credible identification strategy, for which a properly specified econometric or causal-inference framework is generally more appropriate. Strong prediction alone does not establish causation.",
        "solution_steps": [
            "Identify Objective 1 as a prediction problem: which borrowers are likely to default?",
            "Identify Objective 2 as a causal question: what would happen if the bank changed collateral requirements?",
            "Distinguish predictive association from causal effect.",
            "Match each objective to its principal strength: validated machine learning for prediction; econometric or causal-inference methods for intervention effects and statistical uncertainty."
        ],
        "option_explanations": {
            "A": "Incorrect — this reverses the usual comparative strengths. Machine learning commonly emphasizes prediction, while econometric and causal methods emphasize inference, interpretation, and causal identification.",
            "B": "Incorrect — cross-validation evaluates predictive performance; by itself it does not resolve confounding, selection bias, or reverse causality.",
            "C": "Correct — it matches the predictive objective with validated machine learning and the intervention question with an appropriate causal framework.",
            "D": "Incorrect — machine-learning models can use correlated predictors, although correlation can affect stability and interpretation in some models."
        },
        "exam_tip": "Prediction asks: What is likely to happen? Causal inference asks: What would happen if we intervened?",
        "countdown_seconds": 60,
        "disclaimer": "This independently created educational content is for learning purposes only. It is not an official GARP® or FRM® examination question and is not endorsed by or affiliated with GARP."
    },

    {
        "category": "Probability",
        "question": "If P(A) = 55%, P(B) = 45%, and P(A ∩ B) = 30%, what is P(A | B)?",
        "options": [
            "30.00%",
            "54.55%",
            "66.67%",
            "75.00%"
        ],
        "answer": "66.67%",
        "explanation": "P(A|B) = P(A ∩ B) / P(B) = 0.30 / 0.45 = 66.67%."
    },

    {
        "category": "Probability",
        "question": "Which formula gives P(A ∪ B)?",
        "options": [
            "P(A) + P(B)",
            "P(A) + P(B) - P(A ∩ B)",
            "P(A) × P(B)",
            "P(A ∩ B) / P(B)"
        ],
        "answer": "P(A) + P(B) - P(A ∩ B)",
        "explanation": "For a union, add the two probabilities and subtract the overlap."
    },

    {
        "category": "Probability",
        "question": "The symbol ∩ represents:",
        "options": [
            "Union / OR",
            "Intersection / AND",
            "Conditional probability",
            "Complement"
        ],
        "answer": "Intersection / AND",
        "explanation": "∩ means intersection: both events occur. Our famous upside-down CUP dude 😂."
    },

    {
        "category": "Statistics",
        "question": "Variance measures:",
        "options": [
            "The average level of a variable",
            "Dispersion around the mean",
            "Correlation only",
            "Skewness only"
        ],
        "answer": "Dispersion around the mean",
        "explanation": "Variance measures how widely observations are spread around their mean."
    },

    {
        "category": "Statistics",
        "question": "Covariance is primarily used to measure:",
        "options": [
            "The joint movement of two variables",
            "The average of one variable",
            "The kurtosis of a distribution",
            "The probability of default"
        ],
        "answer": "The joint movement of two variables",
        "explanation": "Positive covariance means two variables tend to move together; negative covariance means they tend to move in opposite directions."
    },

    {
        "category": "Statistics",
        "question": "A z-score is calculated as:",
        "options": [
            "(X + Mean) / SD",
            "(X - Mean) / SD",
            "Mean / X",
            "Variance / Mean"
        ],
        "answer": "(X - Mean) / SD",
        "explanation": "The z-score tells you how many standard deviations an observation is from the mean."
    },

    {
        "category": "Statistics",
        "question": "High positive kurtosis generally indicates:",
        "options": [
            "Very thin tails",
            "Fat tails and more extreme observations",
            "No variance",
            "Perfect normality"
        ],
        "answer": "Fat tails and more extreme observations",
        "explanation": "High kurtosis is associated with heavier tails and a greater probability of extreme outcomes."
    },

    {
        "category": "Regression",
        "question": "In linear regression, the error term represents:",
        "options": [
            "The part of Y perfectly explained by X",
            "The unexplained component of Y",
            "The slope coefficient",
            "The intercept only"
        ],
        "answer": "The unexplained component of Y",
        "explanation": "The error term captures variation in the dependent variable that the model does not explain."
    },

    {
        "category": "Regression",
        "question": "Logistic regression is especially suitable when the dependent variable is:",
        "options": [
            "A continuous interest rate",
            "A bond price",
            "Binary, such as default / no default",
            "Always normally distributed"
        ],
        "answer": "Binary, such as default / no default",
        "explanation": "Logistic regression is commonly used for classification problems with outcomes such as 0/1."
    },

    {
        "category": "Regression",
        "question": "Cook's Distance is mainly used to identify:",
        "options": [
            "Influential observations in regression",
            "Option volatility",
            "Bond duration",
            "Credit spreads"
        ],
        "answer": "Influential observations in regression",
        "explanation": "Cook's Distance helps identify observations that have a large influence on regression estimates."
    },

    {
        "category": "Machine Learning",
        "question": "Which type of machine learning uses labeled observations?",
        "options": [
            "Supervised learning",
            "Unsupervised learning",
            "Reinforcement learning only",
            "Monte Carlo learning"
        ],
        "answer": "Supervised learning",
        "explanation": "Supervised learning trains using inputs together with known target labels."
    },

    {
        "category": "Machine Learning",
        "question": "Overfitting is typically associated with:",
        "options": [
            "High bias and low variance",
            "Low bias and high variance",
            "High bias and high variance only",
            "Zero model error everywhere"
        ],
        "answer": "Low bias and high variance",
        "explanation": "An overfit model fits training data extremely well but can perform poorly on new data."
    },

    {
        "category": "Machine Learning",
        "question": "A bank tests a default-classification model. The model correctly identifies 72 borrowers who actually default and misses 18 borrowers who actually default. What is the model's recall (sensitivity) for the default class?",
        "options": [
            "44.44%",
            "80.00%",
            "90.11%",
            "92.00%"
        ],
        "answer": "80.00%",
        "explanation": "Recall (sensitivity) = TP / (TP + FN) = 72 / (72 + 18) = 80%. It measures the percentage of actual defaults correctly identified by the model. Do not confuse recall with precision, which uses TP / (TP + FP)."
    },

    {
        "category": "Machine Learning",
        "question": "Which statement best distinguishes underfitting from overfitting in a machine-learning model?",
        "options": [
            "Underfitting is associated with high bias and low variance, while overfitting is associated with low bias and high variance",
            "Underfitting is associated with low bias and high variance, while overfitting is associated with high bias and low variance",
            "Both underfitting and overfitting are associated with high bias and low variance",
            "Underfitting and overfitting have the same effect on out-of-sample performance"
        ],
        "answer": "Underfitting is associated with high bias and low variance, while overfitting is associated with low bias and high variance",
        "explanation": "Underfitting occurs when a model is too simple to capture important patterns, producing high bias and typically low variance. Overfitting occurs when a model is too complex and fits noise in the training data, producing low bias but high variance and weaker out-of-sample performance."
    },

    {
        "category": "Machine Learning",
        "question": "Which of the following BEST describes a key difference between classical econometric modeling and machine learning?",
        "options": [
            "Classical econometrics mainly focuses on maximizing out-of-sample predictive accuracy, while machine learning mainly focuses on estimating interpretable model parameters.",
            "Classical econometrics typically places greater emphasis on model specification, assumptions, parameter interpretation, and statistical inference, whereas machine learning generally places greater emphasis on flexible pattern recognition and out-of-sample prediction.",
            "Classical econometric models can only use continuous variables, while machine-learning models can use both continuous and categorical variables.",
            "Machine-learning models always require fewer observations than classical econometric models."
        ],
        "answer": "Classical econometrics typically places greater emphasis on model specification, assumptions, parameter interpretation, and statistical inference, whereas machine learning generally places greater emphasis on flexible pattern recognition and out-of-sample prediction.",
        "explanation": "Classical econometrics generally starts with a specified statistical/economic relationship and places strong emphasis on assumptions, parameter estimates, interpretation, and inference. Machine learning generally puts greater emphasis on learning patterns from data and achieving strong out-of-sample predictive performance, often using tools such as training/testing data, cross-validation, and regularization. The distinction is not absolute because the two approaches can overlap.",
        "memory_trick": "Econometrics → Explain / Infer\n\nMachine Learning → Predict / Generalize"
    },

    {
        "category": "Time Series",
        "question": "For a stationary AR(1) process, the absolute value of the AR coefficient should generally be:",
        "options": [
            "Greater than 2",
            "Equal to 1",
            "Less than 1",
            "Always zero"
        ],
        "answer": "Less than 1",
        "explanation": "For AR(1), stationarity generally requires |φ| < 1."
    },

    {
        "category": "Time Series",
        "question": "ARIMA models are mainly associated with:",
        "options": [
            "Time-series analysis",
            "Option pricing only",
            "Credit ratings only",
            "Accounting ratios"
        ],
        "answer": "Time-series analysis",
        "explanation": "ARIMA stands for Autoregressive Integrated Moving Average."
    },

    {
        "category": "Simulation",
        "question": "Monte Carlo simulation estimates risk by:",
        "options": [
            "Generating many possible scenarios",
            "Using only one historical observation",
            "Eliminating randomness",
            "Ignoring distributions"
        ],
        "answer": "Generating many possible scenarios",
        "explanation": "Monte Carlo repeatedly simulates possible outcomes using assumed probability distributions."
    },

    {
        "category": "Market Risk",
        "question": "Expected Shortfall (ES) measures:",
        "options": [
            "The maximum gain at a confidence level",
            "The average loss beyond the VaR threshold",
            "The probability that VaR equals zero",
            "The bond coupon rate"
        ],
        "answer": "The average loss beyond the VaR threshold",
        "explanation": "ES looks into the tail and estimates the average loss conditional on losses exceeding VaR."
    },

    {
        "category": "Market Risk",
        "question": "Stress testing is primarily designed to:",
        "options": [
            "Estimate performance under severe but plausible scenarios",
            "Guarantee future profit",
            "Replace all VaR models",
            "Eliminate market risk"
        ],
        "answer": "Estimate performance under severe but plausible scenarios",
        "explanation": "Stress tests examine the impact of extreme scenarios that may not be adequately captured by normal risk models."
    },

    {
        "category": "Market Risk",
        "question": "DV01 represents approximately:",
        "options": [
            "The price change for a 1 basis point yield movement",
            "The default probability over one year",
            "The option delta",
            "The bond coupon payment"
        ],
        "answer": "The price change for a 1 basis point yield movement",
        "explanation": "DV01 is the dollar value change associated with a one-basis-point movement in yield."
    },

    {
        "category": "Options",
        "question": "Gamma measures:",
        "options": [
            "The change in option delta when the underlying price changes",
            "The change in option value when time passes",
            "The change in option value when volatility changes",
            "The change in interest rates"
        ],
        "answer": "The change in option delta when the underlying price changes",
        "explanation": "Gamma is the sensitivity of delta to changes in the underlying asset price."
    },

    {
        "category": "Options",
        "question": "Vega measures sensitivity of an option price to:",
        "options": [
            "Volatility",
            "Time only",
            "Dividend payment only",
            "Credit rating"
        ],
        "answer": "Volatility",
        "explanation": "Vega tells us how the option value changes when implied volatility changes."
    },

    {
        "category": "Options",
        "question": "Theta measures sensitivity of an option price to:",
        "options": [
            "Passage of time",
            "Volatility",
            "Underlying price only",
            "Credit spread"
        ],
        "answer": "Passage of time",
        "explanation": "Theta measures time decay."
    },

    {
        "category": "Options",
        "question": "An American option may generally be exercised:",
        "options": [
            "Only at expiration",
            "At any time up to and including expiration",
            "Only after a dividend",
            "Only one year before expiration"
        ],
        "answer": "At any time up to and including expiration",
        "explanation": "This exercise flexibility distinguishes American options from European options."
    },

    {
        "category": "CAPM",
        "question": "Under CAPM, idiosyncratic risk is:",
        "options": [
            "Rewarded with a higher expected return",
            "Diversifiable and therefore not priced",
            "The same as systematic risk",
            "Measured exclusively by duration"
        ],
        "answer": "Diversifiable and therefore not priced",
        "explanation": "CAPM compensates investors for systematic risk, measured by beta, rather than diversifiable idiosyncratic risk."
    },

    {
        "category": "CAPM",
        "question": "If beta doubles while the risk-free rate and market risk premium remain unchanged, what happens to the beta-related risk premium?",
        "options": [
            "It is cut in half",
            "It doubles",
            "It becomes zero",
            "It becomes negative automatically"
        ],
        "answer": "It doubles",
        "explanation": "CAPM: E(R) = Rf + Beta × Market Risk Premium."
    },

    {
        "category": "Portfolio Management",
        "question": "The Treynor ratio uses which measure of risk in its denominator?",
        "options": [
            "Beta",
            "Standard deviation",
            "Variance",
            "DV01"
        ],
        "answer": "Beta",
        "explanation": "Treynor evaluates excess return relative to systematic risk, measured by beta."
    },

    {
        "category": "Portfolio Management",
        "question": "The Fama-French three-factor model adds which factors to the market factor?",
        "options": [
            "Size and value",
            "Duration and convexity",
            "Gamma and vega",
            "Liquidity and inflation only"
        ],
        "answer": "Size and value",
        "explanation": "The classic three factors are market, SMB (size), and HML (value)."
    },

    {
        "category": "Fixed Income",
        "question": "A zero-coupon bond:",
        "options": [
            "Pays regular coupon payments",
            "Makes no coupon payments before maturity",
            "Always trades at par",
            "Has zero yield to maturity"
        ],
        "answer": "Makes no coupon payments before maturity",
        "explanation": "A zero-coupon bond pays its face value at maturity and normally trades at a discount before maturity."
    },

    {
        "category": "Fixed Income",
        "question": "For a conventional bond, if YTM rises while everything else remains unchanged, the bond price generally:",
        "options": [
            "Rises",
            "Falls",
            "Remains unchanged",
            "Becomes zero"
        ],
        "answer": "Falls",
        "explanation": "Bond prices and yields generally move in opposite directions."
    },

    {
        "category": "Credit Risk",
        "question": "Unexpected credit loss is generally associated with:",
        "options": [
            "Loss variability around expected loss",
            "The expected annual coupon",
            "The risk-free rate",
            "Only operational losses"
        ],
        "answer": "Loss variability around expected loss",
        "explanation": "Expected loss is anticipated and priced/provisioned; unexpected loss represents adverse deviations around that expectation."
    },

    {
        "category": "Operational Risk",
        "question": "Operational risk is primarily the risk of loss resulting from:",
        "options": [
            "Failed processes, people, systems, or external events",
            "Only changes in interest rates",
            "Only changes in FX rates",
            "Only bond defaults"
        ],
        "answer": "Failed processes, people, systems, or external events",
        "explanation": "Operational risk covers failures in processes, people and systems, as well as external events."
    },

    {
        "category": "Liquidity Risk",
        "question": "Funding liquidity risk refers to the risk that an institution:",
        "options": [
            "Cannot meet its payment obligations when due",
            "Cannot calculate beta",
            "Cannot price an option",
            "Has a high coupon bond"
        ],
        "answer": "Cannot meet its payment obligations when due",
        "explanation": "Funding liquidity risk concerns an institution's ability to obtain funds and meet obligations."
    },

    {
        "category": "ERM",
        "question": "Enterprise Risk Management (ERM) is best described as:",
        "options": [
            "Managing risks across the organization in an integrated manner",
            "Managing only market risk",
            "Managing only operational risk",
            "Eliminating all risk"
        ],
        "answer": "Managing risks across the organization in an integrated manner",
        "explanation": "ERM provides an organization-wide framework for identifying, assessing, managing, and monitoring risks."
    },

    {
        "category": "FX / Forwards",
        "question": "A forward contract is best described as:",
        "options": [
            "An agreement today to transact at a specified future date and price",
            "A transaction that must settle immediately",
            "An equity dividend",
            "A credit rating"
        ],
        "answer": "An agreement today to transact at a specified future date and price",
        "explanation": "Forward contracts lock in terms today for a transaction occurring in the future."
    },

    {
        "category": "Fixed Income",
        "question": "High-yield bonds generally have:",
        "options": [
            "Higher credit risk and higher promised yields",
            "Zero credit risk",
            "Lower yields than risk-free bonds by definition",
            "No default exposure"
        ],
        "answer": "Higher credit risk and higher promised yields",
        "explanation": "Investors generally require higher yields to compensate for greater credit risk."
    },

    {
        "category": "Markets",
        "question": "The law of one price states that:",
        "options": [
            "Identical assets with identical cash flows should have the same price",
            "Every bond must trade at par",
            "Every stock must have the same beta",
            "All options have identical volatility"
        ],
        "answer": "Identical assets with identical cash flows should have the same price",
        "explanation": "If identical cash flows had different prices, arbitrage opportunities could arise."
    },

    {
        "category": "Mortgages",
        "question": "In mortgage markets, TBA commonly means:",
        "options": [
            "To Be Announced",
            "Total Bond Allocation",
            "Term-Based Arbitrage",
            "Treasury Benchmark Adjustment"
        ],
        "answer": "To Be Announced",
        "explanation": "TBA is a common forward-settlement convention in agency mortgage-backed securities markets."
    },

    {
        "category": "Ethics",
        "question": "Under the GARP Code of Conduct, a risk professional should primarily:",
        "options": [
            "Act with integrity and professional competence",
            "Hide material conflicts of interest",
            "Guarantee investment performance",
            "Ignore applicable rules when profitable"
        ],
        "answer": "Act with integrity and professional competence",
        "explanation": "Integrity, professional conduct, competence, and appropriate disclosure are central principles of professional ethics."
    }
]


# -----------------------------
# SESSION STATE
# -----------------------------

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "selected_answer" not in st.session_state:
    st.session_state.selected_answer = None


# -----------------------------
# QUIZ DISPLAY
# -----------------------------

total_questions = len(questions)
current = st.session_state.current_question

st.progress(current / total_questions)

st.write(
    f"### Question {current + 1} of {total_questions}"
)

question = questions[current]

st.caption("Topic: " + question["category"])

st.subheader(question["question"])

if question.get("countdown_seconds"):
    components.html(
        f"""
        <div style="font-family:Arial,sans-serif;text-align:center;padding:10px;
                    border-radius:12px;background:#0f172a;color:white;">
            <div style="font-size:14px;letter-spacing:.08em;">ANSWER-REVEAL COUNTDOWN</div>
            <div id="frm-timer" style="font-size:38px;font-weight:800;color:#38bdf8;">
                {question["countdown_seconds"]}
            </div>
        </div>
        <script>
            let remaining = {question["countdown_seconds"]};
            const timer = document.getElementById("frm-timer");
            const tick = setInterval(() => {{
                remaining -= 1;
                timer.textContent = remaining;
                if (remaining <= 0) {{
                    clearInterval(tick);
                    timer.textContent = "Time!";
                    timer.style.color = "#fbbf24";
                }}
            }}, 1000);
        </script>
        """,
        height=105,
    )

selected = st.radio(
    "Choose your answer:",
    question["options"],
    index=None,
    key=f"question_{current}"
)


# -----------------------------
# SUBMIT ANSWER
# -----------------------------

if st.button("Submit Answer", disabled=st.session_state.answered):

    if selected is None:
        st.warning("⚠️ Please select an answer.")

    else:
        st.session_state.selected_answer = selected
        st.session_state.answered = True

        if selected == question["answer"]:
            st.session_state.score += 1


# -----------------------------
# SHOW RESULT
# -----------------------------

if st.session_state.answered:

    if st.session_state.selected_answer == question["answer"]:
        st.success("✅ Correct! 🔥")
        st.balloons()

    else:
        st.error(
            "❌ Incorrect. Correct answer: "
            + question["answer"]
        )

    st.info("💡 " + question["explanation"])

    if question.get("solution_steps"):
        st.markdown("### Step-by-step solution")
        for step_number, step in enumerate(question["solution_steps"], 1):
            st.write(f"**{step_number}.** {step}")

    if question.get("option_explanations"):
        st.markdown("### Why each choice is right or wrong")
        for option_letter, option_explanation in question["option_explanations"].items():
            st.write(f"**{option_letter}.** {option_explanation}")

    if question.get("exam_tip"):
        st.success("🎯 Exam Tip: " + question["exam_tip"])

    if question.get("disclaimer"):
        st.caption(question["disclaimer"])

    if question.get("memory_trick"):
        st.markdown("**Memory trick:**")
        st.info(question["memory_trick"])

    st.write(
        f"### Current score: {st.session_state.score} / {current + 1}"
    )


    # NEXT QUESTION
    if current < total_questions - 1:

        if st.button("Next Question ➡️"):

            st.session_state.current_question += 1
            st.session_state.answered = False
            st.session_state.selected_answer = None

            st.rerun()

    else:

        st.success("🏁 QUIZ COMPLETED!")

        percentage = (
            st.session_state.score / total_questions
        ) * 100

        st.write(
            f"## Final Score: {st.session_state.score} / {total_questions}"
        )

        st.write(
            f"## Percentage: {percentage:.1f}%"
        )

        if percentage >= 80:
            st.success("🔥 Excellent FRM review!")
        elif percentage >= 60:
            st.warning("👍 Good, but let's review the weak areas.")
        else:
            st.error("😂 Back to the books, dude!")


# -----------------------------
# RESET
# -----------------------------

st.divider()

if st.button("🔄 Restart Quiz"):

    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected_answer = None

    st.rerun()
