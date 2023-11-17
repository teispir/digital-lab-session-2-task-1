from microbit import *
ledState = 0
interval = 0
pauseMillis = 0
while True:
    timeMillis = running.time()
    
    if timeMillis – pauseMillis >= interval:
        pauseMillis = timeMillis
    if ledState == 0:
        ledState = 1
    else:
        ledState = 0
        pin0.write_digital(ledState)
