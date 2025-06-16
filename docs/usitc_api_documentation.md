# USITC DataWeb API Reference

## Overview

The United States International Trade Commission (USITC) DataWeb API allows users with API credentials to bypass the web application and send queries directly to the API. The DataWeb API is tool-agnostic and compatible with any HTTP-capable tools.

## Prerequisites

- Python 3.x with Pandas and Requests libraries installed
- An active DataWeb account with API key
- API credentials obtained from the API tab in DataWeb (requires login)

## Getting Started

### Base Configuration

```python
import pandas as pd
import requests

# Configuration
token = '[Get your token from the API tab in Dataweb (requires login)]'
baseUrl = 'https://datawebws.usitc.gov/dataweb'
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer " + token
}
requests.packages.urllib3.disable_warnings()
```

### Important Notes

- A "Dataweb is in data load mode" error appears while new data is being loaded - the API is unavailable during this period
- Not all manual updates to queries can be processed by the API
- If you encounter problems, consider creating a saved query in the DataWeb application

## Core API Endpoints

### Primary Query Endpoint
- **URL**: `POST /api/v2/report2/runReport`
- **Purpose**: Execute data queries and retrieve results

### Saved Queries
- **URL**: `GET /api/v2/savedQuery/getAllSavedQueries`
- **Purpose**: Retrieve all saved queries for the authenticated user

## Query Structure

### Basic Query Template

```json
{
  "savedQueryName": "",
  "savedQueryDesc": "",
  "isOwner": true,
  "runMonthly": false,
  "reportOptions": {
    "tradeType": "Import",
    "classificationSystem": "HTS"
  },
  "searchOptions": {
    "MiscGroup": {
      "districts": {
        "aggregation": "Aggregate District",
        "districtGroups": {"userGroups": []},
        "districts": [],
        "districtsExpanded": [{"name": "All Districts", "value": "all"}],
        "districtsSelectType": "all"
      },
      "importPrograms": {
        "aggregation": null,
        "importPrograms": [],
        "programsSelectType": "all"
      },
      "extImportPrograms": {
        "aggregation": "Aggregate CSC",
        "extImportPrograms": [],
        "extImportProgramsExpanded": [],
        "programsSelectType": "all"
      },
      "provisionCodes": {
        "aggregation": "Aggregate RPCODE",
        "provisionCodesSelectType": "all",
        "rateProvisionCodes": [],
        "rateProvisionCodesExpanded": []
      }
    },
    "commodities": {
      "aggregation": "Aggregate Commodities",
      "codeDisplayFormat": "YES",
      "commodities": [],
      "commoditiesExpanded": [],
      "commoditiesManual": "",
      "commodityGroups": {"systemGroups": [], "userGroups": []},
      "commoditySelectType": "all",
      "granularity": "2",
      "groupGranularity": null,
      "searchGranularity": null
    },
    "componentSettings": {
      "dataToReport": ["CONS_FIR_UNIT_QUANT"],
      "scale": "1",
      "timeframeSelectType": "fullYears",
      "years": ["2022", "2023"],
      "startDate": null,
      "endDate": null,
      "startMonth": null,
      "endMonth": null,
      "yearsTimeline": "Annual"
    },
    "countries": {
      "aggregation": "Aggregate Countries",
      "countries": [],
      "countriesExpanded": [{"name": "All Countries", "value": "all"}],
      "countriesSelectType": "all",
      "countryGroups": {"systemGroups": [], "userGroups": []}
    }
  },
  "sortingAndDataFormat": {
    "DataSort": {
      "columnOrder": [],
      "fullColumnOrder": [],
      "sortOrder": []
    },
    "reportCustomizations": {
      "exportCombineTables": false,
      "showAllSubtotal": true,
      "subtotalRecords": "",
      "totalRecords": "20000",
      "exportRawData": false
    }
  }
}
```

## Step-by-Step Query Configuration

### Step 1: Trade Flow and Classification System

#### Trade Flow Options
- **Import**: Imports for Consumption
- **Export**: Domestic Exports
- **GenImp**: General Imports
- **TotExp**: Total Exports
- **Balance**: Trade Balance
- **ForeignExp**: Foreign Exports
- **ImpExp**: Imports and Exports

#### Classification System Options
- **QUICK**: Quick Query
- **HTS**: HTS Items
- **SIC**: SIC Codes (1989-2001)
- **SITC**: SITC Codes
- **NAIC**: NAICS Codes (1997-present)
- **EXPERT**: Expert Mode

