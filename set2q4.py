import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
     
def convol(im,kernel):
    ws,ws1=kernel.shape;
    pd=int((ws-1)/2);
    start=ws-pd-1;
    row,col=im.shape
    f=np.pad(im,[(pd,pd)],'constant')
    r,c=f.shape;
    out=np.zeros([row,col])
    for i in range(start,r-pd):
        for j in range(start,c-pd):
            window=f[(i-pd):(i+pd+1),(j-pd):(j+pd+1)];
            m=np.multiply(kernel,window)
            su=np.sum(np.ravel(m))
            out[i-start,j-start]=su;
    out1=out/(ws*ws);
    return(out1)
    
def convandcorr(fil,image):
    filtr=[item.split() for item in fil.split('\n')] 
    h_corr=np.int8(filtr);
    r,c=image.shape
    m,n = h_corr.shape
    h_corr=h_corr/(m*n)
    h_conv=np.zeros([m,n])
    f_corr=np.zeros([r,c])
    f_conv=np.zeros([r,c])
    #%Rotating the matrix by 180 degree 
    #%for getting convolution matrix.
    for i in range(m):
        for j in range(n):
            h_conv[i,j] = h_corr[m-i-1,n-j-1]
        

    f_corr = convol(f,h_corr);
    f_conv = convol(f,h_conv);   
    return(f_corr,f_conv)
    
image = img.imread('cameraman.tif')
f=np.double(image)
fil3 = open('filter3.txt').read()
conv3,corr3=convandcorr(fil3,f)
fil7 = open('filter7.txt').read()
conv7,corr7=convandcorr(fil7,f)
fil11 = open('filter11.txt').read()
conv11,corr11=convandcorr(fil11,f)
           
plt.subplot(321)
plt.imshow(conv3)
plt.title('Convolution 3X3')
plt.axis('off')
plt.set_cmap('gray')

plt.subplot(322)
plt.imshow(corr3)
plt.title('Correlation 3X3')
plt.axis('off')
plt.set_cmap('gray')

plt.subplot(323)
plt.imshow(conv7)
plt.title('Convolution 7X7')
plt.axis('off')
plt.set_cmap('gray')

plt.subplot(324)
plt.imshow(corr7)
plt.title('Correlation 7X7')
plt.axis('off')
plt.set_cmap('gray')

plt.subplot(325)
plt.imshow(conv11)
plt.title('Convolution 11X11')
plt.axis('off')
plt.set_cmap('gray')

plt.subplot(326)
plt.imshow(corr11)
plt.title('Correlation 11X11')
plt.axis('off')
plt.set_cmap('gray')
plt.show()