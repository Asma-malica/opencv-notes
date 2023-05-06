import cv2
import numpy as np
from matplotlib import pyplot as plt
# kernal - remove the noise from the images
img = cv2.imread('morpological.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5,5), np.uint8) # (5,5) - kernal size and data type


dilation = cv2.dilate(mask, kernal, iterations=10) 
erosion = cv2.erode(mask, kernal, iterations=2)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal) # morphopen -->  erosion followed by dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal) # morphclose --> dilation followed by erosion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal) #MORPH_GRADIENT --> differentiation b/w dilation and erosion
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal) # MORPH_TOPHAT --> differentiation b/w opening and closing

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()