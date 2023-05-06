
#edge deduction methods 
# 1 . laplacian
# 2 . sobel X sobel Y sobelcombined

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("messi5.jpg", cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=5) # laplacian means --> edge deduction --if ksize is increased the img is blurred
lap = np.uint8(np.absolute(lap))


titles = ['image', 'Laplacian']
images = [img, lap]
for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()