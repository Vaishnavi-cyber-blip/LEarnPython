import cv2
import os


def image_processing():
    img = cv2.imread("hacktober.png", cv2.IMREAD_COLOR)

    cv2.line(img, (20, 200), (200, 20), (0, 0, 255), 5)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
