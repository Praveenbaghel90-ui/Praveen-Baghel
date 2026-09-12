import cv2
img=cv2.imread("input.jpg")

cv2.imwrite("output_mean.png",cv2.blur(img,(7,7)))
cv2.imwrite("output_gaussian.png",cv2.GaussianBlur(img,(7,7),0))
cv2.imwrite("output_median.png",cv2.medianBlur(img,7))

cv2.imshow("Original",img)
cv2.imshow("Mean Filter",cv2.blur(img,(7,7)))
cv2.imshow("Gaussian Filter",cv2.GaussianBlur(img,(7,7),0))
cv2.imshow("Median Filter",cv2.medianBlur(img,7))

cv2.waitKey(0)
cv2.destroyAllWindows()