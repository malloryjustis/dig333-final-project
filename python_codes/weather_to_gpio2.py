import currentweatherdataonly2 as c
from pprint import pprint

import RPi.GPIO as GPIO

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
else:
    #turn DC fan off
    GPIO.output(13,GPIO.LOW)
    print('fan OFF')

#fireplace turning on/off
GPIO.setup(15, GPIO.OUT)

if current_weather['temp'] < 70:
    #turn fireplace on
    GPIO.output(15,GPIO.HIGH)
    print('fireplace ON')
else:
    GPIO.output(15,GPIO.LOW)
    print('fireplace OFF')

#solar panel
GPIO.setup(29, GPIO.OUT)

if 'Few Clouds' or 'Clear' or "Partly Cloudy" in current_weather['wx_str']:
    #solar on
    GPIO.output(29, GPIO.HIGH)
    print('solar ON')
else:
    GPIO.output(29, GPIO.LOW)
    print('solar OFF')

