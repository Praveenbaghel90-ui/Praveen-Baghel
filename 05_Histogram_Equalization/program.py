import cv2
import matplotlib.pyplot as plt

img=cv2.imread("input.jpg",0);
eq=cv2.equalizeHist(img)
cv2.imwrite("output.png",eq)

h1=cv2.calcHist([img],[0],None,[256],[0,256]);
h2=cv2.calcHist([eq],[0],None,[256],[0,256])

plt.figure(figsize=(8,4)); 
plt.subplot(1,2,1);
plt.plot(h1);
plt.title("Before"); 
plt.xlim(0,256)

plt.subplot(1,2,2); 
plt.plot(h2);
plt.title("After"); 
plt.xlim(0,256);
plt.tight_layout()

plt.savefig("histogram_comparison.png",bbox_inches="tight");
plt.close()

cv2.imshow("Original",img) 
cv2.imshow("Equalized",eq)

cv2.waitKey(0)
cv2.destroyAllWindows()