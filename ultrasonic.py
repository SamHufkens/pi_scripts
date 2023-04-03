import wiringpi
import sys
import time

trgpin = 1
echopin = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(trgpin, 1)
wiringpi.pinMode(echopin, 0)

while True:
    wiringpi.digitalWrite(trgpin, 1)
    time.sleep(0.00001)
    wiringpi.digitalWrite(trgpin, 0)
    while wiringpi.digitalRead(echopin) == 0:
        time_start = time.time()
    while wiringpi.digitalRead(echopin) == 1:
        time_end = time.time()
    time_elapsed = time_end - time_start
    distance = int(time_elapsed * 17000)
    print(f"Distance: {distance} cm")
    time.sleep(0.5)

# cleanup
print("done")
