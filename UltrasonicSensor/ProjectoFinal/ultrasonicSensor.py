import time

import pulsein
from pythonArduinoConnection import *

# Defining the pins that will be used for the Sensor.
Buzzer = 13
Sensor_Trigger = 5
Sensor_Echo = 6
sound = 34300

def Start_Trigger():
    """
    It sends a signal to the sensor to start the measurement.
    """
    board.digital[Sensor_Trigger].write(0)
    time.sleep(0.0002)
    board.digital[Sensor_Trigger].write(1)
    time.sleep(0.0001)
    board.digital[Sensor_Trigger].write(0)

def CalcDistance():
    """
    Calculate the distance of the object in front of the sensor by measuring the time it takes for the
    sound to bounce back to the sensor
    :return: The distance in cm
    """
    time = pulsein.pulseIn(Sensor_Echo)
    distance = (time * 0.000001 * sound) / (2.0)
    time.sleep(0.5)
    return distance

