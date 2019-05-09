'''
The Python Imaging Library (PIL) provides general image handling and lots of useful
basic image operations like resizing, cropping, rotating, color conversion and much
more.

The most important module is the Image module.


1- pip install Pillow
2- pip install PIL


'''

from PIL import Image

img = Image.open('light.jpg')

# Color conversions are done using the convert() method.
# To read an image and convert it to grayscale, just add convert('L') like this.
img = Image.open('light.jpg').convert('L')


img.show()
