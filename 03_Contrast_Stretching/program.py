import cv2
import numpy as np

img=cv2.imread("input.jpg",0)
mn,mx=int(img.min()),int(img.max())

print("Minimum intensity:",mn,"Maximum intensity:",mx)

result=((img-mn)*255/(mx-mn)).clip(0,255).astype(np.uint8)if mx>mn else img

cv2.imshow("Original",img)
cv2.imshow("Contrast Stretched",result)
cv2.imwrite("output.png",result)

cv2.waitKey(0)
cv2.destroyAllWindows()