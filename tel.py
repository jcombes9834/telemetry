from altimeter import altitude
import time

temp = time.time()

for i in range(100):
	print(altitude())
	now = time.time()
	while time.time()-now < 0.03:
		pass

print("It is finished")
