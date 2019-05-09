import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

i = Image.open('dotndot.png')
iar = np.asarray(i)

plt.imshow(iar)
plt.show()
