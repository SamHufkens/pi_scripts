import wiringpi
import time
print("Start")
pinSwitch = 1 
wiringpi.wiringPiSetup()
wiringpi.pinMode(pinSwitch, 0)
 
while True:
    if(wiringpi.digitalRead(pinSwitch) == 0):
        print("Button Pressed")
        time.sleep(0.3) 
    else:
        print("Button released")
        time.sleep(0.3)