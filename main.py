from flask import Flask, render_template, request, url_for, jsonify
from config import API_KEY, BASE_URL
from weather_api import WeatherFetcher
from logger import WeatherLogger

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getWeather', methods=["POST"])
def getWeather():
    data = request.get_json()
    city = data.get("city")
    
    fetcher = WeatherFetcher(api_key=API_KEY, base_url=BASE_URL)
    weather_data = fetcher.fetch_weather(city=city)
    
    if str(weather_data)=="(<Response 58 bytes [200 OK]>, 500)":
            return None
    else:
        logger = WeatherLogger("weather_log.txt")
        logger.log_to_file(weather_data=weather_data)
        return jsonify(weather_data)
    

if __name__ == '__main__':
    app.run(debug=True)