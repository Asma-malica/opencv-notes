import cv2
import numpy as np
img = cv2.imread('Screenshot (186).png',0)
print(img)
cv2.imshow('Screenshot (186).png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()