```python
query['reportOptions']['tradeType'] = 'Import'
query['reportOptions']['classificationSystem'] = 'HTS'
```

### Step 2: Data and Years

#### Full Years Selection
```python
query['searchOptions']['componentSettings']['timeframeSelectType'] = 'fullYears'
query['searchOptions']['componentSettings']['years'] = ['2020', '2021', '2022']
query['searchOptions']['componentSettings']['yearsTimeline'] = 'Annual'  # or 'Monthly'
```

#### Specific Date Range
```python
query['searchOptions']['componentSettings']['startDate'] = '06/2023'
query['searchOptions']['componentSettings']['endDate'] = '10/2023'
query['searchOptions']['componentSettings']['timeframeSelectType'] = 'specificDateRange'
query['searchOptions']['componentSettings']['yearsTimeline'] = 'Monthly'
```

### Step 3: Countries

#### Get All Countries
```python
response = requests.get(f"{baseUrl}/api/v2/country/getAllCountries", 
                       headers=headers, verify=False)
countries = response.json()['options']
```

#### Select Individual Countries
```python
selected_countries = [countries[1], countries[4]]  # Select by index
query['searchOptions']['countries']['countries'] = [x['value'] for x in selected_countries]
```

#### Get User's Saved Country Groups
```python
response = requests.get(f"{baseUrl}/api/v2/country/getAllUserGroupsWithCountries", 
                       headers=headers, verify=False)
country_groups = response.json()['options']
```

#### Aggregation Options
```python
query['searchOptions']['countries']['aggregation'] = 'Breakdown'  # or 'Aggregate Countries'
```

### Step 4: Commodities

#### Get System-Managed Commodity Groups
```python
options = {'tradeType': "Import", 'classificationSystem': "HTS", 'timeframe': "2023"}
response = requests.post(f"{baseUrl}/api/v2/commodity/getAllSystemGroupsWithCommodities",
                        headers=headers, json=options, verify=False)
```

#### Get User-Saved Commodity Groups
```python
response = requests.post(f"{baseUrl}/api/v2/commodity/getAllUserGroupsWithCommodities",
                        headers=headers, json=options, verify=False)
```

### Step 5: Programs (Import Only)

**Note**: Programs are only available for "Imports For Consumption" trade flow.

#### Get Import Programs
```python
response = requests.post(f"{baseUrl}/api/v2/query/getImportPrograms",
                        json={"tradeType": "Import"}, 
                        headers=headers, verify=False)
programs = response.json()['options']
```

#### Apply Programs to Query
```python
selected_programs = [programs[3]]  # Select desired programs
query['searchOptions']['MiscGroup']['extImportPrograms']['extImportPrograms'] = selected_programs
query['searchOptions']['MiscGroup']['extImportPrograms']['extImportProgramsExpanded'] = selected_programs
query['searchOptions']['MiscGroup']['extImportPrograms']['programsSelectType'] = 'manual'
query['searchOptions']['MiscGroup']['extImportPrograms']['aggregation'] = 'Breakdown'
```

### Step 6: Rate Provision Codes

#### Get Rate Provision Codes
```python
response = requests.post(f"{baseUrl}/api/v2/query/getRPCodesList",
                        headers=headers, 
                        json={"tradeType": "Import"}, 
                        verify=False)
rp_codes = response.json()['options']
```

#### Apply RP Codes to Query
```python
selected_rp_codes = [rp_codes[4]]
query['searchOptions']['MiscGroup']['provisionCodes']['provisionCodesSelectType'] = 'manual'
query['searchOptions']['MiscGroup']['provisionCodes']['rateProvisionCodes'] = selected_rp_codes
query['searchOptions']['MiscGroup']['provisionCodes']['rateProvisionCodesExpanded'] = selected_rp_codes
```

### Step 7: Districts

#### Get User-Saved District Groups
```python
response = requests.get(f"{baseUrl}/api/v2/district/getAllUserGroupsWithDistricts",
                       headers=headers, verify=False)
district_groups = response.json()
```

#### Get All Districts
```python
response = requests.get(f"{baseUrl}/api/v2/district/getAllDistricts",
                       headers=headers, verify=False)
districts = response.json()['options']
```

#### Apply Districts to Query
```python
selected_districts = [districts[0], districts[1]]
query['searchOptions']['MiscGroup']['districts']['districts'] = selected_districts
query['searchOptions']['MiscGroup']['districts']['districtsExpanded'] = selected_districts
query['searchOptions']['MiscGroup']['districts']['districtsSelectType'] = 'manual'
```

