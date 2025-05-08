# Note: This script calls the postgREST api for DW-SFTIES to get the all the water systems for your primacy agency. 
# First you interact with the server to retrieve the access token and then use the access token to interact with the api

# request library to interact with the server/api
# json to make the resulting json into a redable format
import requests
import json

serverUrl='https://dwsfties-uat-api.epa.gov/api/auth/realms/sdwismod/protocol/openid-connect/token'

access_token = ''

# login credentials
credentials = {
    "grant_type":'password',
    # client_id and client_secret will be provided to you
    "username": '<provided_client_id>', 
    "password": '<provided_client_secret>'
}

# header
postHeaders = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# we send our login credentials to the server to get the access_token and other relevant information
serverResponse = requests.post(serverUrl, data=credentials, headers=postHeaders)

# process the response
if serverResponse.status_code != 200:
    print("Failed to get tokens:", serverResponse.status_code, serverResponse.text)
else:
    actualResponse = serverResponse.json()
    # print(actualResponse)
    access_token = actualResponse.get("access_token")
    refresh_token = actualResponse.get("refresh_token")
    token_type = actualResponse.get("token_type")
    expires_in = actualResponse.get("expires_in")
    # print("Access token: ", access_token)

# Now we have the access_token, we're ready to call the api
postGrestApi = "https://dwsfties-uat-api.epa.gov:443/api/db"

# Lower case for your agency. format is dwp_yourAgency 
# if x1 is your agency then primacyAgency = dwp_x1
primacyAgency='dwp_<yourAgency>'

headerForApi = {
    "accept": 'application/json',
    "Authorization": f"Bearer {access_token}",
    "Accept-Profile": primacyAgency
}

# gets all the water system info for your primacy agency
apiCall = requests.get(f"{postGrestApi}/dwp_water_system", headers=headerForApi)

# print in a readable format
if apiCall.status_code != 200:
    print("Api call failed with the token: ", apiCall.status_code, apiCall.text)
else:
    data = apiCall.json()
    print(json.dumps(data, indent=4))


