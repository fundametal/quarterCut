import cv2
import cv2 as cv
import numpy as np

# globe valuables
cut_x, cut_y = -1, -1

# image input
src = cv.imread("./images/image.jpg", cv2.IMREAD_GRAYSCALE)
show_image = cv.cvtColor(src, cv2.COLOR_GRAY2BGR)

# window setting
root_wind = 'Quarter Cut'
cv.namedWindow(root_wind)


def save_image():
    global src, cut_x, cut_y
    height, width = src.shape[0], src.shape[1]

    if cut_x != -1 and cut_y != -1:
        cropped_img = src[0: cut_y, 0: cut_x]
        cv2.imwrite('./images/first_quarter.jpg', cropped_img)
        cropped_img = src[0: cut_y, cut_x: width]
        cv2.imwrite('./images/second_quarter.jpg', cropped_img)
        cropped_img = src[cut_y: height, 0: cut_x]
        cv2.imwrite('./images/third_quarter.jpg', cropped_img)
        cropped_img = src[cut_y: height, cut_x: width]
        cv2.imwrite('./images/fourth_quarter.jpg', cropped_img)


def invert_image():
    global src
    src = cv.bitwise_not(src)


# draw interface
def draw(mouse_x, mouse_y):
    global src, show_image, cut_x, cut_y

    show_image = cv.copyMakeBorder(src, 25, 0, 0, 0, cv2.BORDER_CONSTANT, 0)
    show_image = cv.cvtColor(show_image, cv2.COLOR_GRAY2BGR)

    # draw save button
    cv.rectangle(show_image, (src.shape[1]-47, 3), (src.shape[1]-3, 22), (235, 206, 135), -1)
    cv.putText(show_image, 'Save', (src.shape[1]-45, 20), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
    # draw invert button
    cv.rectangle(show_image, (src.shape[1] - 102, 3), (src.shape[1] - 50, 22), (235, 206, 135), -1)
    cv.putText(show_image, 'Invert', (src.shape[1] - 100, 20), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))

    if mouse_y > 25:
        for y in range(25, show_image.shape[0]):
            show_image[y, mouse_x] = [0, 0, 255]

        for x in range(0, show_image.shape[1]):
            show_image[mouse_y, x] = [0, 0, 255]

    if cut_x != -1 and cut_y != -1:
        for y in range(25, show_image.shape[0]):
            show_image[y, cut_x] = [0, 255, 0]

        for x in range(0, show_image.shape[1]):
            show_image[cut_y, x] = [0, 255, 0]


# call back
def mouse_input(event, mouse_x, mouse_y, flags, param):
    global cut_x, cut_y, show_image

    if event is cv.EVENT_LBUTTONDOWN and 3 <= mouse_y <= 22:
        # save button pressed
        if src.shape[1] - 47 <= mouse_x <= src.shape[1] - 3:
            save_image()
        #
        elif src.shape[1] - 102 <= mouse_x <= src.shape[1] - 50:
            invert_image()

    if event is cv.EVENT_LBUTTONDBLCLK and mouse_y > 25:
        cut_x, cut_y = mouse_x, mouse_y

    draw(mouse_x, mouse_y)


# set callback
cv.setMouseCallback(root_wind, mouse_input)

# create window
draw(-1, -1)
while True:
    cv.imshow(root_wind, show_image)

    code = cv.waitKey(1)
    # press q for exit
    if code == ord('q'):
        break

cv.destroyAllWindows()
