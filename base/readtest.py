from altimeter import altitude
import time

temp = time.time()

while True:
	now = time.time()
	alt = altitude()
	newAlt = altitude()
	if  newAlt != alt:
		readTime = time.time() - now
		print(readTime*1000)
		break

print("time in milliseconds")
print((time.time()-temp)*1000)
