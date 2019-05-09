# Graylevel Transforms
# After reading images to NumPy arrays, we can perform any mathematical operation we like on them
# interval 0 . . . 255.


from PIL import Image
from numpy import *

img = array(Image.open('light.jpg').convert('L'))
img0 = array(Image.open('light.jpg'))

img = 52 -img0
img1 = (100.0/255) * img +100
print(img1)
img2 = 255.0 * (img/255.0) ** 2

# The reverse of the array() transformation can be done using the PIL function fromarray().

imgs = Image.fromarray(img)
print(imgs.show())



