import RPi.GPIO as GPIO
from gpiozero import Motor
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(13, GPIO.OUT)
GPIO.output(13,GPIO.HIGH)
print('fan ON')
time.sleep(5)
GPIO.output(13,GPIO.LOW)
print('fan OFF')
