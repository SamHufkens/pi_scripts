import wiringpi
import time

pinLed = 2
pinSwitch = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(pinLed, 1) # Output
wiringpi.pinMode(pinSwitch, 0) # Input



while True:
    if wiringpi.digitalRead(pinSwitch) == 0:
        print("Button Pressed")
        time.sleep(0.5)
        wiringpi.digitalWrite(pinLed, 1)
    else:
        print("Button Released")
        time.sleep(0.5)
        wiringpi.digitalWrite(pinLed, 0)