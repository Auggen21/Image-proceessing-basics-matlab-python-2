import matplotlib.pyplot as plt
import imageio
from scipy import ndimage
from skimage import feature
import numpy as np
im = imageio.imread('wirebond_mask.tif')

asd=np.array([2,2])
plt.figure(1)
plt.imshow(im,cmap='gray'),plt.title ('Original Image')
#Horizontal Line

sob=([-1,-2,-1],[0,0,0],[1,2,1])
pre=([-1,-1,-1],[0,0,0],[1,1,1])
rob=([-1,0],[0,1])
loag=([0,0,-1,0,0],[0,-1,2,-1,0],[-1,2,16,-2,-1],[0,-1,-2,-1,0],[0,0,-1,0,0])
can=feature.canny(im,sigma=3)

out1=ndimage.filters.convolve(im,sob)
out2=ndimage.filters.convolve(im,pre)
out3=ndimage.filters.convolve(im,rob)
out4=ndimage.filters.convolve(im,loag)
out5=ndimage.filters.convolve(im,can)

plt.figure(2)
plt.imshow((out1),cmap='gray'),plt.title ('Sobel Edge Detection')

plt.figure(3)
plt.imshow((out2),cmap='gray'),plt.title ('Prewitt Edge Detection')

plt.figure(4)
plt.imshow((out3),cmap='gray'),plt.title ('Roberts Edge Detection')

plt.figure(5)
plt.imshow((out4),cmap='gray'),plt.title ('Laplacian of Gaussian Edge Detection')


plt.figure(5)
plt.imshow((out4),cmap='gray'),plt.title ('Canny Edge Detection')