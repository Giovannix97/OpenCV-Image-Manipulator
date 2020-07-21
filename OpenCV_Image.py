import cv2 as cv
class OpenCV_Image:
    def __init__(self,path,mode=1):
        self.path = path
        self.image = cv.imread(path,mode)
        self.height = self.get_height()
        self.width = self.get_width()
        self.color_levels = self.get_color_levels()


    def get_height(self):
        return self.image.shape[0]

    def get_width(self):
        return self.image.shape[1]

    def get_color_levels(self):
        return self.image.shape[2]

    def show(self,title):
        cv.imshow(title,self.image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def save(self,name,extension):
        try:
            cv.imwrite(name + "." + extension, self.image)
            print("Image saved successfully.")
        except:
            print("Error while saving image!")


    def get_opencv_image(self):
        return self.image

    def set_opencv_image(self,opencv_image):
        self.image = opencv_image