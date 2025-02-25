# Use official Python image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy requirement files first (for caching)
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project files (after dependencies are installed)
COPY . .

# Ensure model training if missing
RUN if [ ! -f "model/model.pkl" ]; then python train_model.py; else echo "Model already exists, skipping training."; fi

# Expose Cloud Run-compatible port
EXPOSE 8080

# Run Streamlit on Cloud Run-compatible port (8080)
CMD ["streamlit", "run", "src/streamlit_app.py", "--server.port=8080", "--server.address=0.0.0.0"]
