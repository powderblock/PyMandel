import math
import sys
from collections import *

width = 64; height = 64
imageSize = width * height

# Named tuple for holding image information
pixel = namedtuple('pixel', ['r', 'g', 'b'])
imageArray = []

magnify = 1.0
max_iterations = 64
# Header infomation:
print("P6")
print str(width)+" "+str(height)+"\n255\n"
for hy in range(0, height):
    for hx in range(0, width):
        cx = ((float(hx) / float(width)) - 0.5) / magnify*3.0-0.7
        cy = ((float(hy) / float(height)) - 0.5) / magnify*3.0
        zx = cx
        zy = cy
        for i in range(0, max_iterations):
            tmp = zx * zx - zy * zy + cx;
            zy = (2.0 * zx)*zy+cy;
            zx = tmp;
            if(zx * zx + zy * zy > 4.0): break
        if(i < max_iterations): imageArray.append(pixel(0, 0, i * 4))
        else: imageArray.append(pixel(0, 0, 0))
for i in range(0, len(imageArray)):
    sys.stdout.write("%c%c%c" % (imageArray[i].r,imageArray[i].g,imageArray[i].b))
