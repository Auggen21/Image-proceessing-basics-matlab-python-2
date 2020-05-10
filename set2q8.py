import numpy as np 
import imageio
from matplotlib import pyplot as plt 
import cv2
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
img = cv2.imread('lena_RGB.tif') 
m,n,o=img.shape
out=np.zeros([m,n,o]) 
R=img[:,:,0]
G=img[:,:,1]
B=img[:,:,2]
ws=3
pd=int((ws-1)/2)
kernel = -1*np.ones((ws,ws))
kernel[pd,pd]=-1*np.sum(np.ravel(kernel))
R1=convol(R,kernel)
G1=convol(G,kernel)
B1=convol(B,kernel)
R1=np.clip(R1,0,255)
G1=np.clip(G1,0,255)
B1=np.clip(B1,0,255)
out[:,:,0]=R1
out[:,:,1]=G1
out[:,:,2]=B1
cv2.imshow('Original Image',img)
cv2.imshow('Sharpened Image',out)
cv2.waitKey(0)
