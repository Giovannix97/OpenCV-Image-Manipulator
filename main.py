from Image import *

IMAGE_PATH = 'Images/lena.jpg'

def main():

    lena_image= OpenCV_Image(IMAGE_PATH,1)
    lena_image.show("A beatiful girl: Lena!")

if __name__ == '__main__':
    main()