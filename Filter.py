import cv2 as cv
from OpenCV_Image import  *

class Filter:
    def __init__(self, image, name, kernel_size):
        self.image = image
        self.name = name
        self.kernel_size = kernel_size

    def get_name(self):
        return self.name

    def set_name(self,new_name):
        self.name = new_name

    def get_image(self):
        return self.image

    def set_image(self, new_image):
        self.image = new_image

    def get_kernel_size(self):
        return self.kernel_size

    def set_kernel_size(self,new_size):
        self.kernel_size = new_size

    def apply(self):
        pass