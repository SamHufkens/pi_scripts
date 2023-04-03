"""import wiringpi

W3 = 3
W4 = 4
W6 = 6
W9 = 9 

#wave_seq = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
full_seq = [[1,0,1,0],[0,1,1,0],[0,1,0,1],[1,0,0,1]]


wiringpi.wiringPiSetup()
wiringpi.pinMode(W3, 1)
wiringpi.pinMode(W4, 1)
wiringpi.pinMode(W6, 1)
wiringpi.pinMode(W9, 1)


wiringpi.digitalWrite(W3, 0)
wiringpi.digitalWrite(W4, 0)
wiringpi.digitalWrite(W6, 0)
wiringpi.digitalWrite(W9, 0)


def set_step(step):
    wiringpi.digitalWrite(W3, step[0])
    wiringpi.digitalWrite(W4, step[1])
    wiringpi.digitalWrite(W6, step[2])
    wiringpi.digitalWrite(W9, step[3])


for i in range(512): 
    set_step(full_seq[i%4]) 
    wiringpi.delay(10) 


wiringpi.digitalWrite(W3, 0)
wiringpi.digitalWrite(W4, 0)
wiringpi.digitalWrite(W6, 0)
wiringpi.digitalWrite(W9, 0)"""

import wiringpi
import time

# Set up pins
W3 = 3
W4 = 4
W6 = 6
W9 = 9

# Set up the step sequence
sequence = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

# Set up the motor control
wiringpi.wiringPiSetup()
wiringpi.pinMode(W3, 1)
wiringpi.pinMode(W4, 1)
wiringpi.pinMode(W6, 1)
wiringpi.pinMode(W9, 1)



# Set initial step to 0
stepRight = 0

# Move 30 steps to the right
for i in range(90):
    # Set the GPIO pins based on the current step
    wiringpi.digitalWrite(W3, sequence[stepRight][0])
    wiringpi.digitalWrite(W4, sequence[stepRight][1])
    wiringpi.digitalWrite(W6, sequence[stepRight][2])
    wiringpi.digitalWrite(W9, sequence[stepRight][3])

    # Increment or decrement the step based on the direction
    stepRight += 1
    if stepRight == len(sequence):
        stepRight = 0

    # Delay between steps
    wiringpi.delay(5)
    

# Set initial step to 0
stepLeft = 0

# Move 30 steps to the left
for i in range(90):
    # Set the GPIO pins based on the current step
    wiringpi.digitalWrite(W3, sequence[stepLeft][0])
    wiringpi.digitalWrite(W4, sequence[stepLeft][1])
    wiringpi.digitalWrite(W6, sequence[stepLeft][2])
    wiringpi.digitalWrite(W9, sequence[stepLeft][3])

    # Decrement or increment the step based on the direction
    stepLeft -= 1
    if stepLeft < 0:
        stepLeft = len(sequence) - 1

    # Delay between steps
    wiringpi.delay(5)


# Clean up GPIO pins
wiringpi.digitalWrite(W3, 0)
wiringpi.digitalWrite(W4, 0)
wiringpi.digitalWrite(W6, 0)
wiringpi.digitalWrite(W9, 0)



