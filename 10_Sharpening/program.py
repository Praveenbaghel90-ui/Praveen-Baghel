import cv2 
import numpy as np

img=cv2.imread("input.jpg")
kernel=np.array([
     [0,-1,0],
     [-1,5,-1],
     [0,-1,0]],
     dtype=np.float32)
result=cv2.filter2D(img,-1,kernel)

cv2.imwrite("output.png",result)
cv2.imshow("Original",img) 
cv2.imshow("Sharpened",result)

cv2.waitKey(0)
cv2.destroyAllWindows()