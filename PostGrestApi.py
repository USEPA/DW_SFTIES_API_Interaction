# request library to interact with the server/api
# json to make the resulting json into a redable format
import requests
import json

# Now we have the access_token, we're ready to call the api
postGrestApi = "https://dwsfties-uat-api.epa.gov:443/api/db"

# copy and paste the access_token from your profile-> copy access token in UAT
access_token = "<your_token_from_uat_profile>"

# Lower case for your agency. format is dwp_yourAgency 
# if x1 is your agency then primacyAgency = dwp_x1
primacyAgency='dwp_<your_agency>'

headerForApi = {
    "accept": 'application/json',
    "Authorization": f"Bearer {access_token}",
    "Accept-Profile": primacyAgency
}

# retrieve list of water system in your primacy agency
apiCall = requests.get(f"{postGrestApi}/dwp_water_system", headers=headerForApi)

if apiCall.status_code != 200:
    print("Api call failed with the token: ", apiCall.status_code, apiCall.text)
else:
    data = apiCall.json()
    print(json.dumps(data, indent=4))
