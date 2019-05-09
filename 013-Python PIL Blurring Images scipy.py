# Blurring Images

# A classic and very useful example of image convolution is Gaussian blurring of images
# SciPy comes with a module for filtering called scipy.ndimage.
# filters that can be used to compute these convolutions using a fast 1D separation

import numpy as np
from PIL import Image
from numpy import *
from scipy.ndimage import gaussian_filter
a = np.arange(50,step=2).reshape((5,5))

img= array(Image.open('light.jpg').convert('L'))
img1= array(Image.open('light.jpg'))
val = gaussian_filter(img1, sigma=2)


imags=Image.fromarray(val)
imags.show()


