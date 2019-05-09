# Create Thumbnails

# Using PIL to create thumbnails is very simple.
# The thumbnail() method takes a tuple specifying the new size and converts the image to a thumbnail image with size that fits within the tuple

from PIL import Image
def main():
    try:
        #Relative Path
        img = Image.open("light.jpg")

        #In-place modification
        img.thumbnail((128, 128))

        img.save("thumb_112.jpg")
    except IOError:
        pass

if __name__ == "__main__":
    main()
