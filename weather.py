import requests

API_KEY = "50be83e565db5ead67100d04f874c07a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

print("Welcome!")
city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp']-273.15, 2)
    fahrenheit = round((data['main']['temp']-273.15)*(9/5)+32, 2)

    print("Weather:", weather)
    print(f"Temperature in celsius: {temperature} C")
    print(f"Temperature in fahrenheit: {fahrenheit} F")

else:
    print("An error occurred.")

