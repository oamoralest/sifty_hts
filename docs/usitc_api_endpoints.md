# USITC Dataweb API Reference

## Overview

The USITC Dataweb API provides access to public trade data through various endpoints. Some endpoints require an API token which can be generated from the Dataweb application at https://dataweb.usitc.com/api-key (requires login).

**Base URL:** `https://datawebws.usitc.gov/dataweb`  
**API Version:** v0.0.1  
**Authentication:** Bearer token (JWT) or API key

## Authentication

To use endpoints that require authentication:
1. Generate an API token from https://dataweb.usitc.com/api-key
2. Include the token in the Authorization header: `Bearer YOUR_TOKEN`

---

## Endpoints by Category

### 🏷️ Tariffs

#### Get Tariff Summary Details
- **Endpoint:** `POST /api/v2/tariff/tariffSummaryDetails`
- **Description:** Returns a list of countries for a given tariff group code
- **Request Body:** `TariffSummaryRequest`
- **Response:** Array of `TariffSummaryDetails`

#### Get Tariff Summary Counts  
- **Endpoint:** `POST /api/v2/tariff/tariffSummaryCounts`
- **Description:** Returns a list of countries for a given tariff group code
- **Request Body:** `TariffSummaryRequest`
- **Response:** `TariffSummaryTableCounts`

#### Get Tariff Program (Single)
- **Endpoint:** `POST /api/v2/tariff/tariffProgramSingle`
- **Description:** Returns a list of countries for a given tariff group code
- **Request Body:** `TariffProgramRequest`
- **Response:** `TariffProgramResponse`

#### Get NAFTA/USMCA Details
- **Endpoint:** `POST /api/v2/tariff/getNaftaUSMCADetails`
- **Description:** Returns a list of countries for a given tariff group code
- **Request Body:** `TariffSummaryRequest`
- **Response:** Array of `NaftaUSMCADetails`

#### Get Future Tariff Agreement (Single)
- **Endpoint:** `POST /api/v2/tariff/futureTariffAgreementSingle`
- **Description:** Returns tariff information for a given country and commodity ID (HTS number)
- **Request Body:** `TariffRequest`
- **Response:** `TariffInformation`

#### Get Future Tariff Agreement Lookup
- **Endpoint:** `POST /api/v2/tariff/futureTariffAgreementLookup`
- **Description:** Returns the detailed data for a single tariff agreement program
- **Request Body:** `TariffRequest`
- **Response:** `TariffAgreements`

#### Current Tariff Lookup
- **Endpoint:** `POST /api/v2/tariff/currentTariffLookup`
- **Description:** Returns a list of HTS numbers
- **Request Body:** `CurrentTariffRequest`
- **Response:** `CurrentTariffList`

#### Get Tariff Programs (GET)
- **Endpoint:** `GET /api/v2/tariff/tariffProgramsLookup`
- **Description:** Returns a list of tariff programs with descriptions
- **Response:** `TariffProgramsResponse`

#### Get Current Tariff Year
- **Endpoint:** `GET /api/v2/tariff/currentTariffYear`
- **Description:** Returns the current year for which the database has tariff information
- **Response:** `CurrentTariffYear`

#### Get Current Tariff Details
- **Endpoint:** `GET /api/v2/tariff/currentTariffDetails`
- **Description:** Returns details about a particular HTS8 number and year
- **Parameters:**
  - `year` (required): String
  - `hts8` (required): String
- **Response:** `TariffDetailsWrapper`

---

### 🏃‍♂️ Run Query

#### Run Report
- **Endpoint:** `POST /api/v2/report2/runReport`
- **Description:** Returns import/export data based on sent query parameters
- **Request Body:** `SavedQuery`
- **Response:** `DTOTokenPairQueryResultsDatasetDataExportTable`

---

### 💾 Saved Queries

#### Get Saved Query
- **Endpoint:** `POST /api/v2/savedQuery/getSavedQuery`
- **Description:** Returns all parameters of a saved query based on user specific query ID
- **Request Body:** `SavedQueryRequest`
- **Response:** `SavedQuery`

