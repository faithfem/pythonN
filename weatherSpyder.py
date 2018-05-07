import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?lat=41.781&lon=-71.4372&appid=852e7ec79c723c416d0e7d5f262a8842'

url = api_address

json_data = requests.get(url).json()

formatted_data = json_data

print(formatted_data)