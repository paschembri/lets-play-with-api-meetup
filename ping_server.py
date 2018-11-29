import requests

url = "https://netsach.com/status/"

response = requests.get(url)

print(response.status_code, response.json())
