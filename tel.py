from altimeter import altitude
from altimeter import altitude
from adxl345 import ADXL345
import time

adxl = ADXL345()
start = time.time()

for i in range(100):
	print(altitude(), adxl.getAxes(False))
	now = time.time()
	while time.time()-now < 0.1: #wait 100 ms between readings
		pass

print("It is finished")
