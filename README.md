# Sifty_HTS

A web application for retrieving Harmonized Tariff Schedule (HTS) code data and Federal Register documents.

## Features

- Retrieve HTS code data from US government API
- Search Federal Register documents
- User-friendly frontend interface
- RESTful API for integration with existing software
- Docker containerization with live reloading

## Tech Stack

- Backend: Python 3.11 with FastAPI
- Frontend: React with Tailwind CSS
- Containerization: Docker
- See [Tech Stack](docs/Tech_Stack.md) for detailed information

## Prerequisites

- Docker
- Docker Compose (optional)
- Python 3.11+ (for local development)
- Node.js (for local development)

## Setup

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

3. Build and run with Docker:
   ```bash
   docker build -t sifty-hts .
   docker run -p 7000:7000 -p 3000:3000 --env-file .env -v $(pwd):/app sifty-hts
   ```

## Development

### Backend (FastAPI)

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

### Frontend (React)

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

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[MIT License](LICENSE) 