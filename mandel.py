import math
import sys
from collections import *

width, height = 256, 256

# Named tuple for holding image information
pixel = namedtuple('pixel', ['r', 'g', 'b'])
imageArray = []

magnify = 1.0
max_iterations = 16
# Header infomation:
print("P6")
print str(width)+" "+str(height)+"\n255\n"
for hy in range(0, height):
	for hx in range(0, width):
		c = z = (hx/float(width)-.5)*3-0.7 + (hy/float(height)-.5)*3j
		for i in range(0, (max_iterations + 1)):
			z = z*z+c
			if abs(z)>2:break
		if(i < max_iterations): imageArray.append(pixel(0, 0, i * 4))
		else: imageArray.append(pixel(0, 0, 0))
for i in range(0, len(imageArray)):
	sys.stdout.write("%c%c%c" % (imageArray[i].r,imageArray[i].g,imageArray[i].b))
