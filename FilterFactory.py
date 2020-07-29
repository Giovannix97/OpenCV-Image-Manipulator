from Filter import *

class FilterFactory:
    def __init__(self,):
        pass

    @classmethod
    def get_filter(cls, image, filter_name, kernel_size, *args):
        """Choose from different filters to apply to the image.

        :param image: An input image.
        :param filter_name: A string representing the name of the chosen filter.
        :param kernel_size: Size of the kernel(matrix) in the number of rows and columns. It must be an odd number
        equals o greater than 3. For example 3,5,7...
        :param args: Optional arguments used for the Gaussian and the Bilateral filters.
        :return: Output image in which the filter has been applied.
        """
        if filter_name.lower() == "average":
            return AverageFilter(image, filter_name, kernel_size)
        elif filter_name.lower() == "gaussian":
            sigma_x = args[0]
            sigma_y = args[1]
            return GaussianBlur(image, filter_name, kernel_size, sigma_x, sigma_y)
        elif filter_name.lower() == "median":
            return MedianBlur(image, filter_name, kernel_size)
        elif filter_name.lower() == "bilateral":
            diameter = args[0]
            sigma_color = args[1]
            sigma_space = args[2]
            return BilateralFilter(image, filter_name, kernel_size, diameter, sigma_color, sigma_space)
        else:
            raise Exception("Please specify a correct filter!\n"
                            "Check if the name of the chosen filter is correct.")

