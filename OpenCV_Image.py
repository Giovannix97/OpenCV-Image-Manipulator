import cv2 as cv
from matplotlib import pyplot as plt

class OpenCV_Image:
    """A simple wrapper to extend the features of the classic Open-CV image."""
    def __init__(self, path, mode=1):
        """

        :param path: The path(string) in which the image is stored. Don't forget to add the image name and extension.
                     For example MyFolder/my_image.jpg
        :param mode: Numeric value (1,0,-1) corresponding to the flags
                    cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
                    cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
                    cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

        """
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

    def show(self, title):
        """Show in a new window the image selected."""
        cv.imshow(title, self.image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def save(self, name, extension):
        """Save the current image with the specified name and extension."""
        try:
            cv.imwrite(name + "." + extension, self.image)
            print("Image saved successfully.")
        except:
            print("Error while saving image!")

    def get_opencv_image(self):
        """Return the homonym class attribute, or rather an OpenCV image."""
        return self.image

    def set_opencv_image(self, opencv_image):
        self.image = opencv_image

    def canny_edge_detection(self, threshold_1, threshold_2):
        """Apply Canny algorithm to the image. It is useful to detect the edges of the image.
        Try to change the two parameters to have different results.

        :param threshold_1: Numeric value that represents the first threshold used in the algorithm.
        :param threshold_2: Numeric value that represents the second threshold used in the algorithm.
        :return: An image in which the outlines are highlighted.
        """
        return cv.Canny(self.image, threshold_1, threshold_2)

    def show_histogram(self):
        """
            Show the color histogram for the specified image
            :param:
            :return: Show the histogram of the chosen image.
        """
        color = ('b', 'g', 'r')

        for i, col in enumerate(color):
            histr = cv.calcHist([self.image], [i], None, [256], [0, 256])
            plt.plot(histr, color=col)
            plt.xlim([0, 256])
        plt.show()