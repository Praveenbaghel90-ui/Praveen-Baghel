import cv2
import matplotlib.pyplot as plt

img=cv2.imread("input.jpg",0)
hist=cv2.calcHist([img],[0],None,[256],[0,256])

print("Intensity with highest frequency:",int(hist.argmax()))

plt.plot(hist);
plt.xlim(0,256);
plt.xlabel("Intensity");
plt.ylabel("Frequency");
plt.title("Intensity Histogram")

plt.savefig("output.png",bbox_inches="tight");
plt.close()

cv2.imshow("Original",img)

cv2.waitKey(0)
cv2.destroyAllWindows()