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


class AverageFilter(Filter):
    def __init__(self, image, name, kernel_size):
        super().__init__(image, name, kernel_size)

    def apply(self):
        k = self.kernel_size
        return cv.blur(self.image, (k,k))


class GaussianBlur(Filter):
    def __init__(self, image, name, kernel_size, sigma_x, sigma_y=0):
        self.sigma_x = sigma_x
        self.sigma_y = sigma_y
        super().__init__(image, name, kernel_size)

    def apply(self):
        k = self.kernel_size
        return cv.GaussianBlur(self.image, (k,k), self.sigma_x, self.sigma_y )


class MedianBlur(Filter):
    def __init__(self, image, name, kernel_size):
        super().__init__(image,name,kernel_size)

    def apply(self):
        return cv.medianBlur(self.image, self.kernel_size)

class BilateralFilter(Filter):
    def __init__(self, image, name, kernel_size, diameter, sigma_color, sigma_space):
        self.diameter = diameter
        self.sigma_color = sigma_color
        self.sigma_space = sigma_space
        super().__init__(image,name,kernel_size)

    def apply(self):
        return cv.bilateralFilter(self.image,self.diameter,self.sigma_color,self.sigma_space)