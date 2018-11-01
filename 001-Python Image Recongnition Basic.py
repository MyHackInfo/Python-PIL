'''

1- pip install Pillow

'''

from PIL import Image
import numpy as np

i = Image.open('dot.png')
iar = np.asarray(i)
print(iar)
