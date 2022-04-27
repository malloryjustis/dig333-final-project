import currentweatherdataonly2 as c
from pprint import pprint

import RPi.GPIO as GPIO
from gpiozero import Motor

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

current_weather = c.current_weather_data_only()

#porch lights turning on/off
GPIO.setup(11, GPIO.OUT)

if current_weather['night'] == False:
    #porch lights off
    GPIO.output(11,GPIO.LOW)
    print('porch OFF')
else:
    GPIO.output(11,GPIO.HIGH)
    print('porch ON')
    
#fan turning on/off
GPIO.setup(13, GPIO.OUT)

if current_weather['temp'] > 69:
    #turn DC fan on
    GPIO.output(13,GPIO.HIGH)
    print('fan ON')

#fireplace turning on/off
GPIO.setup(15, GPIO.OUT)

if current_weather['temp'] < 46:
    #turn fireplace on
    GPIO.output(15,GPIO.HIGH)
    print('fireplace ON')
else:
    GPIO.output(15,GPIO.LOW)
    print('fireplace OFF')

#blinds #need to adjust this code for new api
if 'Sunny' or 'Clear' in current_weather['shortForecast']:
    #shades down
    print('shades DOWN')
else:
    print('shades UP')

