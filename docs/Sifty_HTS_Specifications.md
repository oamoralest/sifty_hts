# Sifty_HTS App Specifications

## 1. Overview
**Sifty_HTS** is a web application designed to retrieve Harmonized Tariff Schedule (HTS) code data from the US government API and documents from the Federal Register API. It provides a user-friendly frontend for viewing results and a robust backend for integration with existing software. The app is built with Python for the backend, runs in a Docker container, and supports live reloading for development. Logging and debugging can be toggled via environment variables. Future phases will integrate an LLM API for summarizing and organizing Federal Register documents.

## 2. Objectives
- Retrieve and display HTS code data and Federal Register documents.
- Provide a backend API for integration with existing software.
- Offer a simplified frontend interface for viewing API results.
- Support live reloading in Docker for development efficiency.
- Enable configurable logging and debugging via .env file.
- Ensure well-commented code for ease of implementation.
- Plan for future LLM API integration for document summarization.

## 3. Technology Stack
- **Backend**: Python (FastAPI for RESTful API)
- **Frontend**: React with Tailwind CSS (served via CDN for simplicity)
- **Containerization**: Docker with live reloading
- **Configuration**: .env file for environment variables
- **APIs**:
  - HTS Code API (US government)
  - Federal Register API
  - Future: LLM API for summarization
- **Development Tools**: Cursor, Vibecoding

## 4. Functional Requirements
### 4.1. Core Features
- **API Integration**:
  - Fetch HTS code data from the US government API.
  - Retrieve documents from the Federal Register API.
  - Handle API authentication (if required) via environment variables.
- **Backend**:
  - Expose RESTful endpoints for HTS code and Federal Register data.
  - Support integration with existing software via API calls.
  - Implement error handling and data validation.
- **Frontend**:
  - Display HTS code data and Federal Register documents in a clean, tabular format.
  - Include search/filter functionality for results.
  - Responsive design using Tailwind CSS.
- **Docker**:
  - Run the app in a Docker container.
  - Support live reloading for backend (FastAPI) and frontend (React) changes.
- **Logging and Debugging**:
  - Configurable logging (enable/disable) via .env file.
  - Debug mode for detailed console/terminal output.
- **Future Phase**:
  - Integrate an LLM API to summarize and organize Federal Register documents.

### 4.2. Non-Functional Requirements
- **Performance**: Handle API responses within 2 seconds under normal conditions.
- **Scalability**: Backend should support multiple concurrent API requests.
- **Maintainability**: Code must include detailed comments for all functions, classes, and configuration files.
- **Security**: Store API keys securely in .env file, not in source code.
- **Compatibility**: Run on any system with Docker installed.

## 5. Architecture
### 5.1. System Components
- **Frontend (React)**:
  - Single-page application using JSX and Tailwind CSS.
  - Communicates with backend via RESTful API calls.
  - Displays HTS codes and Federal Register documents in tables/cards.
- **Backend (FastAPI)**:
  - Handles API requests to HTS and Federal Register APIs.
  - Exposes endpoints: `/hts` (HTS code data), `/federal-register` (documents).
  - Processes and formats API responses for frontend and external integration.
- **Docker**:
  - Single Dockerfile for backend and frontend.
  - Uses `nodemon` for frontend live reloading and `uvicorn` with `--reload` for backend.
- **Environment Configuration**:
  - .env file for API keys, logging, and debugging settings.
- **External APIs**:
  - HTS Code API: Retrieve tariff codes and related data.
  - Federal Register API: Fetch documents based on query parameters.

### 5.2. Data Flow
1. User interacts with frontend (e.g., submits HTS code or document query).
2. Frontend sends request to backend FastAPI server.
3. Backend fetches data from HTS or Federal Register API.
4. Backend processes and returns formatted data to frontend.
5. Frontend displays results in a user-friendly format.
6. Backend logs requests/responses if logging is enabled.
7. External software can query backend endpoints for integration.

## 6. File Structure
```
sifty_hts/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── api/
│   │   ├── hts.py          # HTS API logic
│   │   ├── federal_register.py # Federal Register API logic
│   ├── utils/
│   │   ├── logger.py       # Custom logging configuration
│   ├── requirements.txt    # Python dependencies
├── frontend/
│   ├── public/
│   │   ├── index.html      # React app entry point
│   ├── src/
│   │   ├── App.jsx         # Main React component
│   │   ├── components/     # Reusable React components
│   ├── package.json        # Node.js dependencies
├── Dockerfile              # Docker configuration
├── .env                    # Environment variables
├── README.md               # Project documentation
```

