import numpy as np
import imageio
import matplotlib.pyplot as plt

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

def gauss(r,c,sigma,mu):
    x, y = np.meshgrid(np.linspace(-1,1,r), np.linspace(-1,1,c))
    g = np.exp(-((x-mu)**2+(y-mu)**2)/(2*sigma**2)) 
    return g

print('Menu')
print('1.Sobel Filter')
print('2.Prewitt Filter')
print('3.Roberts Filter')
print('4.Laplacian of Gaussian Filter')
print('5.Canny Filter')
print('6.Exit')
ch=input('Enter the choice:')

im = imageio.imread('building.tif')
r,c=im.shape
plt.figure(1),plt.imshow(im,cmap='gray'),plt.title('Original image')
plt.xticks([]), plt.yticks([]) 
img=im/max(np.ravel(im))

if (ch=='1'):

#Sobel filter
    #for gradient in x direction
    thres1=0.20
    ds1 = np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]])
    sobelEdge1 = convol(img,ds1)
    #for gradient in y direction
    ds2 = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
    sobelEdge2 = convol(img,ds2)
    ds=np.abs(sobelEdge1)+np.abs(sobelEdge2)
    T1=thres1*max(np.ravel(ds))
    sob=np.multiply((ds>=T1),ds)
    plt.figure()
    plt.subplot(2,2,1),plt.imshow(np.abs(sobelEdge1),cmap='gray')
    plt.title('Gradient X Direction'),plt.axis('off')
    plt.subplot(2,2,2),plt.imshow(np.abs(sobelEdge2),cmap='gray')
    plt.title('Gradient Y Direction'),plt.axis('off')
    plt.subplot(2,2,3),plt.imshow(ds,cmap='gray')
    plt.title('Gradient X+Y'),plt.axis('off')
    plt.subplot(2,2,4),plt.imshow(sob,cmap='gray')
    plt.title('Thresholded image'),plt.axis('off')

elif (ch=='2'):
       
#Prewitt filter
    thres2=0.20
    #for gradient in x direction
    dx1 = np.array([[-1, -1, -1],[0, 0, 0],[1, 1, 1]])
    prewEdge1 = convol(img,dx1)
    #for gradient in y direction
    dx2 = np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]])
    prewEdge2 = convol(img,dx2)
    dx=np.abs(prewEdge1)+np.abs(prewEdge2)
    T2=thres2*max(np.ravel(dx))
    pre=np.multiply((dx>=T2),dx)
    plt.figure()
    plt.subplot(2,2,1),plt.imshow(np.abs(prewEdge1),cmap='gray'),plt.title('Gradient X Direction')
    plt.axis('off')
    plt.subplot(2,2,2),plt.imshow(np.abs(prewEdge2),cmap='gray'),plt.title('Gradient Y Direction')
    plt.axis('off')
    plt.subplot(2,2,3),plt.imshow(dx,cmap='gray'),plt.title('Gradient X+Y')
    plt.axis('off')
    plt.subplot(2,2,4),plt.imshow(pre,cmap='gray'),plt.title('Thresholded image')
    plt.axis('off')


elif (ch=='3'):
    
#Roberts filter
    thres3=0.20
    #for gradient in x direction
    rb1 = np.array([[-1,0],[0,1]])
    #for gradient in y direction
    rb2 = np.array([[0,-1],[1,0]])
    ws=2
    pd=int((ws)/2);
    start=ws-pd;
    row,col=im.shape
    f=np.pad(im,[(pd,pd)],'edge')
    r,c=f.shape;
    robertsEdge1=np.zeros([row,col])
    robertsEdge2=np.zeros([row,col])
    for i in range(start,r-pd):
        for j in range(start,c-pd):
           window=f[(i-pd):(i+pd),(j-pd):(j+pd)];
           m1=np.multiply(rb1,window)
           m2=np.multiply(rb2,window)
           su1=np.sum(np.ravel(m1))
           su2=np.sum(np.ravel(m2))
           robertsEdge1[i-start,j-start]=su1;
           robertsEdge2[i-start,j-start]=su2;
    rb=np.abs(robertsEdge1)+np.abs(robertsEdge2)
    T3=thres3*max(np.ravel(rb))
    rob=np.multiply((rb>=T3),rb)
    plt.figure()
    plt.subplot(2,2,1),plt.imshow(np.abs(robertsEdge1),cmap='gray'),plt.title('Gradient X Direction')
    plt.axis('off')
    plt.subplot(2,2,2),plt.imshow(np.abs(robertsEdge2),cmap='gray'),plt.title('Gradient Y Direction')
    plt.axis('off')
    plt.subplot(2,2,3),plt.imshow(rb,cmap='gray'),plt.title('Gradient X+Y')
    plt.axis('off')
    plt.subplot(2,2,4),plt.imshow(rob,cmap='gray'),plt.title('Thresholded image')
    plt.axis('off')


elif (ch=='4'):
    
