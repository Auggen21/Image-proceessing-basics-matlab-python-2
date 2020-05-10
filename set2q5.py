import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

def salt_pepper_noise(im,noiseprob,saltprob):
    out = np.array(im, dtype=float)
    r,c=im.shape
    pcnt=np.uint8(0)
    scnt=np.uint8(0)    
    saltnoise=noiseprob*saltprob #prob of salt noise
    pepnoise=noiseprob*(1-saltprob) #prob of pepper noise
    saltamount=np.uint16(r*c*saltnoise)
    pepamount=np.uint16(r*c*pepnoise)
    while saltamount > scnt:
        m=np.random.randint(0,r)
        n=np.random.randint(0,c)
        out[m][n] =255
        scnt=scnt+1
            
    while pepamount > pcnt:
        m=np.random.randint(0,r-1)
        n=np.random.randint(0,c-1)
        out[m][n] =0
        pcnt=pcnt+1
    return out

def medianfilter(image,ws):
    f=np.double(image)
    r,c=np.shape(f)
    pd=int((ws-1)/2)
    s=np.pad(image,[(pd,pd)],mode='edge')
    start=ws-pd-1
    m,n=np.shape(s)
    W=np.zeros(sze*sze)
    M=np.zeros((r,c),dtype='double')
    for i in range(start,m-pd):
            for j in range(start,n-pd):
                window=s[i-pd:i+pd+1,j-pd:j+pd+1];
                W=np.sort(np.ravel(window))
                m=np.median(W)
                M[i-start,j-start]=m
    return (M)
   
im = img.imread('cameraman.tif')
noiseprob=0.1
saltnoise=0.5
noise_img = salt_pepper_noise(im,noiseprob,saltnoise)
sze=int(input('Enter the Windows size of Median Filter:'))
blurimg = medianfilter(noise_img,sze)

plt.subplot(131)
plt.imshow(im,'gray')
plt.title('Orginal Image')
plt.xticks([]), plt.yticks([])

plt.subplot(132)
plt.imshow(noise_img,'gray')
plt.title('Noise Image')
plt.xticks([]), plt.yticks([])

plt.subplot(133)
plt.imshow(blurimg,'gray')
plt.title('Median filtered Image')
plt.xticks([]), plt.yticks([])
plt.show()
