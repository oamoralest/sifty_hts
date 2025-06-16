# Use official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Node.js for frontend
RUN apt-get update && apt-get install -y nodejs npm

# Copy backend requirements and install
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy frontend dependencies and install
COPY frontend/package.json frontend/
RUN cd frontend && npm install

# Copy all project files
COPY . .

# Expose ports (FastAPI: 7000, frontend: 3000)
EXPOSE 7000 3000

# Start backend and frontend with live reloading
CMD bash -c "cd backend && uvicorn main:app --host 0.0.0.0 --port 7000 --reload & cd frontend && npm start" 