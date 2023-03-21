import wiringpi
import time

print("Start")
ldr_pin = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(ldr_pin, 0)

while True:
    print(wiringpi.analogRead(ldr_pin))
    time.sleep(1)
    """if (wiringpi.digitalRead(ldr_pin) == 0):
        print("Dark")
        time.sleep(0.5)
    else:
        print("Light")
        time.sleep(0.5)"""