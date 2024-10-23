import time
import requests
from flask import Flask, jsonify
from database import Database
from weather_service import WeatherService
from utils import convert_to_celsius, calculate_aggregates

app = Flask(__name__)
db = Database()
weather_service = WeatherService(api_key='2a14ca0c19b80f8c0a7af1fe01fcb073')  # Use your actual API key here

@app.route('/start_monitoring', methods=['POST'])
def start_monitoring():
    while True:
        for city in ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']:
            data = weather_service.get_weather_data(city)
            if data:
                temperature_c = convert_to_celsius(data['main']['temp'])
                weather_summary = calculate_aggregates(data, temperature_c)
                db.store_daily_summary(weather_summary)
                # Check for alerts
                check_alerts(temperature_c)
            time.sleep(300)  # wait for 5 minutes
    return jsonify({"message": "Monitoring started."})

def check_alerts(temperature):
    threshold = 35  # User-defined threshold
    if temperature > threshold:
        print(f"Alert! High temperature: {temperature}°C")

if __name__ == '__main__':
    app.run(debug=True)
