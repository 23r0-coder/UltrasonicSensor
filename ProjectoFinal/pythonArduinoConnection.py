import pyfirmata
from pyfirmata import PWM, Arduino

# The port that the Arduino is connected to.
port = "\\.\COM4"

# Connecting to the Arduino board.
print("Conectando con Arduino por USB...")
board = Arduino(port)
print("Conectado a Arduino por USB.")
