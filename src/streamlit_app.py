import streamlit as st
import os
import pickle
import numpy as np

# Set the port to 8080 (required for Cloud Run)
PORT = int(os.getenv("PORT", 8080))

# Load Model
MODEL_PATH = "model/model.pkl"
if not os.path.exists(MODEL_PATH):
    st.error("❌ Model file not found! Please train the model first.")
    st.stop()

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.set_page_config(page_title="Loan Approval Predictor", page_icon="🏦", layout="centered")
st.title("🏦 Loan Approval Predictor")
st.markdown("<p style='text-align: center; font-size: 18px;'>Fill in the details below to check your loan eligibility.</p>", unsafe_allow_html=True)

# Form Input Fields
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("👤 Gender", ["Male", "Female"])
    married = st.selectbox("💍 Married", ["No", "Yes"])
    education = st.selectbox("🎓 Education", ["Not Graduate", "Graduate"])
    self_employed = st.selectbox("🏢 Self Employed", ["No", "Yes"])
    dependents = st.selectbox("👶 Dependents", ["0", "1", "2", "3+"])

with col2:
    applicant_income = st.number_input("💰 Applicant Income", min_value=0)
    coapplicant_income = st.number_input("💵 Coapplicant Income", min_value=0)
    loan_amount = st.number_input("🏦 Loan Amount", min_value=0)
    loan_term = st.number_input("📆 Loan Term (Months)", min_value=0)
    credit_history = st.selectbox("📝 Credit History", [0, 1])
    property_area = st.selectbox("🏠 Property Area", ["Rural", "Semiurban", "Urban"])

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
    prediction = model.predict(np.array(data).reshape(1, -1))[0]
    if prediction == 1:
        st.success("✅ Congratulations! Your loan is Approved.")
    else:
        st.error("❌ Sorry! Your loan is Rejected.")

st.write(f"🚀 Running on Port {PORT}")
