from fastapi import APIRouter, HTTPException, Query
from typing import Dict, Any, List, Optional
import requests
import os
from datetime import datetime, timedelta
from utils.logger import setup_logger

# Initialize router
federal_register_router = APIRouter()

# Setup logger
logger = setup_logger(
    logging_enabled=os.getenv("LOGGING_ENABLED", "true").lower() == "true",
    debug_mode=os.getenv("DEBUG_MODE", "true").lower() == "true"
)

# Get base URL from environment or use default
BASE_URL = os.getenv("FEDERAL_REGISTER_BASE_URL", "https://www.federalregister.gov/api/v1")

@federal_register_router.get("/search")
async def search_documents(
    query: str = Query(..., description="Search query for Federal Register documents"),
    document_type: Optional[str] = Query(None, description="Document type (RULE, PRORULE, NOTICE, PRESDOCU)"),
    agency: Optional[str] = Query(None, description="Publishing agency"),
    publication_date_start: Optional[str] = Query(None, description="Start date (YYYY-MM-DD)"),
    publication_date_end: Optional[str] = Query(None, description="End date (YYYY-MM-DD)"),
    page: int = Query(1, ge=1, description="Page number"),
    per_page: int = Query(20, ge=1, le=1000, description="Results per page")
) -> Dict[str, Any]:
    """
    Search Federal Register documents with various filters.
    
    Args:
        query (str): Search term
        document_type (str, optional): Type of document
        agency (str, optional): Publishing agency
        publication_date_start (str, optional): Start date
        publication_date_end (str, optional): End date
        page (int): Page number for pagination
        per_page (int): Number of results per page
        
    Returns:
        Dict[str, Any]: List of matching documents and metadata
    """
    try:
        # Build search conditions
        conditions = {}
        
        if query:
            conditions["term"] = query
            
        if document_type:
            conditions["type"] = [document_type]
            
        if agency:
            conditions["agencies"] = [agency]
            
        if publication_date_start:
            conditions["publication_date"] = conditions.get("publication_date", {})
            conditions["publication_date"]["gte"] = publication_date_start
            
        if publication_date_end:
            conditions["publication_date"] = conditions.get("publication_date", {})
            conditions["publication_date"]["lte"] = publication_date_end

        # Build request parameters
        params = {
            "conditions": conditions,
            "per_page": per_page,
            "page": page,
            "order": "relevance"
        }

        # Make request to Federal Register API
        response = requests.get(
            f"{BASE_URL}/documents.json",
            params=params
        )
        
        # Check for successful response
        response.raise_for_status()
        
        # Log the successful request
        logger.info(f"Successfully fetched Federal Register documents for query: {query}")
        
        return response.json()

    except requests.RequestException as e:
        logger.error(f"Error fetching Federal Register documents: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching Federal Register documents: {str(e)}"
        )

@federal_register_router.get("/document/{document_number}")
async def get_document(
    document_number: str = Query(..., description="Federal Register document number")
) -> Dict[str, Any]:
    """
    Fetch a specific Federal Register document by its document number.
    
    Args:
        document_number (str): The document number to fetch
        
    Returns:
        Dict[str, Any]: Document details
    """
    try:
        # Make request to Federal Register API
        response = requests.get(
            f"{BASE_URL}/documents/{document_number}.json"
        )
        
        # Check for successful response
        response.raise_for_status()
        
        # Log the successful request
        logger.info(f"Successfully fetched Federal Register document: {document_number}")
        
        return response.json()

    except requests.RequestException as e:
        logger.error(f"Error fetching Federal Register document: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching Federal Register document: {str(e)}"
        ) 