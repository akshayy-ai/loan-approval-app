import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def preprocess_data(df):
    # Drop Loan_ID (not useful for prediction)
    df.drop(columns=["Loan_ID"], inplace=True)

    # Convert categorical values to numerical
    df.replace({
        "Loan_Status": {'N': 0, 'Y': 1},
        "Gender": {'Male': 0, 'Female': 1},
        "Education": {'Not Graduate': 0, 'Graduate': 1},
        "Married": {'No': 0, 'Yes': 1},
        "Self_Employed": {'No': 0, 'Yes': 1}
    }, inplace=True)

    # Fill missing values in numerical columns only
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    # One-hot encoding for categorical columns
    df = pd.get_dummies(df, columns=["Property_Area", "Dependents"])

    return df

if __name__ == "__main__":
    df = load_data("./data/Finance.csv")
    df = preprocess_data(df)

    # Save cleaned data
    df.to_csv("./data/cleaned_data.csv", index=False)
    print("✅ Cleaned data saved as `cleaned_data.csv`!")
