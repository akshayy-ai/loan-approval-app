# Loan Approval Prediction App

A machine learning-based loan approval prediction system deployed using **Streamlit**, **Docker**, and **Google Cloud Platform (GCP)**.

## 🛠 Tech Stack
- **Python** (Pandas, NumPy, Scikit-learn, Streamlit)
- **Docker**
- **Google Cloud Run**
- **GitHub Actions (CI/CD)**

## 📌 Features
- Train a machine learning model for loan approval.
- Deploy using **Docker** and **Google Cloud Run**.
- Automate deployments with **GitHub Actions**.

---

## 🚀 Setup Instructions

### 1️⃣ Local Setup

#### **Clone the Repository**
```sh
git clone https://github.com/your-username/loan-approval-app.git
cd loan-approval-app
```

#### **Create Virtual Environment & Install Dependencies**
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### **Train the Model**
```sh
python train_model.py
```

#### **Run Streamlit App Locally**
```sh
streamlit run src/streamlit_app.py --server.port=8080
```
App will be available at: **http://localhost:8080**

---

## 🐳 Dockerization

### 2️⃣ Build & Run Docker Container

#### **Build Docker Image**
```sh
docker build -t loan-approval-app .
```

#### **Run Container**
```sh
docker run -p 8080:8080 loan-approval-app
```
App will be accessible at: **http://localhost:8080**

---

## ☁️ Deploy on Google Cloud Run

### 3️⃣ Google Cloud Setup

#### **Authenticate with Google Cloud**
```sh
gcloud auth login
```

#### **Set Project & Enable Cloud Run API**
```sh
gcloud config set project YOUR_PROJECT_ID
gcloud services enable run.googleapis.com
```

#### **Build & Push Docker Image to Google Container Registry (GCR)**
```sh
docker tag loan-approval-app gcr.io/YOUR_PROJECT_ID/loan-approval-app:v1
docker push gcr.io/YOUR_PROJECT_ID/loan-approval-app:v1
```

#### **Deploy to Cloud Run**
```sh
gcloud run deploy loan-approval-app \
    --image gcr.io/YOUR_PROJECT_ID/loan-approval-app:v1 \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --port 8080
```
After deployment, the service URL will be displayed. Use it to access your app.

---

## ⚡ Automate with GitHub Actions (CI/CD)

### 4️⃣ Set Up GitHub Actions for Continuous Deployment

#### **Create `.github/workflows/deploy.yml`**
```yaml
name: Deploy to Cloud Run

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3
      
      - name: Authenticate with GCP
        uses: google-github-actions/auth@v1
        with:
          credentials_json: ${{ secrets.GCP_SERVICE_ACCOUNT_KEY }}

      - name: Build & Push Docker Image
        run: |
          gcloud auth configure-docker
          docker build -t gcr.io/YOUR_PROJECT_ID/loan-approval-app:v1 .
          docker push gcr.io/YOUR_PROJECT_ID/loan-approval-app:v1

      - name: Deploy to Cloud Run
        run: |
          gcloud run deploy loan-approval-app \
            --image gcr.io/YOUR_PROJECT_ID/loan-approval-app:v1 \
            --platform managed \
            --region us-central1 \
            --allow-unauthenticated \
            --port 8080
```

#### **GitHub Secrets to Add**
- `GCP_SERVICE_ACCOUNT_KEY` (JSON key of your GCP service account)

Once you push changes to **main**, GitHub Actions will **automatically deploy** your app to Cloud Run. 🚀

---

## 📌 Notes
- Ensure **PORT=8080** is set in `Dockerfile` and Cloud Run deployment.
- Use `gcloud auth configure-docker` before pushing images to GCR.
- Check Cloud Run logs if the deployment fails: `gcloud logs read --format=json`

---

## 📞 Support
If you face any issues, feel free to open an **Issue** or reach out. 😊

