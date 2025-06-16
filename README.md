# Sifty_HTS

A web application for retrieving Harmonized Tariff Schedule (HTS) code data and Federal Register documents.

## Features

- Retrieve HTS code data from US government API
- Search Federal Register documents
- User-friendly frontend interface
- RESTful API for integration with existing software
- Docker containerization with live reloading for both frontend and backend

## Tech Stack

- Backend: Python 3.11 with FastAPI
- Frontend: React with Tailwind CSS
- Containerization: Docker
- See [Tech Stack](docs/Tech_Stack.md) for detailed information

## Prerequisites

- Docker
- Docker Compose
- Python 3.11+ (for local development without Docker)
- Node.js (for local development without Docker)

## Development Setup

### Using Docker (Recommended)

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd sifty-hts
   ```

2. Create a `.env` file:
   ```bash
   cp .env.example .env
   ```
   Update the environment variables with your API keys.

3. Start the development environment:
   ```bash
   docker-compose up
   ```

This will start both the backend and frontend with live reloading:
- Backend will be available at http://localhost:7000
- Frontend will be available at http://localhost:3000
- Any changes to the code will automatically trigger a reload

To rebuild the containers after adding new dependencies:
```bash
docker-compose up --build
```

To stop the containers:
```bash
docker-compose down
```

### Local Development (Without Docker)

#### Backend (FastAPI)

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # or
   .\venv\Scripts\activate  # Windows
   ```

2. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Run the backend:
   ```bash
   uvicorn main:app --reload --port 7000
   ```

#### Frontend (React)

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Start the development server:
   ```bash
   npm start
   ```

## API Documentation

Once the backend is running, visit:
- Swagger UI: http://localhost:7000/docs
- ReDoc: http://localhost:7000/redoc

## Development Notes

- The development environment is configured for hot reloading:
  - Backend: FastAPI with uvicorn's reload flag
  - Frontend: Create React App's hot module replacement
- Docker volumes are used to sync local changes with containers
- Python bytecode generation is disabled in containers to avoid permission issues
- Frontend hot reload is configured to work in Docker on all platforms

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[MIT License](LICENSE) 