#### Get All System Saved Queries
- **Endpoint:** `GET /api/v2/savedQuery/getAllSystemSavedQueries`
- **Description:** Returns list of all system defined saved queries
- **Response:** `SavedQueryResult`

#### Get All Shared Queries
- **Endpoint:** `GET /api/v2/savedQuery/getAllSharedQueries`
- **Description:** Returns a list of all queries a user has shared
- **Response:** `SavedQueryResult`

#### Get All Saved Queries
- **Endpoint:** `GET /api/v2/savedQuery/getAllSavedQueries`
- **Description:** Returns a list of all queries a user has saved
- **Response:** `SavedQueryResult`

---

### ❓ Query Info

#### Get RP Codes List
- **Endpoint:** `POST /api/v2/query/getRPCodesList`
- **Description:** Returns a list of all rate provision codes
- **Request Body:** `OptionsRequestBasic`
- **Response:** `QueryResult`

#### Get RP Code Groups
- **Endpoint:** `POST /api/v2/query/getRPCodeGroups`
- **Description:** Returns a list of all rate provision code groups
- **Request Body:** `OptionsRequestBasic`
- **Response:** `OptionsDTORPCodeGroupDTO`

#### Get Import Programs
- **Endpoint:** `POST /api/v2/query/getImportPrograms`
- **Description:** Returns a list of all import programs
- **Request Body:** `OptionsRequestBasic`
- **Response:** `QueryResult`

#### Get District User Group by Hash
- **Endpoint:** `POST /api/v2/query/getDistrictUserGroupByHash`
- **Description:** Returns the list of districts in a user saved district group
- **Request Body:** `GroupLookupRequest`
- **Response:** `DistrictGroup`

#### Get Country User Group by Hash
- **Endpoint:** `POST /api/v2/query/getCountryUserGroupByHash`
- **Description:** Returns the list of countries in a user saved country group
- **Request Body:** `GroupLookupRequest`
- **Response:** `CountryGroup`

#### Get Commodity User Group by Hash
- **Endpoint:** `POST /api/v2/query/getCommodityUserGroupByHash`
- **Description:** Returns the list of commodities in a user saved commodities group
- **Request Body:** `CommodityGroupLookupRequest`
- **Response:** `CommodityGroup`

#### Get Unit Conversion List
- **Endpoint:** `GET /api/v2/query/getUnitConversionList`
- **Description:** Returns the list of unit conversion objects
- **Response:** Array of `ConversionDTO`

#### Get Global Variables
- **Endpoint:** `GET /api/v2/query/getGlobalVars`
- **Description:** Returns current year, month, and quarter information
- **Response:** `GlobalVars`

---

### 📦 Commodities

#### Validate Commodity Search
- **Endpoint:** `POST /api/v2/commodity/validateCommoditySearch`
- **Description:** Returns a list of commodities based on comma separated list of search terms for a given commodity system classification level
- **Request Body:** `OptionsRequest`
- **Response:** `CommodityValidationResultList`

#### Validate Commodity Numbers Only
- **Endpoint:** `POST /api/v2/commodity/validateCommodityNumbersOnly`
- **Description:** Returns a list of commodities based on comma separated list of search terms (numbers only) for a given commodity system classification level
- **Request Body:** `OptionsRequest`
- **Response:** `CommodityValidationResultList`

#### Get All User Groups with Commodities
- **Endpoint:** `POST /api/v2/commodity/getAllUserGroupsWithCommodities`
- **Description:** Returns a list of user defined commodities groups along with all corresponding commodities within the group
- **Request Body:** `CommodityGroupReadRequest`
- **Response:** `CommodityGroupOptions`

#### Get All System Groups with Commodities
- **Endpoint:** `POST /api/v2/commodity/getAllSystemGroupsWithCommodities`
- **Description:** Returns a list of system commodity groups administered through the dataweb admin app
- **Request Body:** `AllCommoditiesRequest`
- **Response:** `CommodityGroupOptions`

