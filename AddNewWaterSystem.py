# This script adds a new water system to your primacy agency

# request library to interact with the server/api
# json to make the resulting json into a redable format
import requests
import json

# url for inventory api
inventoryApi = "https://inventory.dwsfties-uat-api.epa.gov"

# copy and paste the access_token from your profile-> copy access token in UAT
access_token = "<your_access_token>"

headerForApi = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Note: you can change all the values to the right of : in newWaterSystem
newWaterSystem = {
  "waterSystemId": "X19852075",
  "name": "myNewWaterSystem",
  "wsOwnerTypeCode": "L",
  "wsStatusCode": "A",
  "waterSystemStatusDt": "2025-04-16",
  "seasonalInd": "N",
  "dwpWaterSystemAnnualOperatingPeriods": [],
  "waterSystemServiceConnections": [],
  "measureRequests": [],
  "wsIndicatorRequests": [],
  "relatedPOCRequests": [],
  "flowRateRequests": [],
  "waterSystemCertRequests": [],
  "geographicAreas": [],
  "serviceAreas": [],
  "wholeSalerInd": "Y",
  "wsServiceLineRequests": []
}

# Send the newWaterSystem
apiCall = requests.post(f"{inventoryApi}/inventory/water-system", json=newWaterSystem, headers=headerForApi)

# code of 200 means successfully added the newWaterSystem
if apiCall.status_code != 200:
    print("Api call failed with the token: ", apiCall.status_code, apiCall.text)
else:
    print("success")
