from datetime import datetime
from datetime import timedelta
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
import time
import requests
import json
import simplejson
from params import topic, notification_key, website_url

from blinking_signals import SetUp#, blink401, blinkbreakloop, blink404 NoInternet, blinkServerError, blinkFifteenMinutes
# defining of parameters and function
###############################################

BUTTON_out=13
BUTTON_in = 19
RED_LED = 16
YELLOW_LED = 12

url = website_url
pressed_time = datetime.now() - timedelta(-30)

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
while True:
    try:
    	GPIO.output(BUTTON_out, GPIO.HIGH)
        input_value = GPIO.input(BUTTON_in)
        if input_value:
            elapsed_time = datetime.now() - pressed_time
            if elapsed_time.total_seconds() > 900:
                pressed_time = datetime.now()
                GPIO.output(YELLOW_LED,GPIO.HIGH)
                r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=5)
		        status_code = r.status_code
                GPIO.output(YELLOW_LED,GPIO.LOW)
		        if status_code == 201:
                    pass
                elif status_code == 401:
                    blink401()
                elif status_code == 404:
                    blink404()
                elif int(status_code) >=500
                    blinkServerError()
            else:
                GPIO.output(YELLOW_LED,GPIO.LOW)
                blinkFifteenMinutes()
    except Exception as e:
        filename = "errors/" + str(datetime.now())
        logf = open(filename, "w")
        logf.write('An exceptional thing happed - %s' % e)
        brinkbreakloop()
	    GPIO.cleanup()
	    break
