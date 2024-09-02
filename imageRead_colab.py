# 코랩에서 cv2 동작시키기

import cv2
import sys
from google.colab.patches import cv2_imshow

fileName = 'cat.jpg'

img = cv2.imread(fileName)
if img is None:
    sys.exit("Could not read the image.")

# cv2.namedWindow("Display window", cv2.WINDOW_AUTOSIZE)
cv2_imshow(img)
cv2.waitKey(0)
cv2.destroyAllWindows()
