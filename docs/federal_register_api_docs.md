# Federal Register API Documentation

## Overview

FederalRegister.gov provides multiple public API endpoints for accessing Federal Register documents and related data. The API is completely free and requires no API keys - all you need is an HTTP client or browser.

**Base URL:** `https://www.federalregister.gov/api/v1/`

## Important Legal Notice

⚠️ **LEGAL STATUS**: This API provides access to a prototype "Web 2.0" version of the daily Federal Register. It is NOT an official legal edition and does not replace the official print version or the official electronic version on GPO's govinfo.gov. For legal research, always verify results against an official edition of the Federal Register.

## API Endpoints

### Federal Register Documents

#### Get Single Document
```
GET /documents/{document_number}.{format}
```

Fetch a single Federal Register document by its document number.

**Parameters:**
- `document_number` (required, path): Federal Register document number
- `format` (required, path): Response format (json)
- `fields[]` (optional, query): Array of document attributes to return

**Example:**
```
GET /api/v1/documents/2024-12345.json
```

#### Get Multiple Documents
```
GET /documents/{document_numbers}.{format}
```

Fetch multiple Federal Register documents at once.

**Parameters:**
- `document_numbers` (required, path): Comma-separated array of Federal Register document numbers
- `format` (required, path): Response format (json)
- `fields[]` (optional, query): Array of document attributes to return

**Example:**
```
GET /api/v1/documents/2024-12345,2024-12346.json
```

#### Search Documents
```
GET /documents.{format}
```

Search all Federal Register documents published since 1994.

**Parameters:**
- `format` (required, path): Response format (json)
- `fields[]` (optional, query): Document attributes to return
- `per_page` (optional, query): Number of documents per page (max 1000, default 20)
- `page` (optional, query): Page number of results
- `order` (optional, query): Sort order (relevance, newest, oldest)

**Search Conditions:**
- `conditions[term]`: Full text search
- `conditions[publication_date][is]`: Exact publication date (YYYY-MM-DD)
- `conditions[publication_date][year]`: Documents from specific year (YYYY)
- `conditions[publication_date][gte]`: Documents on or after date (YYYY-MM-DD)
- `conditions[publication_date][lte]`: Documents on or before date (YYYY-MM-DD)
- `conditions[effective_date][is]`: Exact effective date (YYYY-MM-DD)
- `conditions[effective_date][year]`: Effective date in specific year (YYYY)
- `conditions[effective_date][gte]`: Effective date on or after (YYYY-MM-DD)
- `conditions[effective_date][lte]`: Effective date on or before (YYYY-MM-DD)
- `conditions[agencies][]`: Publishing agency (see Agency enum)
- `conditions[type][]`: Document type (RULE, PRORULE, NOTICE, PRESDOCU)
- `conditions[presidential_document_type][]`: Presidential document type
- `conditions[president][]`: Signing president
- `conditions[docket_id]`: Agency docket number
- `conditions[regulation_id_number]`: Regulation ID Number (RIN)
- `conditions[sections][]`: FederalRegister.gov section
- `conditions[topics][]`: Associated topics (CFR Indexing terms)
- `conditions[significant]`: Deemed significant under EO 12866 ("0" or "1")
- `conditions[cfr][title]`: CFR title number
- `conditions[cfr][part]`: CFR part or range (e.g., '17' or '1-50')
- `conditions[near][location]`: Location search (zipcode or City, State)
- `conditions[near][within]`: Max distance from location in miles (max 200)

**Example:**
```
GET /api/v1/documents.json?conditions[term]=climate&conditions[type][]=RULE&per_page=50
```

#### Get Document Facets
```
GET /documents/facets/{facet}
```

Get counts of matching documents grouped by a facet.

**Parameters:**
- `facet` (required, path): Grouping facet (daily, agencies, type, etc.)
- All search conditions from document search are supported

**Example:**
```
GET /api/v1/documents/facets/agencies.json?conditions[term]=healthcare
```

#### Get Issue Table of Contents
```
GET /issues/{publication_date}.{format}
```

Fetch document table of contents for a specific publication date.

**Parameters:**
- `publication_date` (required, path): Publication date (YYYY-MM-DD)
- `format` (required, path): Response format (json)

**Example:**
```
GET /api/v1/issues/2024-06-10.json
```

### Public Inspection Documents

