# request library to interact with the server/api
# json to make the resulting json into a redable format
import requests
import json

# Now we have the access_token, we're ready to call the api
inventoryApi = "https://inventory.dwsfties-uat-api.epa.gov"

# copy and paste the access_token from your profile-> copy access token in UAT
access_token = "<your_token_from_uat_profile>"
headerForApi = {
    "Authorization": f"Bearer {access_token}"
}

apiCall = requests.get(f"{inventoryApi}/inventory/water-system", headers=headerForApi)

if apiCall.status_code != 200:
    print("Api call failed with the token: ", apiCall.status_code, apiCall.text)
else:
    data = apiCall.json()
    print(json.dumps(data, indent=4))