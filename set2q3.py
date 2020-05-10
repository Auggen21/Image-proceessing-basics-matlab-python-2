import imageio
import cv2
from matplotlib import pyplot as plt 
import numpy as np
img = imageio.imread('cameraman.tif') 
plt.subplot(2,2,1);
plt.imshow(img,'gray');
plt.title('Orginal Image'); 
plt.xticks([]), plt.yticks([]) 
imgavg = cv2.blur(img,(5,5)) 
plt.subplot(222);plt.imshow(imgavg,'gray');plt.title('Averaging filter'); 
plt.xticks([]), plt.yticks([]) 
imggau = cv2.GaussianBlur(img,(5,5),0) 
plt.subplot(223);plt.imshow(imggau,'gray');plt.title('Guassian filter'); 
plt.xticks([]), plt.yticks([])  
lapl = cv2.Laplacian(img,cv2.CV_64F) 
lapout=img+lapl
lapout=np.clip(lapout,0,255)
plt.subplot(224);plt.imshow(lapout,'gray');plt.title('Laplacian filter');
plt.xticks([]), plt.yticks([])
plt.show()