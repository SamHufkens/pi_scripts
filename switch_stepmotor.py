import wiringpi
import time

pinSwitch = 1
W3 = 3
W4 = 4
W6 = 6
W9 = 9

full_seq = [[1,0,1,0],[0,1,1,0],[0,1,0,1],[1,0,0,1]]

dir = 1


wiringpi.wiringPiSetup()
wiringpi.pinMode(W3, 1)
wiringpi.pinMode(W4, 1)
wiringpi.pinMode(W6, 1)
wiringpi.pinMode(W9, 1)
wiringpi.pinMode(pinSwitch, 0)


wiringpi.digitalWrite(W3, 0)
wiringpi.digitalWrite(W4, 0)
wiringpi.digitalWrite(W6, 0)
wiringpi.digitalWrite(W9, 0)


def set_step(step):
    wiringpi.digitalWrite(W3, step[0])
    wiringpi.digitalWrite(W4, step[1])
    wiringpi.digitalWrite(W6, step[2])
    wiringpi.digitalWrite(W9, step[3])

i = 0
while True:
    if(wiringpi.digitalRead(1) == 0): # Check if the switch is pressed
        dir = -1 if dir == 1 else 1 # Change the direction of rotation
        while(wiringpi.digitalRead(1) == 0): # Wait for the switch to be released
            pass
    set_step(full_seq[i%4]) # Set the GPIO pins to the appropriate state
    i = (i + dir) % 4 # Update the step counter based on the direction of rotation
    wiringpi.delay(10) # Delay for 10ms between steps
