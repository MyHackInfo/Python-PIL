# Histogram Equalization

# A very useful example of a graylevel transformis histogramequalization.
# This transformflattens the graylevel histogramof an image so that all intensities are as equally commonas possible

# This is often a good way to normalize image intensity before further
# processing and also a way to increase image contrast

# The transform function is, in this case, a "cumulative distribution function (cdf)" of the
# pixel values in the image (normalized to map the range of pixel values to the desired range).


from PIL import Image
from numpy import *



def histeq(im, nbr_bins=256):
    # Histogram equalization of a grayscale image.

    # get image histogram
    imhist,bins = histogram(im.flatten(), nbr_bins,normed = True)
    cdf = imhist.cumsum() # cumlative distribution function
    cdf = 255 * cdf / cdf[-1]  #normalize

    # use linear interpolation of cdf to find new pixel values
    im2 = interp(im.flatten(), bins[:-1],cdf)

    return im2.reshape(im.shape),cdf


im = array(Image.open('light.jpg').convert('L'))
img2,cdf = histeq(im)

imgs = Image.fromarray(img2)
print(imgs.show())


    
    


















'''
from PIL import Image

def main():
    try:
         #Relative Path
        img = Image.open("light.jpg")
        
        #Getting histogram of image
        print (img.histogram())
    except IOError:
        pass

if __name__ == "__main__":
    main()
'''
