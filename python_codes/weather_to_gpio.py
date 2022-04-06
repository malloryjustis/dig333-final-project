import currentweatherdataonly as c
from pprint import pprint

import RPi.GPIO as GPIO

current_weather = c.current_weather_data_only()

#porch lights turning on/off
if current_weather['isDaytime'] == True:
    #porch lights off
    print('porch OFF')
else:
    GPIO.output(7,GPIO.HIGH)
    print('porch ON')


#fan turning on/off
if current_weather['temperature'] > 69:
    #turn fan on
    print('fan ON')
else:
    print('fan OFF')

#fireplace turning on/off
if current_weather['temperature'] < 46:
    #turn fireplace on
    GPIO.output(11,GPIO.HIGH)
    print('fireplace ON')
else:
    print('fireplace OFF')


#blinds
if 'Sunny' or 'Clear' in current_weather['shortForecast']:
    #shades down
    print('shades DOWN')
else:
    print('shades UP')


    
