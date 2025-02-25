# 🚀 Loan Approval App

This repository contains a Machine Learning-based Loan Approval Prediction application deployed on Google Cloud Platform (GCP) using Docker and Cloud Run. It also includes a CI/CD pipeline for automated deployment using GitHub Actions.

## ✨ Features
- 🎨 Streamlit-based UI for user interaction
- 🤖 Machine Learning model for loan approval prediction
- 🐳 Dockerized application for easy deployment
- ☁️ Google Cloud Run for serverless deployment
- 🔄 GitHub Actions for CI/CD automation

## 🔧 Prerequisites
Before starting, ensure you have the following installed:
- 🐳 [Docker](https://www.docker.com/get-started)
- ☁️ [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- 🔗 [Git](https://git-scm.com/downloads)
- 🐍 [Python 3.9+](https://www.python.org/downloads/)
- 🖥️ [VS Code (Optional)](https://code.visualstudio.com/)

## 🏗️ Project Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/akshayy-ai/loan-approval-app.git
   cd loan-approval-app
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🐳 Docker Setup & Deployment on GCP
1. Authenticate with GCP:
   ```bash
   gcloud auth login
   gcloud config set project [PROJECT_ID]
   ```
2. Enable required services:
   ```bash
   gcloud services enable run.googleapis.com artifactregistry.googleapis.com
   ```
3. Build and push the Docker image:
   ```bash
   docker build -t gcr.io/[PROJECT_ID]/loan-approval-app:latest .
   docker push gcr.io/[PROJECT_ID]/loan-approval-app:latest
   ```
4. Deploy to Cloud Run:
   ```bash
   gcloud run deploy loan-approval-app \
     --image gcr.io/[PROJECT_ID]/loan-approval-app:latest \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

## 🔄 CI/CD Automation with GitHub Actions
### 🔹 Setup
1. Create a new service account in GCP and grant `Cloud Run Admin` and `Artifact Registry Writer` roles.
2. Grant `iam.serviceAccounts.actAs` permission to the service account.
3. Generate a JSON key for the service account and add it as a GitHub secret (`GCP_CREDENTIALS`).

### 📜 GitHub Actions Workflow
The CI/CD workflow (`.github/workflows/deploy.yml`) automates the build and deployment process:
- ✅ On push to `main` branch, the workflow builds and pushes the Docker image.
- 🚀 It then deploys the new version to Cloud Run.

### 🔧 Adding the Workflow
1. Create a `.github/workflows/` directory:
   ```bash
   mkdir -p .github/workflows
   ```
2. Create a `deploy.yml` file inside `.github/workflows/` with the following content:
   ```yaml
   name: 🚀 Deploy to Cloud Run

   on:
     push:
       branches:
         - main

   jobs:
     deploy:
       runs-on: ubuntu-latest

       steps:
         - name: 🛠️ Checkout repository
           uses: actions/checkout@v3

         - name: 🔑 Authenticate with Google Cloud
           uses: google-github-actions/auth@v1
           with:
             credentials_json: '${{ secrets.GCP_CREDENTIALS }}'

         - name: 🐳 Configure Docker for Artifact Registry
           run: gcloud auth configure-docker gcr.io

         - name: 🔨 Build and push Docker image
           run: |
             docker build -t gcr.io/[PROJECT_ID]/loan-approval-app:latest .
             docker push gcr.io/[PROJECT_ID]/loan-approval-app:latest

         - name: 🚀 Deploy to Cloud Run
           run: |
             gcloud run deploy loan-approval-app \
               --image gcr.io/[PROJECT_ID]/loan-approval-app:latest \
               --platform managed \
               --region us-central1 \
               --allow-unauthenticated
   ```
3. Commit and push changes:
   ```bash
   git add .github/workflows/deploy.yml
   git commit -m "🚀 Added CI/CD workflow"
   git push origin main
   ```

## ⚠️ Troubleshooting & Fixes
During deployment, you may encounter permission errors. Here are the steps we followed to resolve them:
1. **🔴 Artifact Registry Permission Error:**
   - 🛑 Error: `Permission "artifactregistry.repositories.uploadArtifacts" denied`
   - ✅ Solution:
     - Go to **Google Cloud Console → IAM & Admin → IAM**.
     - Locate the service account used (`github-actions-deploy@[PROJECT_ID].iam.gserviceaccount.com`).
     - Assign `Artifact Registry Writer` role.

2. **🔴 Service Account IAM ActAs Permission Error:**
   - 🛑 Error: `Permission 'iam.serviceaccounts.actAs' denied`
   - ✅ Solution:
     - Go to **Google Cloud Console → IAM & Admin → IAM**.
     - Locate the service account (`github-actions-deploy@[PROJECT_ID].iam.gserviceaccount.com`).
     - Assign `Service Account User` role.

3. **🔄 Manually Re-running GitHub Actions Workflow:**
   - If a workflow fails, go to **GitHub → Actions**.
   - Select the failed workflow.
   - Click on "🔄 Re-run jobs" to manually restart the workflow.

## 🌍 Accessing the Application
Once deployed, you will receive a URL from Cloud Run. Open it in your browser to access the **Loan Approval App**.

## 📝 License
This project is licensed under the **MIT License**.

---
💡 **For any issues, feel free to open an issue or reach out!**

### 📞 Contact
👤 **Akshay Shitole**  
📧 Email: [theakshayway@gmail.com](mailto:theakshayway@gmail.com)  

