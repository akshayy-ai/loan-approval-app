import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os

# Load the trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "./model/model.pkl")

if not os.path.exists(MODEL_PATH):
    st.error(f"❌ Model file not found at {MODEL_PATH}. Please train the model first.")
    st.stop()

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/5047/5047028.png", width=100)
st.sidebar.title("🏦 Loan Approval Predictor")

st.write("### 🏠 Loan Approval Prediction App")
st.write("Fill in the details below to check loan eligibility.")

# User input fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])
applicant_income = st.number_input("Applicant Income ($)", min_value=1000, step=500)
coapplicant_income = st.number_input("Coapplicant Income ($)", min_value=0, step=500)
loan_amount = st.number_input("Loan Amount ($)", min_value=5000, step=1000)
loan_term = st.selectbox("Loan Term (Months)", [360, 180, 120, 60])
credit_history = st.selectbox("Credit History", [1, 0])
property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

# Convert user inputs to a DataFrame
input_data = pd.DataFrame({
    "Gender": [1 if gender == "Male" else 0],
    "Married": [1 if married == "Yes" else 0],
    "Dependents": [0 if dependents == "0" else (1 if dependents == "1" else (2 if dependents == "2" else 3))],
    "Education": [1 if education == "Graduate" else 0],
    "Self_Employed": [1 if self_employed == "Yes" else 0],
    "ApplicantIncome": [applicant_income],
    "CoapplicantIncome": [coapplicant_income],
    "LoanAmount": [loan_amount],
    "Loan_Amount_Term": [loan_term],
    "Credit_History": [credit_history],
    "Property_Area": [0 if property_area == "Rural" else (1 if property_area == "Semiurban" else 2)]
})

# Predict the loan approval status
if st.button("Check Loan Eligibility"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("✅ Congratulations! Your loan is **approved**.")
    else:
        st.error("❌ Sorry, your loan **is not approved**.")

st.sidebar.write("📌 This tool uses a Machine Learning model to predict loan approval based on applicant details.")
st.sidebar.write("🔹 Created by **Akshay Shitole** 🚀")