#### Commodity Tree
- **Endpoint:** `POST /api/v2/commodity/commodityTree`
- **Description:** Returns a list of commodity numbers for a particular level, classification system and trade type (import/export)
- **Request Body:** `CommodityTreeRequest`
- **Response:** `QueryResult`

#### Commodity Translation Lookup
- **Endpoint:** `POST /api/v2/commodity/commodityTranslationLookup`
- **Description:** Returns a list of translated commodity classification system numbers (e.g., from HTS to SITC)
- **Request Body:** `CommodityTranslationRequest`
- **Response:** `CommodityTranslationResponse`

#### Commodity Description Lookup
- **Endpoint:** `POST /api/v2/commodity/commodityDescriptionLookup`
- **Description:** Returns a list of all commodity numbers with descriptions for a commodity classification system
- **Request Body:** `CommodityDescriptionRequest`
- **Response:** `CommodityDescriptions`

#### Get All Total User Groups with Commodities
- **Endpoint:** `GET /api/v2/commodity/getAllTotalUserGroupsWithCommodities`
- **Description:** Returns a list of user defined commodities groups along with all corresponding commodities within the group
- **Response:** `CommodityGroupOptions`

---

### 🌍 Countries

#### Get All User Groups with Countries
- **Endpoint:** `GET /api/v2/country/getAllUserGroupsWithCountries`
- **Description:** Returns a list of user defined country groups along with all corresponding countries and respective country codes in the group
- **Response:** `CountryGroupOptions`

#### Get All System Groups with Countries
- **Endpoint:** `GET /api/v2/country/getAllSystemGroupsWithCountries`
- **Description:** Returns a list of default system defined country groups with their corresponding list of countries
- **Response:** `CountryGroupOptions`

#### Get All Countries
- **Endpoint:** `GET /api/v2/country/getAllCountries`
- **Description:** Returns a list of all countries with their respective country codes
- **Response:** `JSON`

---

### 🏢 Districts

#### Get All User Groups with Districts
- **Endpoint:** `GET /api/v2/district/getAllUserGroupsWithDistricts`
- **Description:** Returns a list of user defined district groups along with all corresponding districts and their respective district codes in the group
- **Response:** `DistrictGroupOptions`

#### Get All Districts
- **Endpoint:** `GET /api/v2/district/getAllDistricts`
- **Description:** Returns a list of all districts with their respective district codes
- **Response:** `QueryResult`

---

### 🏛️ Programs

#### Get All Programs
- **Endpoint:** `GET /api/v2/program/programs`
- **Description:** Returns all programs
- **Parameters (optional):**
  - `country`: String
  - `hts8`: String
  - `beginYear`: String
  - `endYear`: String
- **Response:** Array of `Csc2`

#### Get Program Country Years
- **Endpoint:** `GET /api/v2/program/programCountryYears`
- **Description:** Returns program years for a specific program and country
- **Parameters (required):**
  - `programId`: String
  - `countryCode`: String
- **Response:** Array of strings

#### Get Program Countries
- **Endpoint:** `GET /api/v2/program/programCountries`
- **Description:** Returns countries for a specific program
- **Parameters (required):**
  - `programId`: String
- **Response:** Array of `CountryProgram`

#### Get Programs Details
- **Endpoint:** `GET /api/v2/program/getPrograms`
- **Description:** Returns program details
- **Parameters (required):**
  - `hts8`: String
  - `year`: String
  - `countryCode`: String
- **Response:** Array of objects

#### Get Programs and HTS Numbers
- **Endpoint:** `GET /api/v2/program/getProgramsAndHtsNums`
- **Description:** Returns programs and HTS numbers
- **Parameters (required):**
  - `country`: String
  - `year`: String
- **Response:** Array of objects

#### Get Programs and Countries
- **Endpoint:** `GET /api/v2/program/getProgramsAndCountries`
- **Description:** Returns programs and countries
- **Parameters (required):**
  - `hts8`: String
  - `year`: String
- **Response:** Array of objects

---

### 🔔 Notifications

#### Get Notification Preferences
- **Endpoint:** `GET /api/v2/notification/notification-preferences`
- **Description:** Returns user notification preferences
- **Response:** `UserNotificationPreferencesDTO`

