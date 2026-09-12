import cv2
img=cv2.imread("input.jpg")
r3=cv2.blur(img,(2,2)); r7=cv2.blur(img,(15,15))

cv2.imwrite("output.png",r7)
print("Tested 2x2 and 15x15; final output uses 15x15.")

cv2.imshow("Original",img)
cv2.imshow("Mean Filter 2x2",r3)
cv2.imshow("Mean Filter 15x15",r7)

cv2.waitKey(0)
cv2.destroyAllWindows()