import cv2
import numpy as np

img=cv2.imread("input.jpg",0);
r,c=img.shape; cy,cx=r//2,c//2

dft=cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT);
s=np.fft.fftshift(dft)

y,x=np.ogrid[:r,:c];
m=(((x-cx)**2+(y-cy)**2)<=30**2).astype(np.float32);
m=np.dstack((m,m))

out=cv2.idft(np.fft.ifftshift(s*m),flags=cv2.DFT_SCALE|cv2.DFT_REAL_OUTPUT)
out=cv2.normalize(out,None,0,255,cv2.NORM_MINMAX).astype(np.uint8)

cv2.imwrite("output.png",out)
cv2.imshow("Original",img)
cv2.imshow("Low-Pass Filtered",out)

cv2.waitKey(0)
cv2.destroyAllWindows()