#laplacian of gaussian
    thres4=0.30
    #gaussian mask
    n=5; #Gaussian Window Size
    sigma=.5
    mu=0
    G=gauss(n,n,sigma,mu)
    gaussimg=convol(img,G)
    #laplacian mask
    ws=7 #Laplacian Window Size
    pd=int((ws-1)/2)
    lap =1*np.ones((ws,ws))
    lap[pd,pd]=-1*(np.sum(np.ravel(lap))-1)
    lapimg=convol(gaussimg,lap)
    logd=np.zeros(img.shape)
    T4=thres4*max(np.ravel(lapimg))
    #zerocrossing
    for i in range(1, r-1):
        for j in range(1, c-1):
            patch = lapimg[i-1:i+2, j-1:j+2]
            p = lapimg[i, j]
            maxP = patch.max()
            minP = patch.min()
            if (p > 0):
                zeroCross = True if minP < 0 else False
            else:
                zeroCross = True if maxP > 0 else False
            if ((maxP - minP) >= T4) and zeroCross:
                logd[i, j] = 1
        
    logd=np.clip(logd,0,255);                 
    plt.figure()
    plt.subplot(1,3,1),plt.imshow(gaussimg,cmap='gray'),plt.title('Gaussian Image')
    plt.axis('off')
    plt.subplot(1,3,2),plt.imshow(abs(lapimg),cmap='gray'),plt.title('LoG Image')
    plt.axis('off')
    plt.subplot(1,3,3),plt.imshow(logd,cmap='gray'),plt.title('Thresholded Image')
    plt.axis('off')


elif (ch=='5'):
    
#Canny filter
    lowthres=0.075
    highthres=0.175
    #gaussian mask
    n=5;
    sigma=2
    mu=0
    G=gauss(n,n,sigma,mu)
    fs=convol(im,G)
    #sobel operator
    Mx = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    My = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
    gx=convol(fs,Mx)         
    gy=convol(fs,My)
    M=np.sqrt(gx**2+gy**2)
    alpha=np.arctan(gx/gy)*180/np.pi
    alpha2=np.zeros([r,c],dtype='float')
        
    #Adjustment for negative directions, making all directions positive
    for i in range(r):
        for j in range(c):
            if (alpha[i,j]<0):
                alpha[i,j]=360+alpha[i,j];
    #Adjusting directions to nearest 0, 45, 90, or 135 degree
    for i in range(r):
        for j in range(c):
            if (((alpha[i, j] >= 0 ) & (alpha[i, j] < 22.5)) | ((alpha[i, j] >= 157.5) &(alpha[i, j] < 202.5)) | ((alpha[i, j] >= 337.5) & (alpha[i, j] <= 360))):
                alpha2[i, j] = 0;
            elif (((alpha[i, j] >= 22.5) & (alpha[i, j] < 67.5)) | ((alpha[i, j] >= 202.5) & (alpha[i, j] < 247.5))):
                alpha2[i, j] = 45;
            elif (((alpha[i, j] >= 67.5) & (alpha[i, j] < 112.5)) | ((alpha[i, j] >= 247.5) & (alpha[i, j] < 292.5))):
                alpha2[i, j] = 90;
            elif (((alpha[i, j] >= 112.5) & (alpha[i, j] < 157.5)) | ((alpha[i, j] >= 292.5) & (alpha[i, j] < 337.5))):
                alpha2[i, j] = 135;
                
    bw=np.zeros([r,c])
    #Non-Maximum Supression
    for i in range(1,r-1):
        for j in range(1,c-1):
            if (alpha2[i,j]==0):
                bw[i,j] = (M[i,j] == max((M[i,j], M[i,j+1], M[i,j-1])));
            elif (alpha2[i,j]==45):
                bw[i,j] = (M[i,j] == max((M[i,j], M[i+1,j-1], M[i-1,j+1])));
            elif (alpha2[i,j]==90):
                bw[i,j] = (M[i,j] == max((M[i,j], M[i+1,j], M[i-1,j])));
            elif (alpha2[i,j]==135):
                bw[i,j] = (M[i,j] == max((M[i,j], M[i+1,j+1], M[i-1,j-1])));
    bw = np.multiply(bw,M)
    #Thresholding
    T_Low = lowthres* max(np.ravel(bw));
    T_High = highthres * max(np.ravel(bw));
    T_res = np.zeros ([r,c]);
    
    for i in range(1,r-1):
        for j in range(1,c-1):
            if (bw[i,j] < T_Low):
                T_res[i, j] = 0;
            elif (bw[i,j] > T_High):
                T_res[i,j] = 1;
            #Using 8-connected components
            elif ( (bw[i+1,j]>T_High) | (bw[i-1,j]>T_High) | (bw[i,j+1]>T_High) | (bw[i,j-1]>T_High) | (bw[i-1, j-1]>T_High) | (bw[i-1, j+1]>T_High) | (bw[i+1, j+1]>T_High) | (bw[i+1, j-1]>T_High)):
                T_res[i,j] = 1;
    edge_final = T_res
    plt.figure()
    plt.subplot(131),plt.imshow(fs,cmap='gray'),plt.title('Gaussian of image')
    plt.axis('off')
    plt.subplot(132),plt.imshow(M,cmap='gray'),plt.title('Gradient of image')
    plt.axis('off')
    plt.subplot(133),plt.imshow(edge_final,cmap='gray'),plt.title('Thresholded Image')
    plt.axis('off')
    
   

elif (ch=='6'):
    exit()
else:
    print('Invalid Choice')

plt.show()
