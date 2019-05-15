from blinking_signals import (
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
    Print("Setup")
    SetUp()
    time.sleep(1)
    
    print("404 error")
    Blink404()
    time.sleep(1)
    
    print("401 error")
    Blink404
    time.sleep(1)
    
    print("Fifteen minutes error")
    BlinkFifteenMinutes()
    time.sleep(1)

    print("No Internet")
    NoInternet()
    time.sleep()

    print("500 error")
    BlinkServerError()
    time.sleep(1)

    print("Breaking loop")
    BreakingLoop()
