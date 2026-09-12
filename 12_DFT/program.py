import cv2
import numpy as np

img=cv2.imread("input.jpg",0)
dft=cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)
shifted=np.fft.fftshift(dft)

print("Original image shape:",img.shape)
print("DFT result shape:",dft.shape)
print("Shifted DFT shape:",shifted.shape)

mag=cv2.magnitude(shifted[:,:,0],shifted[:,:,1])
mag=cv2.normalize(np.log1p(mag),None,0,255,cv2.NORM_MINMAX).astype(np.uint8)

cv2.imwrite("output.png",mag)
cv2.imshow("Original",img)
cv2.imshow("Magnitude Spectrum",mag)  
  
cv2.waitKey(0)
cv2.destroyAllWindows()