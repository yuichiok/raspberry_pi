import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)     # use GPIO number
GPIO.setup(25, GPIO.OUT)   # output GPIO 25

GPIO.output(25, GPIO.HIGH) # output GPIO as high setting
