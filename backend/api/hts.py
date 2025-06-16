from fastapi import APIRouter, HTTPException
from typing import Dict, Any
import requests
import os
import re
from utils.logger import setup_logger

# Initialize router
hts_router = APIRouter()

# Setup logger
logger = setup_logger(
    logging_enabled=os.getenv("LOGGING_ENABLED", "true").lower() == "true",
    debug_mode=os.getenv("DEBUG_MODE", "true").lower() == "true"
)

# USITC API Configuration
USITC_BASE_URL = "https://datawebws.usitc.gov/dataweb"
USITC_API_KEY = os.getenv("HTS_API_KEY")

def clean_hts_code(hts_code: str) -> str:
    """
    Clean and validate HTS code format.
    
    Args:
        hts_code (str): Raw HTS code input
        
    Returns:
        str: Cleaned HTS code (first 8 digits)
        
    Raises:
        HTTPException: If HTS code format is invalid
    """
    # Remove any dots and whitespace
    cleaned = re.sub(r'[.\s]', '', hts_code)
    
    # Validate it's a 10-digit number
    if not re.match(r'^\d{10}$', cleaned):
        raise HTTPException(
            status_code=400,
            detail="Invalid HTS code format. Must be 10 digits, optionally separated by dots (e.g., 1234567890 or 1234.56.78.90)"
        )
    
    # Return first 8 digits for API compatibility
    return cleaned[:8]

async def get_current_year() -> str:
    """
    Get the current tariff year from USITC API.
    
    Returns:
        str: Current tariff year
        
    Raises:
        HTTPException: If API call fails
    """
    try:
        headers = {"Authorization": f"Bearer {USITC_API_KEY}"}
        response = requests.get(
            f"{USITC_BASE_URL}/api/v2/tariff/currentTariffYear",
            headers=headers,
            verify=False  # As specified in the docs
        )
        response.raise_for_status()
        return response.json()["year"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to get current tariff year: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve current tariff year from USITC API"
        )

@hts_router.get("/search/{hts_code}")
async def search_hts_code(hts_code: str) -> Dict[str, Any]:
    """
    Search for HTS code information.
    
    Args:
        hts_code (str): The HTS code to search for (10 digits)
        
    Returns:
        Dict[str, Any]: HTS code information
        
    Raises:
        HTTPException: If the request fails or returns an error
    """
    if not USITC_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="USITC API key not configured. Please set HTS_API_KEY environment variable."
        )
    
    try:
        # Clean and validate HTS code
        hts8 = clean_hts_code(hts_code)
        logger.info(f"Searching for HTS code: {hts_code} (using first 8 digits: {hts8})")
        
        # Get current year
        year = await get_current_year()
        logger.info(f"Using tariff year: {year}")
        
        # Make request to USITC API
        headers = {"Authorization": f"Bearer {USITC_API_KEY}"}
        response = requests.get(
            f"{USITC_BASE_URL}/api/v2/tariff/currentTariffDetails",
            params={"year": year, "hts8": hts8},
            headers=headers,
            verify=False  # As specified in the docs
        )
        response.raise_for_status()
        
        # Return the tariff details
        return response.json()
        
    except HTTPException as e:
        # Re-raise HTTP exceptions
        raise
    except requests.exceptions.RequestException as e:
        logger.error(f"USITC API request failed: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to retrieve HTS code information: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Unexpected error while searching HTS code: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred while processing your request"
        ) 