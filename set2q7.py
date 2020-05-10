import numpy as np 
import imageio
from matplotlib import pyplot as plt 

def convol(im,kernel):
    ws,ws1=kernel.shape;
    pd=int((ws-1)/2);
    start=ws-pd-1;
    row,col=im.shape
    f=np.pad(im,[(pd,pd)],'reflect')
    r,c=f.shape;
    out=np.zeros([row,col])
    for i in range(start,r-pd):
        for j in range(start,c-pd):
           window=f[(i-pd):(i+pd+1),(j-pd):(j+pd+1)];
           m=np.multiply(kernel,window)
           su=np.sum(np.ravel(m))
           out[i-start,j-start]=su;
    return(out)
    
img = imageio.imread('lena_RGB.tif')
m,n,o=img.shape
out=np.zeros([m,n,o]) 
R=img[:,:,0]
G=img[:,:,1]
B=img[:,:,2]
ws=7
kernel = np.ones((ws,ws))/(ws*ws)
R1=convol(R,kernel)
G1=convol(G,kernel)
B1=convol(B,kernel)
out[:,:,0]=R1
out[:,:,1]=G1
out[:,:,2]=B1
plt.imshow(np.uint8(out))
plt.subplot(121);plt.imshow(img);plt.title('Orginal Image'); 
plt.xticks([]), plt.yticks([]) 
plt.subplot(122);plt.imshow(np.uint8(out));plt.title('Smoothened Image'); 
plt.xticks([]), plt.yticks([]) 
plt.show()