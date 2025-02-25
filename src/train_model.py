import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Define paths
DATA_PATH = "./data/cleaned_data.csv"
MODEL_DIR = "./model"
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")

# Ensure necessary directories exist
os.makedirs(MODEL_DIR, exist_ok=True)

# Load cleaned data
def load_cleaned_data():
    if not os.path.exists(DATA_PATH):
        print(f"❌ Data file not found: {DATA_PATH}")
        print("📌 Please make sure the cleaned_data.csv file is present in the 'data' folder.")
        return None
    return pd.read_csv(DATA_PATH)

# Split Data
def split_data(df):
    y = df["Loan_Status"]
    X = df.drop(columns=["Loan_Status"])
    return train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
def train_model():
    df = load_cleaned_data()
    if df is None:  # Stop execution if data is missing
        return

    X_train, X_test, y_train, y_test = split_data(df)

    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("✅ Model Training Completed!")
    print("Accuracy:", accuracy_score(y_test, y_pred))

    # Save trained model
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    print(f"✅ Model saved at {MODEL_PATH}!")

if __name__ == "__main__":
    train_model()
