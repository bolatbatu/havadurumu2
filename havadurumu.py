import requests
import time

def get_weather_data(city):
    url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid=779c271986d91ab4f86362ce5d62e73c"
    r = requests.get(url)
    data = r.json()
    return data


def get_temperature(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=779c271986d91ab4f86362ce5d62e73c&units=metric"
    r = requests.get(url)
    data = r.json()
    temperature = data["main"]["temp"]
    return temperature

while True:
    city = input("Enter a city name (e.g., Ankara): ")
    weather_data = get_weather_data(city)
    if len(weather_data) > 0:
        lat = weather_data[0]['lat']
        lon = weather_data[0]['lon']
        temp = get_temperature(lat, lon)
        print(f"{city}'s temperature: {temp}°C")
    else:
        print("Invalid city name. Please try again.")
    time.sleep(0.30)
