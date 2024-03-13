import requests
import base64

token_api = "https://www.abc.com"
zip_api = "https://www.xyz.com"
username = "username"
password = "password"


def get_auth_token():
    try:
        credentials = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("utf-8")

        headers = {
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/json"
        }
        payload = {}

        response = requests.post(token_api, headers=headers, json=payload)
        response.raise_for_status()

        response_data = response.json()
        auth_token = response_data.get('Token')

        print(f"Authentication successful. Auth Token: {auth_token}")

        return auth_token

    except requests.exceptions.RequestException as e:
        print(f"Error during authentication: {e}")
        return None


def make_api_request(auth_token):
    try:
        header = {
            "Authorization": f"Bearer {auth_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "header": {
                "RequestType": "AddressQualification",
                "RequestOriginType": "Online"
            },
            "salesAgentCode": None,
            "compaignCode": None,
            "zipCode": "30303",
            "customerType": "New",
            "transactionId": None,
            "city": "",
            "state": ""
        }

        api_response = requests.post(zip_api, headers=header, json=payload)
        api_response.raise_for_status()

        print(api_response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")


token = get_auth_token()

if token:
    make_api_request(token)
else:
    print("Authentication failed.")
