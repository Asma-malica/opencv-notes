#threshold segmentation technique
# seperating the 

import cv2 as cv
import numpy as np

img = cv.imread('gradient.png',0)
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)  # pixel value 0 - black ; >50 means - white
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC) # <127 - actual image la irkura intensity will be the same output 
# if the pixel value exceeds >127 means 127 la irkura pixel value extends to 255  

_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO) # <127 - zero;  >127 - original image will be the output 
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV) # <127 - original image will be the output ; >127 - zero



cv.imshow("Image", img)
cv.imshow("th1", th1)
cv.imshow("th2", th2)
cv.imshow("th3", th3)
cv.imshow("th4", th4)
cv.imshow("th5", th5)

cv.waitKey(0)
cv.destroyAllWindows()