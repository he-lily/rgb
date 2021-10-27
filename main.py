from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


def get_rgb(image_name, resize=None):
    """
	 param image_name   name of image to be processesed
	 param resize       optional: resize image to tuple (width, height)
	 return             3 tuple list of ([r], [g], [b])
	 """
    image_name = image_name
    path_to_image = "images/"+image_name
    red = [0]*256
    green = [0]*256
    blue = [0]*256
    with Image.open(path_to_image) as image:
        image = image.resize((resize[0], resize[1]))
        for x in range(0, image.width):
            for y in range(0, image.height):
                rgb = image.getpixel((x,y))
                red[rgb[0]] += 1
                green[rgb[1]] += 1
                blue[rgb[2]] += 1
    return (red, green, blue)

def plot_histograms(rgb_tuple):
    """takes in 3 tuple of rgb lists. plots histograms"""
    fig, axs = plt.subplots(3)
    axs[0].hist(rgb_tuple[0], bins=256, range=[0, 256], color = "red")
    axs[1].hist(rgb_tuple[1], bins=256, range=[0, 256], color = "green")
    axs[2].hist(rgb_tuple[2], bins=256, range=[0, 256], color = "blue")

    fig.tight_layout()
    plt.show()

def make_histogram_list(rgb):
    """
    :param rgb: 3 tuple list of len 256
    :return: 3 tuple list of occurrences
    """
    new_rgb = ([], [], [])
    for i in range(0, 3):
        for j in range(0, 256):
            if(rgb[i][j]!=0):
                new_rgb[i].extend( [j]*rgb[i][j] )
    return (new_rgb)

if __name__ == "__main__":
    rgb = get_rgb("rgb.jpg", (5, 5))
    print(rgb[2])
    new_rgb = make_histogram_list(rgb)
    print(new_rgb[2])
    print(len(new_rgb[2]))
    plot_histograms(new_rgb)

# red_average = np.mean(red)
# green_average = np.mean(green)
# blue_average = np.mean(blue)
# print(red_average)
# print(green_average)
# print(blue_average)
#