## Executing Queries

### Basic Query Execution
```python
response = requests.post(f"{baseUrl}/api/v2/report2/runReport",
                        headers=headers, 
                        json=query, 
                        verify=False)
```

### Data Processing Functions

#### Extract Column Names
```python
def getColumns(columnGroups, prevCols=None):
    if prevCols is None:
        columns = []
    else:
        columns = prevCols
    
    for group in columnGroups:
        if isinstance(group, dict) and 'columns' in group.keys():
            getColumns(group['columns'], columns)
        elif isinstance(group, dict) and 'label' in group.keys():
            columns.append(group['label'])
        elif isinstance(group, list):
            getColumns(group, columns)
    
    return columns
```

#### Extract Data Values
```python
def getData(dataGroups):
    data = []
    for row in dataGroups:
        rowData = []
        for field in row['rowEntries']:
            rowData.append(field['value'])
        data.append(rowData)
    return data
```

#### Complete Query Results Function
```python
def printQueryResults(headers, requestData):
    response = requests.post(f"{baseUrl}/api/v2/report2/runReport",
                           headers=headers, 
                           json=requestData, 
                           verify=False)
    
    columns = getColumns(response.json()['dto']['tables'][0]['column_groups'])
    data = getData(response.json()['dto']['tables'][0]['row_groups'][0]['row_groups'])
    df = pd.DataFrame(data, columns=columns)
    return df
```

## Swagger API Documentation Links

- **Run Report**: https://datawebws.usitc.gov/dataweb/swagger-ui/index.html#/Run%20Query/runReport
- **Get All Countries**: https://datawebws.usitc.gov/dataweb/swagger-ui/index.html#/Countries/getAllCountries
- **Get User's Country Groups**: https://datawebws.usitc.gov/dataweb/swagger-ui/index.html#/Countries/getAllUserGroupsWithCountries
- **Get System Commodity Groups**: https://datawebws.usitc.gov/dataweb/swagger-ui/index.html#/Commodities/getAllSystemGroupsWithCommodities
- **Get User Commodity Groups**: https://datawebws.usitc.gov/dataweb/swagger-ui/index.html#/Commodities/getAllUserGroupsWithCommodities
- **Get Import Programs**: https://datawebws.usitc.gov/dataweb/swagger-ui/index.html#/Query%20Info/getImportPrograms
- **Get Rate Provision Codes**: https://datawebws.usitc.gov/dataweb/swagger-ui/index.html#/Query%20Info/getRPCodesList
- **Get User District Groups**: https://datawebws.usitc.gov/dataweb/swagger-ui/index.html#/Districts/getAllUserGroupsWithDistricts
- **Get All Districts**: https://datawebws.usitc.gov/dataweb/swagger-ui/index.html#/Districts/getAllDistricts

## Debugging with Browser Developer Tools

### Using Firefox/Chrome Developer Tools

1. **Build Query**: Create your query using the DataWeb UI
2. **Open Developer Tools**: Right-click → "Inspect" → "Network" tab
3. **Execute Query**: Click "View Results" in DataWeb
4. **Find API Call**: Look for "runReport" POST request in Network tab
5. **Copy Payload**: View "Request"/"Payload" to see the exact JSON structure
6. **Use in Code**: Copy the request payload and use `json.loads()` in Python

### Example Usage
```python
import json

# Copy the payload from browser developer tools
browser_payload = '{"reportOptions":{"tradeType":"Import",...}}'
query = json.loads(browser_payload)

# Execute the query
response = requests.post(f"{baseUrl}/api/v2/report2/runReport",
                        headers=headers, 
                        json=query, 
                        verify=False)
```

## Common Data Fields

### Data to Report Options
- `CONS_FIR_UNIT_QUANT`: Consumption/First Unit Quantity
- Additional options available through the API documentation

### Scale Options
- `"1"`: No scaling
- Additional scaling options available

### Timeline Options
- `"Annual"`: Annual aggregation
- `"Monthly"`: Monthly breakdown

## Error Handling

- **Data Load Mode**: API returns error when DataWeb is updating data
- **Authentication**: Ensure Bearer token is valid and current
- **Query Validation**: Complex queries may require validation through DataWeb UI first
- **Rate Limiting**: Respect USITC terms of service for API usage