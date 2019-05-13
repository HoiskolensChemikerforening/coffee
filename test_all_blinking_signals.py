from blinking_signals import SetUp
from blinking_signals import Blink401
from blinking_signals import Blinkbreakloop
from blinking_signals import Blink404 
from blinking_signals import NoInternet 
from blinking_signals import BlinkServerError 
from blinking_signals import BlinkFifteenMinutes

import time
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



