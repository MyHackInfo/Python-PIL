# Morphology --Counting Objects

'''
Morphology (or mathematical morphology) is a framework and a collection of image
processing methods for measuring and analyzing basic shapes. Morphology is usually
applied to binary images but can be used with grayscale also

# Morphological operations are included in the scipy.ndimage module morphology
# Counting and measurement functions for binary images are in the scipy.ndimage module measurements

http://en.wikipedia.org/wiki/Mathematical_morphology
'''


from PIL import Image
from numpy import *
from scipy.ndimage import measurements, morphology

# load image and threshold to make sure it is binary
im = array(Image.open('hours.png').convert('L'))
im = 1*(im<128)

labels,nbr_objects = measurements.label(im)
print("number of objects:",nbr_objects)


# Morphology - opening to separate objects better
im_open = morphology.binary_opening(im,ones((9,5)),iterations=2)
labels_open, nbr_objects_open = measurements.label(im_open)
print("number of objects:",nbr_objects_open)







