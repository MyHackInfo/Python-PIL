from PIL import Image

def main():
    try:
        #Relative Path
        img = Image.open("112.jpg")

        #Angle given
        img = img.rotate(180)

         #Saved in the same relative location
        img.save("rotated_112.jpg")
    except IOError:
        pass

if __name__ == "__main__":
    main()
