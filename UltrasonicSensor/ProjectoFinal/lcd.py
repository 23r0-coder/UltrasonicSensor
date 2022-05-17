from pythonArduinoConnection import *

# Defining the pins that will be used for the LCD.
lcd  = (3,4,7,8)

#FIX LCD ------------- it's not printing info

def printDistance(distance):
    """
    It takes the distance value and prints it on the second line of the LCD display
    
    :param distance: The distance in centimeters to the object
    """
    lcd.setcursor(0,1)
    lcd.print(distance)
    lcd.setcursor(10,1)
    lcd.print("cm")