import time
import warnings

import psycopg2 as db

import lcd
import pulsein
import ultrasonicSensor as us
from pythonArduinoConnection import *

while True:
    
    #Start sensor
    us.Start_Trigger()
    distance = us.CalcDistance()

    #Start warnings
    info = warnings.Warnings(distance)


    #Trial values
    # Warnings(15)
    # Warnings(30)
    db.sendData(info)
board.exit()
