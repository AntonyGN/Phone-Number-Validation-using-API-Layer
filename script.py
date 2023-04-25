import requests
import json
import phonenumbers
from phonenumbers import carrier

number = "+254790295419"

# Validate phone number using API
url = "https://api.apilayer.com/number_verification/validate"
params = {"number": number}
headers = {"apikey": "hwKpz11LVNRgK97gaRYS2Puz4uNITDhg"}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    result = json.loads(response.text)
    if result["valid"]:
        # If phone number is valid, parse it using phonenumbers library and retrieve carrier information
        try:
            parsed_number = phonenumbers.parse(number)
            carrier_name = carrier.name_for_number(parsed_number, 'en')
            if carrier_name:
                print(f"The phone number {number} is valid and belongs to {carrier_name}.")
            else:
                print(f"The phone number {number} is valid but the carrier information is not available.")
        except phonenumbers.NumberParseException as e:
            print(f"The phone number {number} could not be parsed: {e}")
    else:
        print(f"The phone number {number} is not valid.")
else:
    print(f"An error occurred: {response.status_code}")

