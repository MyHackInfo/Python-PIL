# Rotate Image

# To rotate an image, use counterclockwise angles and rotate() method.

from PIL import Image

def main():
    try:
        #Relative Path
        img = Image.open("light.jpg")

        #Angle given
        img = img.rotate(140)

         #Saved in the same relative location
        img.save("rotated_light.jpg")
    except IOError:
        pass

if __name__ == "__main__":
    main()
