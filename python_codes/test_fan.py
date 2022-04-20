import RPi.GPIO as GPIO
from gpiozero import Motor
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(13, GPIO.OUT)
GPIO.output(13,GPIO.HIGH)
print('fan ON')
