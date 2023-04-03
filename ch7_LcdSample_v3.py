import time
import wiringpi
import spidev
from ch7_ClassLCD import LCD

def ActivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 0)       # Activate LCD using CS
    time.sleep(0.000005)

def DeactivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 1)       # Deactivate LCD using CS
    time.sleep(0.000005)

# Define the pinout for the LCD display
PIN_OUT     =   {  
                'SCLK'  :   14,
                'DIN'   :   11,
                'DC'    :   9, 
                'CS'    :   15, # We will not connect this pin! --> we use w13
                'RST'   :   10,
                'LED'   :   6, # backlight   
}

# Use w13 (pin 22) as chip select
pin_CS_lcd = 13
wiringpi.wiringPiSetup() 
wiringpi.wiringPiSPISetupMode(1, 0, 400000, 0)  #(channel, port, speed, mode)
wiringpi.pinMode(pin_CS_lcd , 1)            # Set pin to mode 1 (OUTPUT)

# Create an instance of the LCD class
lcd_1 = LCD(PIN_OUT)

# Initialize LCD and display "hello"
lcd_1.clear()
lcd_1.set_backlight(1)
ActivateLCD()
lcd_1.put_string('hello')
lcd_1.refresh()
DeactivateLCD()

while True:
    # Wait for user input
    user_input = input("Press 'k' to quit: ")
    if user_input == 'k':
        ActivateLCD()
        lcd_1.clear()
        lcd_1.refresh()
        lcd_1.set_backlight(0)
        DeactivateLCD()
        print("\nProgram terminated")
        break




