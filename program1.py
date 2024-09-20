#### Image Resizing
# Explain the various situtions where image resizing is needed

import cv2

img = cv2.imread("jerry.png", 1)
cv2.imshow("Original Image", img)

# The order of dimensions is (WIDTH, HEIGHT)
resized = cv2.resize(img, (500, 250))
cv2.imshow("reducedImage", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
