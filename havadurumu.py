import requests
import time

def get_weather_data():
    url = "https://api.openweathermap.org/geo/1.0/direct?q=Ankara&limit=5&appid=779c271986d91ab4f86362ce5d62e73c"
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
    weather_data = get_weather_data()
    lat = weather_data[0]['lat']
    lon = weather_data[0]['lon']
    temp = get_temperature(lat, lon)
    
    print(f"Ankara'nın sıcaklığı: {temp}°C")
    
    time.sleep(0.30)