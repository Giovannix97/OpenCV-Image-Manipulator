from FilterFactory import *
import argparse
from argparse import RawTextHelpFormatter

FOLDER_PATH = 'Images/'


def parse_arguments():
    """This function uses the argparse library to manage the command line options passed by the user.
       Try to use "-h" flag to see the avaible options.

    """
    my_parser = argparse.ArgumentParser(
        description="Use the Open-CV library to apply some filters and operations on a image."
                    "Place your input image inside the directory \'Image.\'"
                    "\n"
                    "\n"
                    "How to use:        python main.py [input_image] [filter_name] [kernel_size] [optional_arguments...]"
                    "\n"
                    "\n"
                    "Example of usage:  python main.py lena.jpg average 5\n"
                    "                   python main.py lena.jpg median 3\n"
                    "                   python main.py lena.jpg gaussian 5 -sx 10 -sy 5\n"
                    "                   python main.py lena.jpg bilateral 3 -d 9 -sc 75 -ss 75 ",
        formatter_class=RawTextHelpFormatter,
        epilog="Thanks for using this software :)")

    my_parser.add_argument("input_image", help="Input image chosen by the user")
    my_parser.add_argument("filter_name",
                           help="Name of the desired filter. For example average,median,gaussian or bilateral")
    my_parser.add_argument("kernel_size", help="Size of the kernel. Choose a value like 3,5,7,9...",
                           type=int)
    my_parser.add_argument("-sx", "--sigma_x", help="Gaussian kernel standard deviation in X direction.\n"
                                                    "\n"
                                                    "(Used only in Gaussian filter)",
                           type=float)
    my_parser.add_argument("-sy", "--sigma_y", help="Gaussian kernel standard deviation in Y direction.\n"
                                                    "\n"
                                                    "(Used only in Gaussian filter)",
                           type=float)
    my_parser.add_argument("-d", "--diameter", help="Diameter of each pixel neighborhood that is used during filtering.\n"
                                "\n"
                                "(Used only in the Bilateral filter)",
                           type=int)
    my_parser.add_argument("-sc", "--sigma_color",
                           help="Filter sigma in the color space. A larger value of the parameter\n"
                                "means that farther colors within the pixel neighborhood (see sigmaSpace)\n"
                                "will be mixed together, resulting in larger areas of semi-equal color\n"
                                "\n"
                                "(Used only in the Bilateral filter)",
                           type=float)
    my_parser.add_argument("-ss", "--sigma_space",
                           help="Filter sigma in the coordinate space. A larger value of the parameter means\n"
                                " that farther pixels will influence each other as long as their colors are\n"
                                "close enough.\n"
                                "\n"
                                "(Used only in the Bilateral filter)",
                           type=float)

    return my_parser.parse_args()


def show_numpy_image(image):
    """Show the selected image in a new window."""
    cv.imshow("Your Image!", image)
    cv.waitKey(0)
    cv.destroyAllWindows()


def main():

    # Validate the arguments passed by the user.
    args = parse_arguments()

    # Open the image and get the filter chosen by the user.
    input_image = OpenCV_Image(FOLDER_PATH + args.input_image, 1)
    chosen_filter = args.filter_name.lower()

    if chosen_filter == "gaussian":
        filter_f  = FilterFactory.get_filter(input_image.get_opencv_image(), chosen_filter, args.kernel_size,
                                             args.sigma_x, args.sigma_y)
    elif chosen_filter == "bilateral":
        filter_f = FilterFactory.get_filter(input_image.get_opencv_image(), chosen_filter, args.kernel_size,
                                            args.diameter, args.sigma_color, args.sigma_space)
    else:
        filter_f = FilterFactory.get_filter(input_image.get_opencv_image(), chosen_filter, args.kernel_size)

    # Apply the filter and show the result
    output_image = filter_f.apply()
    show_numpy_image(output_image)


if __name__ == '__main__':
    main()

