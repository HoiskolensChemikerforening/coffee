import RPi.GPIO as GPIO 
import time

BUTTON_out=13
BUTTON_in = 19
RED_LED = 16
YELLOW_LED = 12

def SetUp():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUTTON_in,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BUTTON_out,GPIO.OUT)

    GPIO.setup(YELLOW_LED, GPIO.OUT) 
    GPIO.setup(RED_LED, GPIO.OUT) 
    for i in range(5):
        GPIO.output(RED_LED,GPIO.HIGH)
        GPIO.output(YELLOW_LED,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(YELLOW_LED,GPIO.LOW)
        GPIO.output(RED_LED,GPIO.LOW)
        time.sleep(0.1)
    GPIO.output(BUTTON_out,GPIO.HIGH)

def Blink401():
    for i in range(2):
        GPIO.output(RED_LED, GPIO.HIGH)
        GPIO.output(YELLOW_LED, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(RED_LED, GPIO.LOW)
        GPIO.output(YELLOW_LED, GPIO.LOW)
        time.sleep(0.5)

def Blink404():
    for i in range(4):
        GPIO.output(RED_LED, GPIO.HIGH)
        GPIO.output(YELLOW_LED, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(RED_LED, GPIO.LOW)
        GPIO.output(YELLOW_LED, GPIO.LOW)

def NoInternet():
    for i in range(2):
        GPIO.output(RED_LED, GPIO.HIGH)
        GPIO.output(YELLOW_LED, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(RED_LED, GPIO.LOW)
        GPIO.output(YELLOW_LED, GPIO.HIGH)
        time.sleep(0.5)
    GPIO.output(YELLOW_LED, GPIO.LOW)
    GPIO.output(RED_LED, GPIO.LOW)

def BlinkBreakLoop():
    GPIO.output(RED_LED, GPIO.HIGH)
    GPIO.output(YELLOW_LED, GPIO.LOW)
    time.sleep(5)
    GPIO.output(RED_LED, GPIO.LOW)

def BlinkServerError():
    for i in range(2):
        GPIO.output(RED_LED, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(RED_LED, GPIO.LOW)
        time.sleep(0.5)

    for i in range(2):
        GPIO.output(YELLOW_LED, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(YELLOW_LED, GPIO.LOW)
        time.sleep(0.5)

def BlinkFifteenMinutes():
    for i in range(2):
        GPIO.output(RED_LED, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(RED_LED, GPIO.LOW)
        time.sleep(1)

SetUp()
time.sleep(1)
Blink401()
time.sleep(1)
Blinkbreakloop()
time.sleep(1)
Blink404()
time.sleep(1)
NoInternet()
time.sleep(1)
BlinkServerError()
time.sleep(1)
BlinkFifteenMinutes()
