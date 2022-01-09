"""
Weather data example:
{'coord': {'lon': 34.8, 'lat': 32.0833},
'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}],
'base': 'stations',
'main': {'temp': 14.89, 'feels_like': 14.05, 'temp_min': 13.97, 'temp_max': 15.43, 'pressure': 1013, 'humidity': 62},
'visibility': 10000,
'wind': {'speed': 3.6, 'deg': 140},
'clouds': {'all': 0},
'dt': 1641751676,
'sys': {'type': 1, 'id': 6845, 'country': 'IL', 'sunrise': 1641703337, 'sunset': 1641739974},
'timezone': 7200,
'id': 293396,
'name': 'Tel Aviv',
'cod': 200}

"""
import datetime


class WeatherData:

    def __init__(self, data):
        self.data = data
        self.temperature = data['main']['temp']
        self.description = data['weather'][0]['description']
        self.humidity = data['main']['humidity']
        self.update_ts_utc = datetime.datetime.fromtimestamp(data['dt'])
