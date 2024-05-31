import requests
import json

url = "https://api.hh.ru/vacancies?text=python"

response = requests.get(url)

data = response.json()

print(response.text)

with open('data.json', 'w') as file:
    json.dump(data, file)

print(data["items"][0])
