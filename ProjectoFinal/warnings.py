import time
import ultrasonicSensor as us

from pythonArduinoConnection import *

# Defining the pins that will be used for the RGB LED.
Red = 9
Green = 10
Blue = 11

# Setting the pins to PWM mode.
board.digital[Red].mode = PWM
board.digital[Green].mode = PWM
board.digital[Blue].mode = PWM

def Warnings(distance):
    """
    If the distance is less than 10, turn on the LED (color red) and turn on the buzzer. 
    If the distance is greater than 10 and less than 20, turn on the LED (color yellow) and turn on the buzzer. 
    If the distance is greater than 30, turn on the LED (on green) and turn on the buzzer. 
    If the distance is None, turn off the LED and the buzzer.
    
    :param distance: The distance in centimeters from the sensor to the object
    """
    # Red
    if distance <= 10:
        board.digital[Red].write(1)
        board.digital[Green].write(0)
        board.digital[Blue].write(0)
        us.Buzzer.tone(3000, 200)
        color = 'RED'
        time.sleep(.5)
    # Yellow
    if distance > 10 and distance <= 20:
        board.digital[Red].write(0.300) #0.300
        board.digital[Green].write(0.5) #0.5
        board.digital[Blue].write(0)
        board.digital[us.Buzzer].write(0.2500)
        time.sleep(.5)
        color = 'YELLOW'
    # Green
    if distance >= 30:
        board.digital[Red].write(0)
        board.digital[Green].write(1)
        board.digital[Blue].write(0)
        board.digital[us.Buzzer].write(0.2000)
        time.sleep(.5)
        color = 'GREEN'
    # Turn off
    if distance is None:
        board.digital[Red].write(0)
        board.digital[Green].write(0)
        board.digital[Blue].write(0)
        board.digital[us.Buzzer].write(0)

