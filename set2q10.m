clear all
close all
img=imread('cameraman.tif'); 
[M N]=size(img);  
p=2*M; 
q=2*N; 
%FT of image centered 
F=fftshift(fft2(img,p,q)); 
%centre of the frequency rectangle 
cX=p/2; 
cY=q/2; 
%distance Metrix 
D=zeros(p,q); 
for i=1:p 
    for j=1:q 
        D(i,j)=sqrt((i-cX)^2+(j-cY)^2); 
    end
end

%ideal Low Pass Filter
D0=50; 
hid=(D<=D0); 
Ideal_Img=hid.*F; 
Ideal_Img=fftshift(Ideal_Img); 
Ideal_Img=real(ifft2(Ideal_Img)); 
Ideal_Img=Ideal_Img(1:M,1:N); 
subplot(2,2,1); 
imshow(img),title('Original Image'); 
subplot(2,2,2); imshow(uint8(Ideal_Img)),title('Ideal LPF output'); 

%Butterworth Filter 
n=5; %order
h_bu=zeros(p,q); 
for i=1:p 
    for j=1:q 
        h_bu(i,j)=1/(1+(D(i,j)/D0)^(2*n)); 
    end
end
btrWorth=h_bu.*F; 
btrWorth=fftshift(btrWorth); 
btrWorth=real(ifft2(btrWorth)); 
btrWorth=btrWorth(1:M,1:N); 
subplot(2,2,3); imshow(uint8(btrWorth)); title('Butterworth LPF Output');

%Guassian Low Pass Filter
G=zeros(p,q);
for i=1:p
    for j=i:q
        G(i,j)=exp(-D(i,j)^2/(2*D0^2));
    end
end
gsflt=G.*F;
gsflt=fftshift(gsflt);
gsflt=real(ifft2(gsflt));
gsflt=gsflt(1:M,1:N);
subplot(2,2,4);
imshow(uint8(gsflt));
title('Gaussian LPF Output');