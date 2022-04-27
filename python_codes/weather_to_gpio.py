import currentweatherdataonly as c
from pprint import pprint

import RPi.GPIO as GPIO
from gpiozero import Motor

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

current_weather = c.current_weather_data_only()

#porch lights turning on/off
GPIO.setup(1, GPIO.OUT)

if current_weather['isDaytime'] == True:
    #porch lights off
    GPIO.output(1,GPIO.LOW)
    print('porch OFF')
else:
    GPIO.output(1,GPIO.HIGH)
    print('porch ON')
    
#fan turning on/off
GPIO.setup(2, GPIO.OUT)

while current_weather['temperature'] > 69:
    #turn DC fan on
    GPIO.output(2,GPIO.HIGH)
    print('fan ON')

#fireplace turning on/off
GPIO.setup(17, GPIO.OUT)

if current_weather['temperature'] < 46:
    #turn fireplace on
    GPIO.output(17,GPIO.HIGH)
    print('fireplace ON')
else:
    GPIO.output(17,GPIO.LOW)
    print('fireplace OFF')

#blinds
if 'Sunny' or 'Clear' in current_weather['shortForecast']:
    #shades down
    print('shades DOWN')
else:
    print('shades UP')


    