#### Get Single Public Inspection Document
```
GET /public-inspection-documents/{document_number}.{format}
```

**Parameters:**
- `document_number` (required, path): Federal Register document number
- `format` (required, path): Response format (json)

#### Get Multiple Public Inspection Documents
```
GET /public-inspection-documents/{document_numbers}.{format}
```

**Parameters:**
- `document_numbers` (required, path): Comma-separated document numbers
- `format` (required, path): Response format (json)

#### Get Current Public Inspection Documents
```
GET /public-inspection-documents/current.{format}
```

Fetch all documents currently on public inspection.

**Parameters:**
- `format` (required, path): Response format (json)

#### Search Public Inspection Documents
```
GET /public-inspection-documents.{format}
```

Search documents currently on public inspection.

**Parameters:**
- `format` (required, path): Response format (json)
- `fields[]` (optional, query): Document attributes to return
- `per_page` (optional, query): Documents per page (max 1000, default 20)
- `page` (optional, query): Page number
- `conditions[available_on]` (required): Public inspection issue date (YYYY-MM-DD)
- `conditions[term]`: Full text search
- `conditions[agencies][]`: Publishing agency
- `conditions[type][]`: Document type (RULE, PRORULE, NOTICE, PRESDOCU)
- `conditions[special_filing]`: Filing type ("0" for regular, "1" for special)
- `conditions[docket_id]`: Agency docket number

### Agencies

#### Get All Agencies
```
GET /agencies
```

Fetch details for all agencies.

#### Get Specific Agency
```
GET /agencies/{slug}
```

**Parameters:**
- `slug` (required, path): Federal Register slug for the agency
- `id` (optional, query, deprecated): Federal Register ID for the agency

### Images

#### Get Image Metadata
```
GET /images/{identifier}
```

Fetch available image variants and metadata.

**Parameters:**
- `identifier` (required, path): Federal Register image identifier

### Suggested Searches

#### Get All Suggested Searches
```
GET /suggested_searches
```

**Parameters:**
- `conditions[sections]` (optional, query): Limit by FederalRegister.gov section

#### Get Specific Suggested Search
```
GET /suggested_searches/{slug}
```

**Parameters:**
- `slug` (required, path): Federal Register slug for the suggested search

## Document Types

- **RULE**: Final Rule
- **PRORULE**: Proposed Rule  
- **NOTICE**: Notice
- **PRESDOCU**: Presidential Document

## Presidential Document Types

- `determination`
- `executive_order`
- `memorandum`
- `notice`
- `proclamation`
- `other`

## Presidents (for Presidential Documents)

- `william-j-clinton`
- `george-w-bush`
- `barack-obama`
- `donald-trump`
- `joseph-r-biden`

## Section Categories

- `business-and-industry`
- `environment`
- `health-and-public-welfare`
- And many more...

## Common Agency Slugs

- `action`
- `administration-office-executive-office-of-the-president`
- `administrative-conference-of-the-united-states`
- `administrative-office-of-united-states-courts`
- And many more (466 total agencies available)

## Response Format

All API responses return JSON by default. The structure includes:

```json
{
  "results": [...],
  "count": 123,
  "total_pages": 5,
  "current_page": 1,
  // ... other metadata
}
```

## Rate Limits

No explicit rate limits are documented, but use reasonable request patterns to avoid overwhelming the service.

## Error Responses

- **200**: Success
- **404**: Not Found (for specific resource endpoints)

## Tips for Usage

1. Use the `fields[]` parameter to limit response size by requesting only needed attributes
2. For large date ranges with daily faceting, limit your request scope
3. Location searches support zipcode or "City, State" format
4. CFR part searches can use ranges like "1-50"
5. Maximum of 1000 documents per page
6. Full text search supports the `conditions[term]` parameter
7. Always verify legal research against official Federal Register editions

## Example API Calls

### Search for EPA rules about climate change published in 2024
```
GET /api/v1/documents.json?conditions[term]=climate&conditions[agencies][]=environmental-protection-agency&conditions[type][]=RULE&conditions[publication_date][year]=2024
```

### Get document counts by agency for healthcare-related documents
```
GET /api/v1/documents/facets/agencies.json?conditions[term]=healthcare
```

### Find documents effective in the next 30 days
```
GET /api/v1/documents.json?conditions[effective_date][gte]=2024-06-10&conditions[effective_date][lte]=2024-07-10
```