from requests import get
import json
from pprint import pprint

def weatherdatafromapi():

    url = 'https://api.weather.gov/gridpoints/GSP/116,76/forecast'

    weather = get(url).json()['properties']
    pprint(weather)
    return weather


