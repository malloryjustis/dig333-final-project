from requests import get
import json
from pprint import pprint

def weather_data_from_api():

    url = 'https://api.weatherusa.net/v1/forecast?q=35.227085,-80.843124&daily=0&units=e&maxtime=7d'

    weather = get(url).json()
    return weather
