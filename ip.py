import requests
import json

url = "https://jsonip.com/"

response = requests.get(url)

json_response = json.dumps(response.json(), indent=4)

print(json_response)
