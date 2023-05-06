# resize
import cv2 
image =cv2.imread("screenshot.png")
resized_image=cv2.resize(image,None,fx=5,fy=5) #fx = width fy = height if we change the value of 
# fx and fy it will change the size of the image 
# whole num means it increases the size of the image
# floating num reduces the size of the image
cv2.imshow("Original image",image)
cv2.imshow("Resized image",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
