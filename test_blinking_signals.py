from blinking_signals import (
    BlinkSuccess,
    Blink401, 
    Blink404, 
    BlinkFifteenMinutes, 
    BlinkServerError, 
    BreakingLoop,
    NoInternet,
    SetUp
)
import time

if __name__ == "__main__":
    print("Setup")
    time.sleep(2)
    SetUp()
    time.sleep(2)

    print("Success")
    time.sleep(2)
    BlinkSuccess()
    time.sleep(2)
    
    print("404 error")
    time.sleep(2)
    Blink404()
    time.sleep(2)
    
    print("401 error")
    time.sleep(2)
    Blink404
    time.sleep(2)
    
    print("Fifteen minutes error")
    time.sleep(2)
    BlinkFifteenMinutes()
    time.sleep(2)

    print("No Internet")
    time.sleep(2)
    NoInternet()
    time.sleep(2)

    print("500 error")
    time.sleep(2)
    BlinkServerError()
    time.sleep(2)

    print("Breaking loop")
    time.sleep(2)
    BreakingLoop()
