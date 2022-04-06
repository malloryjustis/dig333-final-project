import weatherdatafromapi as w
from pprint import pprint

def current_weather_data_only():

    weather = w.weather_data_from_api()

    weather_list = list(weather['periods'])
    current_weather = weather_list[0]

    return current_weather
