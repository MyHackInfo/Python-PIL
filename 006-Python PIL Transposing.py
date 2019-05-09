from PIL import Image

def main():
    try:
        #Relative Path
        img = Image.open("112.jpg")

        #transposing image
        transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

        #Save transposed image
        transposed_img.save("transposed_112.jpg")
    except IOError:
        pass

if __name__ == "__main__":
    main()
