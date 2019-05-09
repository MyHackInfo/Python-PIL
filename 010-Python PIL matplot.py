from PIL import Image
from pylab import *

'''
#read image to array
im = array(Image.open('light.jpg'))

#plot the image
imshow(im)


# some points
x= [100,100,400,400]
y =[200,500,200,500]

# plot the points with red star-markers
plot(x,y,'r*')

# line plot connecting the first two points
plot(x[:2],y[:2])

# add title and show the plot
title('Plotting: "light.jpg"')
show()

axis('off')
'''

'''
im = array(Image.open('light.jpg'))
imshow(im)
print('please 4 points')
x = ginput(3)
print('you cliked:',x)
show()
'''
