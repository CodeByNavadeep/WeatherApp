from datetime import datetime

class WeatherLogger:
    def __init__(self, filename="weather_log.txt"):
        self.filename = filename
    
    def log_to_file(self, weather_data):
        try:
            with open(self.filename, "a") as f:
                f.write(str(weather_data) + "\n")
                print("Logged Succesfully!")
        except Exception as e:
            print(e)