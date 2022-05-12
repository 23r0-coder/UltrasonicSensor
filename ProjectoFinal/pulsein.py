import time

def pulseIn(pin):
    while not pin.read():
#	print "High"
        continue
    # Went down, let start measure
    start = time.time()

    while pin.read():
        continue

    end = time.time()
    return (end - start) *1000000