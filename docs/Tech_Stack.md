# Sifty_HTS Tech Stack

## Overview
This document outlines the technologies, frameworks, libraries, and tools used in the Sifty_HTS application.

## Core Technologies

### Backend
- **Language**: Python 3.11
- **Framework**: FastAPI
  - RESTful API endpoints
  - CORS middleware for frontend communication
  - Automatic API documentation (Swagger UI)
- **Dependencies**:
  - python-dotenv - Environment variable management
  - requests - HTTP client for API integration
  - uvicorn - ASGI server for FastAPI

### Frontend
- **Framework**: React
- **Styling**: Tailwind CSS (served via CDN)
- **Development**:
  - JSX for component creation
  - React DOM for rendering
  - Babel for JSX transpilation

### Containerization
- **Docker**
  - Python 3.11 slim base image
  - Multi-stage build for efficient deployment
  - Volume mounting for development
  - Live reloading configuration

## Development Environment

### Tools
- **Cursor** - Code editing and development
- **Vibecoding** - Development assistance
- **nodemon** - Frontend live reloading
- **uvicorn** - Backend live reloading

### Configuration
- **.env file** - Environment variables
  - API keys
  - Logging configuration
  - Debug mode settings
  - Port configuration

## External API Integrations

### Current Phase
- **HTS Code API** (US government)
  - Retrieval of tariff codes and related data
  - Authentication via API key

- **Federal Register API**
  - Document retrieval based on query parameters
  - Potential rate limiting considerations

### Future Phase
- **LLM API**
  - Document summarization
  - Content organization
  - Potential caching implementation

## Communication Flow
1. Frontend (React) <--> Backend (FastAPI) via HTTP/REST
2. Backend (FastAPI) <--> External APIs via HTTP/REST
3. External software <--> Backend (FastAPI) for integration

## System Requirements
- Docker-compatible host system
- Network connectivity to external APIs
- Sufficient memory for Docker container operation (minimum recommended: 2GB)

## Security Considerations
- API keys stored in .env file (not in source code)
- CORS configuration to restrict unauthorized origins
- Environment variable separation for development and production

## Future Technical Considerations
- Redis for API response caching
- User authentication implementation
- Enhanced logging and monitoring
- Performance optimization for large document sets 