import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?lat=42.3603&lon=-71.0583&appid=852e7ec79c723c416d0e7d5f262a8842'

url = api_address

json_data = requests.get(url).json()

formatted_data = json_data['weather'][0]['main']

print(formatted_data)