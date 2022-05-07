from time import sleep
import RPi.GPIO as GPIO

DIR = 29 # direction gpio pin
STEP = 31 # step gpio pin
CW = 33 # clockwise rotation
CCW = 35 # counterclockwise rotation
SPR = 48 # steps per revolution (360 / 7.5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

step_count = SPR
delay = 0.0208

for x in range(step_count):
  GPIO.OUTPUT(STEP, GPIO.HIGH)
  sleep(delay)
  GPIO.OUTPUT(STEP, GPIO.LOW)
  sleep(delay)
  
sleep(0.5)
GPIO.output(DIR, CCW)

for x in range(step_count):
  GPIO.OUTPUT(STEP, GPIO.HIGH)
  sleep(delay)
  GPIO.OUTPUT(STEP, GPIO.LOW)
  sleep(delay)
