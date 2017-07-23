import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)     # use GPIO number
GPIO.setup(25, GPIO.OUT)   # output GPIO 25

GPIO.output(25, GPIO.HIGH) # output GPIO as high setting
time.sleep(2)              # wait

GPIO.cleanup()             # turn off the light
