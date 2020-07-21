from Filter import *

class FilterFactory:
    def __init__(self,):
        pass

    @classmethod
    def get_filter(self, filter_name, image, name, kernel_size, *args):
        if filter_name.lower() == "average":
            return AverageFilter(image,name,kernel_size)
        elif filter_name.lower() == "gaussian":
            sigma_x = args[0]
            sigma_y = args[1]
            return GaussianBlur(image,name,kernel_size,sigma_x,sigma_y)
        elif filter_name.lower() == "median":
            return MedianBlur(image,name,kernel_size)
        elif filter_name.lower() == "bilateral":
            diameter = args[0]
            sigma_color = args[1]
            sigma_space = args[2]
            return BilateralFilter(image,name,kernel_size,diameter,sigma_color,sigma_space)
        else:
            raise Exception("Please specify a correct filter!\n"
                            "Check if the name of the chosen filter is correct.")