#### Update Notification Preferences
- **Endpoint:** `POST /api/v2/notification/notification-preferences`
- **Description:** Updates user notification preferences
- **Request Body:** `UserNotificationPreferencesDTO`

---

### 🚨 System Alerts

#### Get All System Alerts
- **Endpoint:** `GET /api/v2/system-alert`
- **Description:** Returns all system alerts
- **Response:** Array of `SystemAlertDTO`

#### Update System Alert
- **Endpoint:** `POST /api/v2/system-alert`
- **Description:** Updates a system alert
- **Request Body:** `SystemAlertDTO`

#### Get System Alert by ID
- **Endpoint:** `GET /api/v2/system-alert/alert/{id}`
- **Description:** Returns a specific system alert
- **Parameters:**
  - `id` (path, required): Integer
- **Response:** `SystemAlertDTO`

#### Delete System Alert
- **Endpoint:** `DELETE /api/v2/system-alert/alert/{id}`
- **Description:** Deletes a specific system alert
- **Parameters:**
  - `id` (path, required): Integer

---

## Key Data Models

### Common Request Models

#### TariffSummaryRequest
```json
{
  "htsCode": "string",
  "years": ["string"],
  "htsCodes": ["string"],
  "type": "string"
}
```

#### TariffProgramRequest
```json
{
  "code": "string",
  "group": "string"
}
```

#### TariffRequest
```json
{
  "agreementId": "string",
  "commodityId": "string"
}
```

#### CurrentTariffRequest
```json
{
  "searchTerm": "string",
  "tariffYear": "string"
}
```

#### OptionsRequest
```json
{
  "tradeType": "string",
  "classificationSystem": "string",
  "search": "string",
  "level": 0
}
```

#### OptionsRequestBasic
```json
{
  "tradeType": "string"
}
```

#### SavedQueryRequest
```json
{
  "savedQueryID": "string"
}
```

#### CommodityGroupReadRequest
```json
{
  "tradeType": "string",
  "classificationSystem": "string"
}
```

#### CommodityTreeRequest
```json
{
  "tradeType": "string",
  "classificationSystem": "string",
  "chapter": "string",
  "level": 0
}
```

#### CommodityTranslationRequest
```json
{
  "classificationFrom": "string",
  "commodityId": "string",
  "year": "string"
}
```

#### CommodityDescriptionRequest
```json
{
  "codes": ["string"],
  "tradeType": "string",
  "classificationSystem": "string",
  "granularity": 0
}
```

### SavedQuery Model (Complex)
The `SavedQuery` model is comprehensive and includes parameters for:
- Trade type and classification system
- Data reporting options and scale
- Timeframe selection (years, dates, months)
- Commodity selection and grouping
- Country selection and grouping  
- Import programs and rate provision codes
- District selection
- Sorting and display options
- Export options and unit conversions

### Response Models

Key response models include:
- `TariffSummaryDetails`: HTS8, text rate, program code
- `TariffInformation`: HTS number, description, staged duty reductions
- `CommodityValidationResult`: Code and description pairs
- `QueryResult`: Generic list of text/value pairs
- `GlobalVars`: Current year, month, quarter, and database dates

---

## Usage Tips

1. **Authentication**: Many endpoints require API tokens - generate one from the Dataweb application
2. **Trade Types**: Common values are "import" and "export"
3. **Classification Systems**: Include HTS, SITC, NAICS, etc.
4. **Granularity Levels**: Different commodity classification levels (2, 4, 6, 8, 10 digit)
5. **Date Formats**: Use proper date formatting for time-based queries
6. **Rate Provision Codes**: Used for tariff-related queries
7. **Batch Operations**: Many endpoints accept arrays for bulk operations

---

## Error Handling

The API returns standard HTTP status codes:
- **200**: Success
- **400**: Bad Request - Invalid parameters
- **401**: Unauthorized - Invalid or missing API token
- **500**: Internal Server Error

Always check the response status and handle errors appropriately in your application.