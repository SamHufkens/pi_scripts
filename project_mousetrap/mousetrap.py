import wiringpi
import time
import spidev
import requests
import json
from classLCD import LCD

def stepmotor(SEQ, pin3, pin4, pin6, pin9):
    for i in range(50):
        for j in range(8):
            wiringpi.digitalWrite(pin3, SEQ[j][0])
            wiringpi.digitalWrite(pin4, SEQ[j][1])
            wiringpi.digitalWrite(pin6, SEQ[j][2])
            wiringpi.digitalWrite(pin9, SEQ[j][3])
            time.sleep(0.001)
    
    for i in range(50):
        for j in range(7, -1, -1):
            wiringpi.digitalWrite(pin3, SEQ[j][0])
            wiringpi.digitalWrite(pin4, SEQ[j][1])
            wiringpi.digitalWrite(pin6, SEQ[j][2])
            wiringpi.digitalWrite(pin9, SEQ[j][3])
            time.sleep(0.001)
    
    wiringpi.digitalWrite(W3, 0)
    wiringpi.digitalWrite(W4, 0)
    wiringpi.digitalWrite(W6, 0)
    wiringpi.digitalWrite(W9, 0)

def ActivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 0)       
    time.sleep(0.000005)

def DeactivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 1)      
    time.sleep(0.000005)

trap_triggerd = False
trap_count = 0


def send_ubeac_data(distance):
    global status, trap_count
    url = "http://samhufkens.hub.ubeac.io/iotessSam"
    uid = "iotessSam"
    data = {
            "id": uid,
            "sensors": [{
                "id": "mouse_trap_status",
                "data": {
                    "count": trap_count,
                    "distance": distance
                }}   
            ]
        }
    headers = {"Content-Type": "application/json"}
    res = requests.post(url, headers=headers, json=data)

    if res.status_code == 200:
        print("Data Succesfully Send To uBeac")
    else:
        print("Something Went Wrong With uBeac!")
        


# PINS stepmotor
W3 = 3
W4 = 4
W6 = 6
W9 = 9

# PINS ultrasonic sensor
W1 = 1
W2 = 2

# PIN button
W0 = 0

# PINS LCD
PIN_OUT = {  
    'SCLK'  :   14,
    'DIN'   :   11,
    'DC'    :   16, 
    'CS'    :   15, 
    'RST'   :   10,
    'LED'   :   8, 
}
pin_CS_lcd = 13

wiringpi.wiringPiSetup()
wiringpi.wiringPiSPISetupMode(1, 0, 400000, 0)

# LCD PINMODE
wiringpi.pinMode(pin_CS_lcd , 1)

# stepmotor PINMODE
wiringpi.pinMode(W3, 1)
wiringpi.pinMode(W4, 1)
wiringpi.pinMode(W6, 1)
wiringpi.pinMode(W9, 1)

# ultrasonic PINMODE
wiringpi.pinMode(W1, 1)
wiringpi.pinMode(W2, 0)

# button PINMODE
wiringpi.pinMode(W0, 0)

# stepmotor sequence
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

distances = [21, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30]

lcd_1 = LCD(PIN_OUT)


lcd_1.clear()
lcd_1.set_backlight(1)
ActivateLCD()
lcd_1.put_string('Trap Active')
lcd_1.refresh()
DeactivateLCD()


while True:
    wiringpi.digitalWrite(W1, 1)
    time.sleep(0.00001)
    wiringpi.digitalWrite(W1, 0)
    while wiringpi.digitalRead(W2) == 0: 
        time_start = time.time()
    while wiringpi.digitalRead(W2) == 1:
        time_end = time.time()
    time_elapsed = time_end - time_start
    distance = int(time_elapsed * 17000)
    print(f"Distance: {distance} cm")
    time.sleep(0.5)

    
    if distance in distances or wiringpi.digitalRead(W0) == 0 and not trap_triggerd:
        stepmotor(sequence, W3, W4, W6, W9)
        ActivateLCD()
        lcd_1.clear()
        lcd_1.refresh()
        lcd_1.set_backlight(0)
        DeactivateLCD()


        trap_triggerd = True
        trap_count += 1
        send_ubeac_data(distance)
        print("Mouse Caught!")
        break


