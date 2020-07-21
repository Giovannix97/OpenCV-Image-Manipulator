from Filter import *


class AverageFilter(Filter):
    def __init__(self, image, name, kernel_size):
        super().__init__(image, name, kernel_size)

    def apply(self):
        k = self.kernel_size
        return cv.blur(self.image, (k,k))

