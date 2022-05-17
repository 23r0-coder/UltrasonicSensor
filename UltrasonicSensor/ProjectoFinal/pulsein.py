import time

def pulseIn(pin):
    """
    It waits for the pin to go low, then starts timing until the pin goes high again
    
    :param pin: The pin to read the signal from
    :return: The time in microseconds that the pin was high.
    """
    while not pin.read():
#	print "High"
        continue
    # Went down, let start measure
    start = time.time()

    while pin.read():
        continue

    end = time.time()
    return (end - start) *1000000