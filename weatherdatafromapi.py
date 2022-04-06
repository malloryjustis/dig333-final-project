from requests import get
import json
from pprint import pprint

url = 'https://api.weather.gov/gridpoints/GSP/116,76/forecast'

weather = get(url).json()['properties']
pprint(weather)

