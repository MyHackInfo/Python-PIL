# Image Derivatives

# How the image intensity changes over the image is important information and is used for many applications
# These derivative filters are easy to implement using the standard convolution available in the scipy.ndimage.filters module



from PIL import Image
from numpy import *
from scipy.ndimage import filters


img= array(Image.open('light.jpg').convert('L'))
img1= array(Image.open('light.jpg'))

# Sobel derivative filters
imx = zeros(img.shape)
filters.sobel(img,1,imx)

imy = zeros(img.shape)
filters.sobel(img,1,imy)
magnitude = sqrt(imx**2+imy**2)

imags=Image.fromarray(magnitude)
imags.show()


