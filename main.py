import cv2 as cv
import numpy as np


# globe valuables
cut_x, cut_y = -1, -1
fliped = False

# image input
src = cv.imread("./images/image.jpg", cv.IMREAD_GRAYSCALE)
saved_image = cv.imread("./images/image.jpg", cv.IMREAD_GRAYSCALE)
show_image = cv.cvtColor(saved_image, cv.COLOR_GRAY2BGR)

# window setting
root_wind = 'Quarter Cut'
cv.namedWindow(root_wind)


def save_image(*args):
    global src, cut_x, cut_y
    height, width = src.shape[0], src.shape[1]

    if cut_x != -1 and cut_y != -1:
        cropped_img = saved_image[0: cut_y, 0: cut_x]
        cv.imwrite('./images/first_quarter.jpg', cropped_img)
        cropped_img = saved_image[0: cut_y, cut_x: width]
        cv.imwrite('./images/second_quarter.jpg', cropped_img)
        cropped_img = saved_image[cut_y + 1: height, 0: cut_x]
        cv.imwrite('./images/third_quarter.jpg', cropped_img)
        cropped_img = saved_image[cut_y + 1: height, cut_x: width]
        cv.imwrite('./images/fourth_quarter.jpg', cropped_img)


def flip_image(*args):
    global fliped, saved_image

    fliped = not fliped

    if fliped:
        upper_img = src[0: cut_y, 0: src.shape[1]]
        upper_img = cv.flip(upper_img, 0)
        saved_image = np.vstack((upper_img, src[cut_y: src.shape[0], 0: src.shape[1]]))
    else:
        saved_image = src

    draw(-1, -1)


def invert_image(*args):
    global fliped, src, saved_image, show_image
    src = cv.bitwise_not(src)
    if fliped:
        fliped = not fliped
        flip_image()
    else:
        saved_image = src
        draw(-1, -1)


# draw interface
def draw(mouse_x, mouse_y):
    global src, show_image, cut_x, cut_y, saved_image

    show_image = cv.cvtColor(saved_image, cv.COLOR_GRAY2BGR)

    for y in range(0, show_image.shape[0]):
        show_image[y, mouse_x] = [0, 0, 255]

    for x in range(0, show_image.shape[1]):
        show_image[mouse_y, x] = [0, 0, 255]

    if cut_x != -1 and cut_y != -1:
        for y in range(0, show_image.shape[0]):
            show_image[y, cut_x] = [0, 255, 0]

        for x in range(0, show_image.shape[1]):
            show_image[cut_y, x] = [0, 255, 0]


# call back
def mouse_input(event, mouse_x, mouse_y, flags, param):
    global cut_x, cut_y, fliped

    if event is cv.EVENT_LBUTTONDBLCLK:
        cut_x, cut_y = mouse_x, mouse_y
        if fliped:
            fliped = not fliped
            flip_image()

    draw(mouse_x, mouse_y)


# set callback
cv.setMouseCallback(root_wind, mouse_input)
cv.createButton('invert image', invert_image)
cv.createButton('flip image', flip_image)
cv.createButton('save image', save_image)

# create window
draw(-1, -1)
while True:
    cv.imshow(root_wind, show_image)

    code = cv.waitKey(1)
    # press q for exit
    if code == ord('q'):
        break

cv.destroyAllWindows()
