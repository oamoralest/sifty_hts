# Use official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Node.js and npm
RUN apt-get update && \
    apt-get install -y nodejs npm && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install nodemon globally for frontend hot reloading
RUN npm install -g nodemon

# Copy requirements first to leverage Docker cache
COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy package.json first to leverage Docker cache
COPY frontend/package.json ./frontend/
RUN cd frontend && npm install

# We'll mount the rest of the code as volumes in docker-compose
# This is just a placeholder for production builds
COPY . .

# Expose ports
EXPOSE 8080 3000

# The actual run command will be in docker-compose.yml
CMD ["echo", "Please use docker-compose for development"] 