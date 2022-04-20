import currentweatherdataonly as c
from pprint import pprint

import RPi.GPIO as GPIO
from gpiozero import Motor
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

current_weather = c.current_weather_data_only()

#porch lights turning on/off
GPIO.setup(7, GPIO.OUT)

if current_weather['isDaytime'] == True:
    #porch lights off
    GPIO.output(7,GPIO.LOW)
    print('porch OFF')
else:
    GPIO.output(7,GPIO.HIGH)
    print('porch ON')
    
#fan turning on/off
while current_weather['temperature'] > 69:
    #turn DC fan on
    GPIO.output(13,GPIO.HIGH)
    print('fan ON')

#fireplace turning on/off
GPIO.setup(11, GPIO.OUT)

if current_weather['temperature'] < 46:
    #turn fireplace on
    GPIO.output(11,GPIO.HIGH)
    print('fireplace ON')
else:
    GPIO.output(11,GPIO.LOW)
    print('fireplace OFF')

#blinds
if 'Sunny' or 'Clear' in current_weather['shortForecast']:
    #shades down
    print('shades DOWN')
else:
    print('shades UP')


    
