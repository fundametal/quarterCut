import cv2
import cv2 as cv
import numpy as np

# globe valuables
ix, iy = -1, -1

# image input
src = cv.imread("./images/image.jpg", cv2.IMREAD_GRAYSCALE)
# src = np.zeros((512, 512, 1), np.uint8)
# cv.rectangle(src, (50, 50), (306, 306), 128)
show_image = cv.cvtColor(src, cv2.COLOR_GRAY2BGR)

# window setting
root_wind = 'Quarter Cut'
cv.namedWindow(root_wind)


# call backs
def save_image(*args):
    height, width = src.shape[0], src.shape[1]
    cropped_img = src[0: iy, 0: ix]
    cv2.imwrite('./images/first_quarter.jpg', cropped_img)
    cropped_img = src[0: iy, ix: width]
    cv2.imwrite('./images/second_quarter.jpg', cropped_img)
    cropped_img = src[iy: height, 0: ix]
    cv2.imwrite('./images/third_quarter.jpg', cropped_img)
    cropped_img = src[iy: height, ix: width]
    cv2.imwrite('./images/fourth_quarter.jpg', cropped_img)


def invert_image(*args):
    global src
    src = cv.bitwise_not(src)


def mouse_input(event, mouse_x, mouse_y, flags, param):
    global ix, iy, show_image

    show_image = cv.cvtColor(src, cv2.COLOR_GRAY2BGR)

    if event is cv.EVENT_LBUTTONDBLCLK:
        ix, iy = mouse_x, mouse_y

    for y in range(0, show_image.shape[0]):
        show_image[y, mouse_x] = [0,0,255]
        # show_image.itemset(y, mouse_x, 0, 0)
        # show_image.itemset(y, mouse_x, 1, 0)
        # show_image.itemset(y, mouse_x, 2, 255)

    for x in range(0, show_image.shape[1]):
        show_image[mouse_y, x] = [0, 0, 255]
        # show_image.itemset(mouse_y, x, 0, 0)
        # show_image.itemset(mouse_y, x, 1, 0)
        # show_image.itemset(mouse_y, x, 2, 255)

    if ix != -1 and iy != -1:
        for y in range(0, show_image.shape[0]):
            show_image[y, ix] = [0, 255, 0]
            # show_image.itemset(y, ix, 0, 0)
            # show_image.itemset(y, ix, 1, 255)
            # show_image.itemset(y, ix, 2, 0)

        for x in range(0, show_image.shape[1]):
            show_image[iy, x] = [0, 255, 0]
            # show_image.itemset(iy, x, 0, 0)
            # show_image.itemset(iy, x, 1, 255)
            # show_image.itemset(iy, x, 2, 0)


# button
cv.createButton('invert image', invert_image)
cv.createButton('save image', save_image)
cv.setMouseCallback(root_wind, mouse_input)

# create window
while True:
    cv.imshow(root_wind, show_image)

    code = cv.waitKey(1)

    if code == ord('q'):
        break

cv.destroyAllWindows()
