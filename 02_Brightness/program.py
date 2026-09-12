import cv2
import numpy as np

img=cv2.imread("input.jpg")
brightness=50
result=np.clip(img.astype(np.int16)+brightness,0,255).astype(np.uint8)

print("Pixel before:",img[50,50])
print("Pixel after:",result[50,50])

cv2.imshow("Original",img)
cv2.imshow("Brightness",result)
cv2.imwrite("output.png",result)

cv2.waitKey(0)
cv2.destroyAllWindows()