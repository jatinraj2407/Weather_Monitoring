import requests

class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather_data(self, city):
        response = requests.get(self.base_url, params={'q': city, 'appid': self.api_key, 'units': 'metric'})
        if response.status_code == 200:
            return response.json()
        return None
