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
app = FastAPI(
    title="Sifty_HTS API",
    description="API for retrieving HTS codes and Federal Register documents",
    version="1.0.0"
)

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
app.include_router(hts_router, prefix="/hts", tags=["HTS"])
app.include_router(federal_register_router, prefix="/federal-register", tags=["Federal Register"])

@app.get("/")
async def root():
    """Root endpoint for health check."""
    logger.info("Health check endpoint accessed")
    return {"message": "Sifty_HTS API is running"} 