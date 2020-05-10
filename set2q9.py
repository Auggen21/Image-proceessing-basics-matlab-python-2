import numpy as np
import matplotlib.pyplot as plt
import imageio

def gauss(r,c):
    x, y = np.meshgrid(np.linspace(-1,1,r), np.linspace(-1,1,c))
    d = np.sqrt(x*x+y*y)
    sigma, mu = .02, 0.0
    g = np.exp(-( (d-mu)**2 / ( 2.0 * sigma**2 ) ) )
    return g

im=imageio.imread('cameraman.tif')
n,m=im.shape
me=0
sd=8

#without padding
df=np.fft.fftshift(np.fft.fft2(im))
h=np.float16(gauss(n,m))
hf=np.fft.fftshift(np.fft.fft2(h))
F=np.multiply(hf,df)
f=np.fft.ifft2(F)
f=np.abs(np.fft.fftshift(np.real(f)))
plt.figure,plt.imshow(im,cmap='gray'),plt.title('Original Image');
plt.figure(2),plt.imshow(f,cmap='gray'),plt.title('DFT Filtering - Without Padding');

#with padding -to avoid wraparround error due to periodicity of FT
p1=n*2 # for mxn matrix pad size P>=2m-1 and Q<=2n-1
p2=m*2;
pd1=np.int(n/2) 
pd2=np.int(m/2)
img1=np.pad(im,[(pd1,pd2)],'constant')
fp=np.fft.fftshift(np.fft.fft2(img1));
hp=np.float16(gauss(p1,p2))
hp=np.fft.fftshift(np.fft.fft2(hp));
rp=np.multiply(hp,fp);
ap=np.fft.ifft2(rp);
ap=np.abs(np.fft.fftshift(np.real(ap)))
Gwopd=ap[int(n/2):int(3*n/2),int(m/2):int(3*m/2)]; 
plt.figure(3),plt.imshow(Gwopd,cmap='gray'),plt.title('DFT Filtering - With Padding');
plt.show()