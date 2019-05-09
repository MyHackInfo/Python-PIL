# Numpy array()

# Arrays in NumPy are multi-dimensional and can represent vectors, matrices, and images.
# An array is much like a list (or list of lists) but is restricted to having all elements of the same type.
# Unless specified on creation, the type will automatically be set depending on the data

# PyLab actually includes some components of NumPy, like the array type. 

from PIL import Image
from pylab import *
#from numpy import *

im = array(Image.open('light.jpg'))
print(im.shape, im.dtype)

im = array(Image.open('light.jpg').convert('L'),'f')
print(im.shape, im.dtype)


# The first tuple on each line is the shape of the image array (rows, columns, color
# channels), and the following string is the data type of the array elements. Images
# are usually encoded with unsigned 8-bit integers (uint8), so loading this image and
# converting to an array gives the type “uint8” in the first case


#The second case does
#grayscale conversion and creates the array with the extra argument “f”. This is a short
#command for setting the type to floating point. For more data type options, see [24].
#Note that the grayscale image has only two values in the shape tuple; obviously it has
#no color information.
