import pyfirmata
from pyfirmata import Arduino, PWM
import time

# The port that the Arduino is connected to.
port = "\\.\COM4"

# Connecting to the Arduino board.
print("Conectando con Arduino por USB...")
board = Arduino(port)
print("Conectado a Arduino por USB.")

# Defining the pins that will be used for the RGB LED.
Red = 9
Green = 10
Blue = 11

# Defining the pins that will be used for the Sensor.
Sensor_Buzzer = 13
Sensor_Trigger = 5
Sensor_Echo = 6
sound = 34300

# Setting the pins to PWM mode.
board.digital[Red].mode = PWM
board.digital[Green].mode = PWM
board.digital[Blue].mode = PWM

def Led_Warning(distance):
    """
    The function takes the distance as an input and then uses the distance to determine which LED to
    turn on
    
    :param distance: The distance in centimeters that the sensor is reading
    """
    # Red
    if distance <= 10:
        board.digital[Red].write(1)
        board.digital[Green].write(0)
        board.digital[Blue].write(0)
        time.sleep(.5)
    # Yellow
    if distance > 10 and distance <= 20:
        board.digital[Red].write(1) #0.300
        board.digital[Green].write(1) #0.5
        board.digital[Blue].write(0)
        time.sleep(.5)
    # Green
    if distance >= 30:
        board.digital[Red].write(0)
        board.digital[Green].write(1)
        board.digital[Blue].write(0)
        time.sleep(.5)

def Start_Trigger():
    """
    It sends a signal to the sensor to start the measurement.
    """
    board.digital[Sensor_Trigger].write(0)
    time.sleep(0.0002)
    board.digital[Sensor_Trigger].write(1)
    time.sleep(0.01)

def CalcDistance():
    duration = pulsein.pulseIn(Sensor_Echo)

while True:
    Start_Trigger()
    Led_Warning(10)
    Led_Warning(15)
    Led_Warning(30)
board.exit()