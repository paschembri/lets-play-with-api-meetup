import requests
import json

city = 'Toulouse, FR'

#: Register on openweathermap to obtain an api key
api_key = 'xxx'

url = (
    f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}'
)

response = requests.get(url)

json_response = json.dumps(response.json(), indent=4)

print(json_response)
