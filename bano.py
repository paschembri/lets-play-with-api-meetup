import requests
import json

address = "5 rue des murgers La Garenne Colombes".replace(" ", "+")

url = f'https://api-adresse.data.gouv.fr/search/?q={address}'

response = requests.get(url)

json_response = json.dumps(response.json(), indent=4)

print(json_response)