## 7. Sample Artifacts
### 7.1. Dockerfile
```dockerfile
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

# Expose ports (FastAPI: 8000, frontend: 3000)
EXPOSE 8000 3000

# Start backend and frontend with live reloading
CMD bash -c "cd backend && uvicorn main:app --host 0.0.0.0 --port 8000 --reload & cd frontend && npm start"
```

### 7.2. Sample .env File
```plaintext
# API keys
HTS_API_KEY=your_hts_api_key_here
FEDERAL_REGISTER_API_KEY=your_federal_register_api_key_here

# Logging and debugging
LOGGING_ENABLED=true
DEBUG_MODE=true

# Backend and frontend ports
BACKEND_PORT=8000
FRONTEND_PORT=3000
```

### 7.3. Sample Backend Code (main.py)
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from api.hts import hts_router
from api.federal_register import federal_register_router
from utils.logger import setup_logger

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Configure CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup logger based on .env configuration
logger = setup_logger(
    logging_enabled=os.getenv("LOGGING_ENABLED", "true").lower() == "true",
    debug_mode=os.getenv("DEBUG_MODE", "true").lower() == "true"
)

# Include API routers
app.include_router(hts_router, prefix="/hts")
app.include_router(federal_register_router, prefix="/federal-register")

@app.get("/")
async def root():
    """Root endpoint for health check."""
    logger.info("Health check endpoint accessed")
    return {"message": "Sifty_HTS API is running"}
```

### 7.4. Sample Logger (logger.py)
```python
import logging

def setup_logger(logging_enabled: bool, debug_mode: bool):
    """
    Configure logger based on environment variables.
    
    Args:
        logging_enabled (bool): Enable/disable logging.
        debug_mode (bool): Enable/disable debug-level logging.
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger("Sifty_HTS")
    logger.setLevel(logging.DEBUG if debug_mode else logging.INFO)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if debug_mode else logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    
    # Add handler only if logging is enabled
    if logging_enabled:
        logger.addHandler(console_handler)
    
    return logger
```

### 7.5. Sample Frontend (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sifty_HTS</title>
    <script src="https://cdn.jsdelivr.net/npm/react@18/umd/react.development.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/react-dom@18/umd/react-dom.development.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@babel/standalone/babel.min.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
    <div id="root"></div>
    <script type="text/babel">
        // Main React app
        function App() {
            return (
                <div className="container mx-auto p-4">
                    <h1 className="text-3xl font-bold">Sifty_HTS</h1>
                    <p className="mt-2">Retrieve HTS codes and Federal Register documents</p>
                    {/* Add components for HTS and Federal Register data */}
                </div>
            );
        }

        ReactDOM.render(<App />, document.getElementById('root'));
    </script>
</body>
</html>
```

## 8. Development Considerations
- **Live Reloading**:
  - Backend: Use `uvicorn --reload` for automatic restarts on code changes.
  - Frontend: Use `npm start` with Create React App for hot reloading.
- **API Integration**:
  - Ensure API keys are stored in .env and loaded securely.
  - Handle rate limits and errors gracefully (e.g., retries, fallbacks).
- **Logging/Debugging**:
  - Controlled via `LOGGING_ENABLED` and `DEBUG_MODE` in .env.
  - Logs output to terminal (backend) and console (frontend).
- **Code Comments**:
  - Include docstrings for all Python functions/classes.
  - Comment key logic blocks in React components.
- **Future LLM Integration**:
  - Plan for an `/llm-summarize` endpoint in the backend.
  - Store LLM API key in .env.
  - Cache summarized results to reduce API costs.

## 9. Setup Instructions
1. Clone the repository.
2. Create a `.env` file based on the sample provided.
3. Build and run the Docker container:
   ```bash
   docker build -t sifty_hts .
   docker run -p 8000:8000 -p 3000:3000 --env-file .env -v $(pwd):/app sifty_hts
   ```
4. Access the frontend at `http://localhost:3000` and backend at `http://localhost:8000`.

## 10. Future Enhancements
- **Phase 2**: Integrate LLM API for document summarization.
- **Phase 3**: Add user authentication for secure access.
- **Phase 4**: Implement caching (e.g., Redis) for frequent API queries.