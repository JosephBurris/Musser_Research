#The code that my brother wrote for the short test

from drone import *

test = Drone("192.168.10.1", 8889)
test.connect()
test.command()
test.takeoff()
test.land()
test.disconnect()
