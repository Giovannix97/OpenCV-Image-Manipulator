from FilterFactory import *
import argparse

FOLDER_PATH = 'Images/'


def parse_arguments():
    my_parser = argparse.ArgumentParser(
        description="Use the Open-CV library to apply some filters and operations on a image."
                    "Place your input image inside the directory \'Image.\'\n\n"
                    "",
        epilog="Thanks for using this software :)")

    my_parser.add_argument("input_image", help="Input image chosen by the user")
    my_parser.add_argument("filter_name",
                           help="Name of the desired filter. For example average,median,gaussian or bilateral")
    my_parser.add_argument("kernel_size", help="Size of the kernel. Choose a value like 3,5,7,9...",
                           type=int)
    my_parser.add_argument("-sx", "--sigma_x", help="Gaussian kernel standard deviation in X direction.",
                           type=float)
    my_parser.add_argument("-sy", "--sigma_y", help="Gaussian kernel standard deviation in Y direction",
                           type=float)
    my_parser.add_argument("-d", "--diameter", help="Diameter of each pixel neighborhood that is used during filtering",
                           type=int)
    my_parser.add_argument("-sc", "--sigma_color",
                           help="Filter sigma in the color space. A larger value of the parameter "
                                "means that farther colors within the pixel neighborhood (see sigmaSpace) "
                                "will be mixed together, resulting in larger areas of semi-equal color",
                           type=float)
    my_parser.add_argument("-ss", "--sigma_space",
                           help="Filter sigma in the coordinate space. A larger value of the parameter means"
                                " that farther pixels will influence each other as long as their colors are "
                                "close enough.",
                           type=float)

    return my_parser.parse_args()

def show_numpy_image(image):
    cv.imshow("Your Image!", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def main():

    args = parse_arguments()

    input_image = OpenCV_Image(FOLDER_PATH + args.input_image, 1)
    chosen_filter = args.filter_name.lower()


    if chosen_filter == "gaussian":
        filter = FilterFactory.get_filter(input_image.get_opencv_image(), chosen_filter, args.kernel_size, args.sigma_x, args.sigma_y)  #Cambia immagine
    elif chosen_filter == "bilateral":
        filter = FilterFactory.get_filter(input_image.get_opencv_image(), chosen_filter, args.kernel_size, args.diameter, args.sigma_color, args.sigma_space)
    else:
        filter = FilterFactory.get_filter(input_image.get_opencv_image(), chosen_filter, args.kernel_size)

    output_image = filter.apply()
    show_numpy_image(output_image)



if __name__ == '__main__':
    main()

