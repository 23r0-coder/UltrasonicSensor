import time
import warnings
from pythonArduinoConnection import *
import pulsein
import lcd

def CalcDistance():
    """
    Calculate the distance of the object in front of the sensor by measuring the time it takes for the
    sound to bounce back to the sensor
    :return: The distance in cm
    """
    # Fix pulsein
    time = pulsein.pulseIn(warnings.Sensor_Echo)
    distance = (time * 0.000001 * warnings.sound) / (2.0)
    time.sleep(0.5)
    return distance

def SaveData(distance):
    print()


#Main process
while True:
    #warnings.Start_Trigger()
    warnings.Warnings(10)
    # Warnings(15)
    # Warnings(30)
board.exit()
