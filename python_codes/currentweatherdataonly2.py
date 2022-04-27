import weatherdatafromapi2 as w
from pprint import pprint

def current_weather_data_only():

    weather = w.weather_data_from_api()

    weather_list = list(weather)
    current_weather = weather_list[0]

    return current_weather

pprint(current_weather_data_only())
