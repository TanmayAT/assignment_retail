# Use official Python image
FROM python:3.10-slim

# Install essential system dependencies (for numpy, pandas, pyarrow)
RUN apt-get update && apt-get install -y build-essential gcc && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy your requirements.txt (you MUST keep it ready in same folder)
COPY req.txt .

# Install dependencies with fixed versions (avoiding numpy 2.x crash)
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r req.txt

# Copy rest of your app files (adjust if needed)
COPY . .

# Expose port (same as your uvicorn port)
EXPOSE 8002

# Run the FastAPI app using Uvicorn (adjust if your app file or variable is different)
CMD ["uvicorn", "model_api_response:app", "--host", "0.0.0.0", "--port", "8002", "--reload"]
