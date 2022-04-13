from requests import get
import json
from pprint import pprint

def weather_data_from_api():

    url = 'https://api.weather.gov/gridpoints/GSP/116,76/forecast/hourly'

    weather = get(url).json()['properties']
    return weather


