import sys
from collections import *

# Width an height of output image
width, height = 1024, 1024

# Named tuple for holding pixel information
pixel = namedtuple('pixel', ['r', 'g', 'b'])
imageArray = []

magnify = 1.0
max_iterations = 32
# Header infomation:
print("P6")
# width and height are image size
# 255 (third number) is color depth of output image.
print str(width)+" "+str(height)+"\n255\n"
# Go through each pixel in the image:
for hy in range(0, height):
	for hx in range(0, width):
		c = z = (hx/float(width)-.5)*3-0.7 + (hy/float(height)-.5)*3j
		# max_iterations + 1 to make sure we _can_ reach max_iterations:
		for i in range(0, (max_iterations + 1)):
			z = z*z+c
			# if it is diviriging, break
			if abs(z)>2:break
		# Make the edge of the set colored. (R, G, B)
		if(i < max_iterations):
			temp = i * 16
			if temp > 255: temp = 255
			imageArray.append(pixel(0, 0, temp))
		#It is is in the set, color it black
		else: imageArray.append(pixel(0, 0, 0))
# Once we have all of the pixels in the image processed, output their values:
for i in range(0, len(imageArray)):
	sys.stdout.write("%c%c%c" % (imageArray[i].r,imageArray[i].g,imageArray[i].b))
