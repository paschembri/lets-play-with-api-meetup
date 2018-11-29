import requests
import json

meetup = 'Paris-Tech-for-Business'

url = f'https://api.meetup.com/{meetup}/events'

response = requests.get(url)

json_response = json.dumps(response.json(), indent=4)

print(json_response)
