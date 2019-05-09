# Resize image

# To resize an image, call resize() with a tuple giving the new size.

from PIL import Image

img = Image.open('light.jpg')
out = img.resize((1900,1260))

out.show()
