import wiringpi


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
wiringpi.digitalWrite(W9, 0)
