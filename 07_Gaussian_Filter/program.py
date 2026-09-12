import cv2

img=cv2.imread("input.jpg")
result=cv2.GaussianBlur(img,(15,15),0)

cv2.imwrite("output.png",result)
cv2.imshow("Original",img)
cv2.imshow("Gaussian Filter",result)

cv2.waitKey(0)
cv2.destroyAllWindows()