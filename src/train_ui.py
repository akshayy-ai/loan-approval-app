import streamlit as st
import os
import subprocess

# Define model path
MODEL_PATH = "./model/model.pkl"

# Streamlit UI
st.title("Loan Approval Model Training")

# Check if model exists
model_exists = os.path.exists(MODEL_PATH)

if model_exists:
    st.success("✅ Trained Model Found! Ready to use.")
else:
    st.warning("⚠ No trained model found. Please train it first.")

# Train model button (only if model doesn't exist)
if not model_exists:
    if st.button("🚀 Train Model Now"):
        st.write("📢 Training started... Please wait.")
        
        # Run train_model.py as a subprocess
        process = subprocess.run(["python", "train_model.py"], capture_output=True, text=True)
        
        # Show output
        if process.returncode == 0:
            st.success("✅ Model trained and saved successfully!")
        else:
            st.error("❌ Error during training. Check logs below.")
            st.code(process.stderr)  # Show error logs
