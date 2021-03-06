from altimeter import altitude
from altimeter import altitude
from altimeter import calibrate
from adxl345 import ADXL345
import time

adxl = ADXL345()
start = time.time()
alt = [0]
accel = [0]
#calibrate()
for i in range(10):
	#alt.append(altitude())
	#accel.append(adxl.getAxes(False)))
	now = time.time()
	with open("data.txt", 'a', encoding = 'utf-8') as f:
		f.write(str(altitude()))
		f.write(" ")
		axes = adxl.getAxes(False)
		f.write(str(axes['x']))
		f.write(" ")
		f.write(str(axes['y']))
		f.write(" ")
		f.write(str(axes['z']))
		f.write("\n")
	while time.time()-now < 0.1: #wait 100 ms between readings
		pass
print("It is finished")
