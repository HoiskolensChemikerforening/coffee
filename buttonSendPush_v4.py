from datetime import datetime
from datetime import timedelta
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
import time
import requests
import json
import simplejson
from params import topic, notification_key
from send_mail import send_mail
from blinking_signals import SetUp, BlinkSuccess, Blink401, Blink404, NoInternet, BreakingLoop, BlinkServerError, BlinkFifteenMinutes
# defining of parameters
###############################################

BUTTON_out=13
BUTTON_in = 19
RED_LED = 16
YELLOW_LED = 12

url = "https://hc.ntnu.no/web_push/send/"
pressed_time = datetime.now() + timedelta(-30)

payload = {
    "topic":topic,
    "notification_key":notification_key,
    "date": str(datetime.now())
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

            # Check that 15 minutes has passed since last press
            if elapsed_time.total_seconds() > 900: 
                GPIO.output(YELLOW_LED,GPIO.HIGH)
                
                # The Http request from the PI to the server
                payload["date"] = str(datetime.now())
                r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=300)
                
                status_code = r.status_code
                print(status_code)
                
                time.sleep(2)
                GPIO.output(YELLOW_LED,GPIO.LOW)
                
                # Processing the status code
                if status_code == 201:
                    print("success")
                    BlinkSuccess()
                    pressed_time = datetime.now()
                elif status_code == 401:
                    print(401)
                    Blink401()
                elif status_code == 402:
                    print(402)
                    BlinkFifteenMinutes()
                elif status_code == 404:
                    print(404)
                    Blink404()
                elif int(status_code) >= 500:
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
        GPIO.output(YELLOW_LED,GPIO.LOW)
        GPIO.output(RED_LED,GPIO.LOW)
        print("Breaking loop")
        
        #Logging the error locally in the pi storrage 
        filename = "/home/pi/coffee/errors/" + str(datetime.now().date()) + "-" + str(datetime.now().microsecond) 
        logf = open(filename, "w+")
        logf.write('An exceptional thing happed\n {} \n'.format(e))
        BreakingLoop()

        # Sending mail to webkom with the error message
        send_mail(e)
        
        GPIO.cleanup()
        break
