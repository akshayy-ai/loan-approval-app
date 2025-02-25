import streamlit as st
import os
import pickle
import numpy as np
import time  # For animation effect

# Load Model
MODEL_PATH = "model/model.pkl"
if not os.path.exists(MODEL_PATH):
    st.error("❌ Model file not found! Please train the model first.")
    st.stop()

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.set_page_config(page_title="Loan Approval Predictor", page_icon="🏦", layout="centered")
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏦 Loan Approval Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Fill in the details below to check your loan eligibility.</p>", unsafe_allow_html=True)

# Form Input Fields
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        gender = st.radio("👤 Gender", ["Male", "Female"], horizontal=True)
        married = st.radio("💍 Married", ["No", "Yes"], horizontal=True)
        education = st.radio("🎓 Education", ["Not Graduate", "Graduate"], horizontal=True)
        self_employed = st.radio("🏢 Self Employed", ["No", "Yes"], horizontal=True)
        dependents = st.radio("👶 Dependents", ["0", "1", "2", "3+"], horizontal=True)

    with col2:
        applicant_income = st.slider("💰 Applicant Income ($)", min_value=0, max_value=15000, step=500, value=4000)
        coapplicant_income = st.slider("💵 Coapplicant Income ($)", min_value=0, max_value=10000, step=500, value=2000)
        loan_amount = st.slider("🏦 Loan Amount ($)", min_value=500, max_value=500000, step=5000, value=100000)
        loan_term = st.slider("📆 Loan Term (Months)", min_value=12, max_value=360, step=12, value=120)
        credit_history = st.radio("📝 Credit History", [1, 0], format_func=lambda x: "Good" if x == 1 else "Poor", horizontal=True)
        property_area = st.radio("🏠 Property Area", ["Rural", "Semiurban", "Urban"], horizontal=True)

# Convert Inputs for Model
data = [
    0 if gender == "Male" else 1,
    0 if married == "No" else 1,
    0 if education == "Not Graduate" else 1,
    0 if self_employed == "No" else 1,
    applicant_income, coapplicant_income, loan_amount, loan_term, credit_history,
    1 if property_area == "Rural" else 0, 1 if property_area == "Semiurban" else 0, 1 if property_area == "Urban" else 0,
    1 if dependents == "0" else 0, 1 if dependents == "1" else 0, 1 if dependents == "2" else 0, 1 if dependents == "3+" else 0
]

# Prediction Button
if st.button("🚀 Predict Loan Status"):
    with st.spinner("Processing your application..."):
        time.sleep(2)  # Simulating processing delay
        prediction = model.predict(np.array(data).reshape(1, -1))[0]

    if prediction == 1:
        st.success("✅ Congratulations! Your loan is Approved.")
        st.balloons()  # 🎈 Approval animation
    else:
        # Rejection animation (shaking effect)
        st.markdown(
            """
            <style>
                @keyframes shake {
                    0% { transform: translateX(0); }
                    25% { transform: translateX(-5px); }
                    50% { transform: translateX(5px); }
                    75% { transform: translateX(-5px); }
                    100% { transform: translateX(0); }
                }
                .shake {
                    animation: shake 0.5s ease-in-out 2;
                }
            </style>
            <div class="shake">
                <h2 style="color: red; text-align: center;">❌ Sorry! Your loan is Rejected.</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Display possible rejection reasons
        rejection_reasons = []
        if applicant_income < 3000:
            rejection_reasons.append("🔴 Low applicant income.")
        if coapplicant_income < 1000 and applicant_income < 5000:
            rejection_reasons.append("🔴 Low co-applicant income.")
        if loan_amount > (applicant_income + coapplicant_income) * 6:
            rejection_reasons.append("🔴 High loan amount compared to income.")
        if loan_term < 12:
            rejection_reasons.append("🔴 Loan term is too short.")
        if credit_history == 0:
            rejection_reasons.append("🔴 No credit history or poor credit score.")
        if property_area == "Rural" and applicant_income < 4000:
            rejection_reasons.append("🔴 Low income for a rural property.")

        if rejection_reasons:
            st.warning("⚠️ Possible Reasons for Rejection:")
            for reason in rejection_reasons:
                st.write(reason)

# Footer with Animation (Typing Effect)
st.markdown(
    """
    <style>
    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }
    @keyframes blink {
        50% { border-color: transparent }
    }
    .typing-container {
        text-align: center;
        margin-top: 20px;
    }
    .typing {
        display: inline-block;
        overflow: hidden;
        border-right: 2px solid orange;
        white-space: nowrap;
        letter-spacing: 2px;
        animation: typing 3s steps(30, end) forwards, blink 1s step-end infinite;
        font-size: 16px;
        font-weight: bold;
        color: #888;
    }
    </style>
    <div class="typing-container">
        <p class="typing">Developed by Akshay Shitole 🚀</p>
    </div>
    """,
    unsafe_allow_html=True
)
