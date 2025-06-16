# Environment Variables Configuration

This document describes all the environment variables used in the Sifty_HTS application. Copy these variables to a `.env` file in the root directory of the project.

## Example `.env` File

```env
# API Keys
# Required for accessing the US government HTS API
HTS_API_KEY=your_hts_api_key_here

# Backend Configuration
BACKEND_PORT=7000
BACKEND_HOST=0.0.0.0
BACKEND_DEBUG=true

# Frontend Configuration
FRONTEND_PORT=3000
REACT_APP_API_URL=http://localhost:7000  # Backend API URL for frontend to use

# Development Settings
LOGGING_ENABLED=true
DEBUG_MODE=true
NODE_ENV=development
PYTHONDONTWRITEBYTECODE=1  # Prevents Python from writing .pyc files
PYTHONUNBUFFERED=1         # Prevents Python from buffering stdout and stderr

# CORS Settings (comma-separated if multiple)
ALLOWED_ORIGINS=http://localhost:3000

# Federal Register API Configuration
FEDERAL_REGISTER_BASE_URL=https://www.federalregister.gov/api/v1

# Future LLM Integration (uncomment when needed)
# LLM_API_KEY=your_llm_api_key_here
# LLM_MODEL=your_model_name
# LLM_MAX_TOKENS=100

# Security Settings
# Generate a secure key: Run 'openssl rand -hex 32' in terminal
API_SECRET_KEY=your_secure_secret_key_here

# Rate Limiting
MAX_REQUESTS_PER_MINUTE=100
```

## Variable Descriptions

### API Keys
- `HTS_API_KEY`: Your API key for the US government HTS API

### Backend Configuration
- `BACKEND_PORT`: Port number for the FastAPI backend (default: 7000)
- `BACKEND_HOST`: Host address for the backend (default: 0.0.0.0)
- `BACKEND_DEBUG`: Enable/disable debug mode for the backend

### Frontend Configuration
- `FRONTEND_PORT`: Port number for the React frontend (default: 3000)
- `REACT_APP_API_URL`: URL where the frontend can reach the backend API

### Development Settings
- `LOGGING_ENABLED`: Enable/disable application logging
- `DEBUG_MODE`: Enable/disable debug mode
- `NODE_ENV`: Node.js environment (development/production)
- `PYTHONDONTWRITEBYTECODE`: Prevent Python from creating .pyc files
- `PYTHONUNBUFFERED`: Ensure Python output is sent straight to terminal

### CORS Settings
- `ALLOWED_ORIGINS`: List of origins allowed to access the API

### Federal Register API Configuration
- `FEDERAL_REGISTER_BASE_URL`: Base URL for the Federal Register API (public API, no key required)

### Future LLM Integration
- `LLM_API_KEY`: API key for the LLM service (future use)
- `LLM_MODEL`: Model name for LLM service
- `LLM_MAX_TOKENS`: Maximum tokens for LLM responses

### Security Settings
- `API_SECRET_KEY`: Secret key for API security (JWT, etc.)

### Rate Limiting
- `MAX_REQUESTS_PER_MINUTE`: Maximum API requests allowed per minute

## Setting Up Your Environment

1. Create a new `.env` file in the root directory:
   ```bash
   cp .env.example .env
   ```

2. Replace the placeholder values with your actual configuration:
   - Get your HTS API key from the US government
   - Generate a secure API secret key:
     ```bash
     openssl rand -hex 32
     ```

3. Adjust other values as needed for your development environment

## Notes

- Never commit the `.env` file to version control
- Keep your API keys secure
- In production, use more restrictive settings for security
- The LLM integration variables are prepared for future use
- Make sure the ports you specify are available on your system
- The Federal Register API is public and does not require authentication 