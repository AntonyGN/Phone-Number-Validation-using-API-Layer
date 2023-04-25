import requests
import json

url = "https://api.apilayer.com/number_verification/validate"
params = {"number": "254790295419"}
headers = {"apikey": "hwKpz11LVNRgK97gaRYS2Puz4uNITDhg"}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    result = json.loads(response.text)
    if result["valid"]:
        if result["carrier"]:
            print(f"The phone number {result['number']} is valid and belongs to {result['carrier']}.")
        else:
            print(f"The phone number {result['number']} is valid but the carrier information is not available.")
    else:
        print(f"The phone number {result['number']} is not valid.")
else:
    print(f"An error occurred: {response.status_code}")
