import cv2

img=cv2.imread("input.jpg")
result=cv2.medianBlur(img,15)

cv2.imwrite("output.png",result)
cv2.imshow("Original",img)
cv2.imshow("Median Filter",result)

cv2.waitKey(0)
cv2.destroyAllWindows()