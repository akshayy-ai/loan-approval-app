import os

# Define project structure
project_structure = [
    "loan_prediction/data",
    "loan_prediction/src",
    "loan_prediction/.github/workflows"
]

# Define files to create
files = {
    "loan_prediction/src/data_preprocessing.py": "",
    "loan_prediction/src/train_model.py": "",
    "loan_prediction/src/predict.py": "",
    "loan_prediction/src/streamlit_app.py": "",
    "loan_prediction/.github/workflows/main.yml": "",
    "loan_prediction/requirements.txt": "pandas\nnumpy\nseaborn\nsklearn\nflask\nstreamlit\npickle-mixin",
    "loan_prediction/Dockerfile": """FROM python:3.8
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "src/predict.py"]""",
    "loan_prediction/README.md": "# Loan Prediction Project\n\nThis project predicts loan approvals using machine learning."
}

# Create directories
for folder in project_structure:
    os.makedirs(folder, exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(file_path, "w") as file:
        file.write(content)

print("✅ Project structure created successfully!")
