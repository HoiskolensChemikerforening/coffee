from blinking_signals import SetUp
from blinking_signals import blink401 
from blinking_signals import blinkbreakloop 
from blinking_signals import blink404 
from blinking_signals import NoInternet 
from blinking_signals import blinkServerError 
from blinking_signals import blinkFifteenMinutes

import time
SetUp()
time.sleep(1)
blink401()
time.sleep(1)
blinkbreakloop()
time.sleep(1)
blink404()
time.sleep(1)
NoInternet()
time.sleep(1)
blinkServerError()
time.sleep(1)
blinkFifteenMinutes()



