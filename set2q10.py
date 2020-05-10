import numpy as np
import matplotlib.pyplot as plt
import imageio

im=imageio.imread('cameraman.tif'); 
M,N=im.shape;  
p=2*M; 
q=2*N; 
pd1=np.int(M/2)
pd2=np.int(N/2)
img=np.pad(im,[pd1,pd2],'constant')
#FT of image centered 
F=np.fft.fftshift(np.fft.fft2(img)); 
#centre of the frequency rectangle 
cX=p/2; 
cY=q/2; 
#distance Metrix 
D=np.zeros((p,q)); 
for i in range(p):
    for j in range(q):
        D[i,j]=np.sqrt((i-cX)**2+(j-cY)**2)

#ideal Low Pass Filter 
D0=50; 
hid=(D<=D0); 
Ideal_Img=np.multiply(hid,F); 
Ideal_Img=np.fft.fftshift(Ideal_Img); 
Ideal_Img=np.real(np.fft.ifft2(Ideal_Img)); 
Ideal_Img=Ideal_Img[int(M/2):int(3*M/2),int(N/2):int(3*N/2)]; 
plt.subplot(2,2,1); 
plt.imshow(im,cmap='gray'),plt.title('Original Image'); 
plt.axis('off')
plt.subplot(2,2,2); plt.imshow(Ideal_Img,cmap='gray'),plt.title('Ideal LPF output'); 
plt.axis('off')

#Butterworth Filter 
n=5; #order
h_bu=np.zeros((p,q)); 
for i in range(p):
    for j in range(q):
        h_bu[i,j]=1/(1+(D[i,j]/D0)**(2*n))
btrWorth=np.multiply(h_bu,F); 
btrWorth=np.fft.fftshift(btrWorth); 
btrWorth=np.real(np.fft.ifft2(btrWorth)); 
btrWorth=btrWorth[int(M/2):int(3*M/2),int(N/2):int(3*N/2)]
#btrWorth=btrWorth[1:M,1:N]; 
plt.subplot(2,2,3); plt.imshow(btrWorth,cmap='gray'); plt.title('Butterworth LPF Output');
plt.axis('off')

#Guassian Low Pass Filter
G=np.zeros((p,q));
for i in range(p):
    for j in range(q):
        G[i,j]=np.exp(-D[i,j]**2/(2*D0**2));
gsflt=np.multiply(G,F);
gsflt=np.fft.fftshift(gsflt);
gsflt=np.real(np.fft.ifft2(gsflt));
gsflt=gsflt[int(M/2):int(3*M/2),int(N/2):int(3*N/2)];
plt.subplot(2,2,4);
plt.imshow(gsflt,cmap='gray');
plt.title('Gaussian LPF Output');
plt.axis('off')
plt.show()