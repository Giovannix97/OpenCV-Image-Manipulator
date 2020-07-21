import cv2 as cv
from matplotlib import pyplot as plt

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


    def canny_edge_detection(self,threshold_1,threshold_2):
        return cv.Canny(self.image, threshold_1, threshold_2)


    def show_histogram(self):
        """
            Show the color histogram for the specified image
            :param:
            :return:
        """
        color = ('b', 'g', 'r')

        for i, col in enumerate(color):
            histr = cv.calcHist([self.image], [i], None, [256], [0, 256])
            plt.plot(histr, color=col)
            plt.xlim([0, 256])
        plt.show()