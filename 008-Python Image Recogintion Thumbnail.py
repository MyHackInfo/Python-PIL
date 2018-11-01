from PIL import Image
def main():
    try:
        #Relative Path
        img = Image.open("112.jpg")

        #In-place modification
        img.thumbnail((200, 200))

        img.save("thumb_112.jpg")
    except IOError:
        pass

if __name__ == "__main__":
    main()
