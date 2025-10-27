import requests
from flask import jsonify
from datetime import datetime

class WeatherFetcher:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url
    
    def fetch_weather(self, city):
        try:
            params = {'q' : city, 'appid' : self.api_key, 'units' : 'metric'}
            response = requests.get(self.base_url, params=params)
            data =  response.json()
            
            if response.status_code != 200:
                return jsonify({"error" : response.get("message")}), 400
            
            weather_info = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "condition": data["weather"][0]["description"],
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            return weather_info
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500