from datetime import datetime
from datetime import timedelta
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
import time
import requests
import json
import simplejson
from params import topic, notification_key

from blinking_signals import SetUp, Blink401, Blink404, NoInternet, BreakingLoop, BlinkServerError, BlinkFifteenMinutes
# defining of parameters and function
###############################################

BUTTON_out=13
BUTTON_in = 19
RED_LED = 16
YELLOW_LED = 12

url = "https://hc.ntnu.no/web_push/send"
pressed_time = datetime.now() + timedelta(-30)

payload = {
    "topic":topic,
    "notification_key":notification_key,
}
headers = {
    "Content-Type": "application/json",
}

# Main part of the script
#######################################
SetUp()
print("Running")
while True:
    try:
    	GPIO.output(BUTTON_out, GPIO.HIGH)
        input_value = GPIO.input(BUTTON_in)
        if input_value:
            elapsed_time =  datetime.now() - pressed_time
            if elapsed_time.total_seconds() > 900:
                pressed_time = datetime.now()
                GPIO.output(YELLOW_LED,GPIO.HIGH)
                r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=300)
                status_code = r.status_code
                print(status_code)
                time.sleep(2)
                GPIO.output(YELLOW_LED,GPIO.LOW)
                if status_code == 201:
                    print("success")
                    GPIO.output(YELLOW_LED,GPIO.LOW)
                    time.sleep(0.2)
                    GPIO.output(YELLOW_LED,GPIO.HIGH)
                    time.sleep(0.2)
                    GPIO.output(YELLOW_LED,GPIO.LOW)
                    time.sleep(0.2)
                    GPIO.output(YELLOW_LED,GPIO.HIGH)
                    time.sleep(0.2)
                    GPIO.output(YELLOW_LED,GPIO.LOW)
                elif status_code == 401:
                    print(401)
                    Blink401()
                elif status_code == 404:
                    print(404)
                    Blink404()
                elif int(status_code) >=500:
                    print("Server error")
                    BlinkServerError()
                time.sleep(5)
            else:
                print("15 minutes error")
                GPIO.output(YELLOW_LED,GPIO.LOW)
                BlinkFifteenMinutes()
    except requests.exceptions.ConnectionError:
        print("No internet")
        NoInternet()
    except Exception as e:
        print("Breaking loop")
        filename = "/home/pi/Coffee-Button/errors/" + str(datetime.now().date()) + "-" + str(datetime.now().microsecond) 
        logf = open(filename, "w")
        logf.write('An exceptional thing happed\n %s \n' % e)
        BreakingLoop()
        GPIO.cleanup()
        break
