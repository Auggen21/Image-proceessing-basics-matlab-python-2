clear all
close all
img=imread('moon.tif'); 
img=double(img.');
[M N]=size(img); 
p=2*M; 
q=2*N; 

%FT 
Ft=fftshift(fft2(img,p,q)); 
%centre of the frequency rectangle 
cX=p/2; 
cY=q/2; 
%Distance Metrix 
D=zeros(p,q); 
for i=1:p 
    for j=1:q 
        D(i,j)=sqrt((i-cX)^2+(j-cY)^2); 
    end
end

%ideal High pass Filter
D0=50; 
H_id=(D>D0); 
Idl_Img=H_id.*Ft; 
Idl_Img=fftshift(Idl_Img); 
Idl_Img=real(ifft2(Idl_Img)); 
Idl_Img=Idl_Img(1:M,1:N); 
Idl_Img=Idl_Img+img; 
subplot(2,2,1),imshow(uint8(img)),title('Original Image'); 
subplot(2,2,2),imshow(uint8(Idl_Img)),title('Ideal HPF Output'); 

%Butterworth Filter 
n=5; 
h_bu=zeros(p,q); 
for i=1:p 
    for j=1:q 
        h_bu(i,j)=1-(1/(1+(D(i,j)/D0)^(2*n))); 
    end
end
btrWorth=h_bu.*Ft; 
btrWorth=fftshift(btrWorth); 
btrWorth=real(ifft2(btrWorth));
btrWorth=btrWorth(1:M,1:N); 
btrWorth=btrWorth+img; 
subplot(2,2,3); imshow(uint8(btrWorth));
title('Butterworth HPF Output');

%Guassian high Pass Filter
G=zeros(p,q);
for i=1:p
    for j=i:q
        G(i,j)=1-(exp(-D(i,j)^2/(2*D0^2)));
    end
end
gsflt=G.*Ft;
gsflt=fftshift(gsflt);
gsflt=real(ifft2(gsflt));
gsflt=gsflt(1:M,1:N);
gsflt=gsflt+img;
subplot(2,2,4);
imshow(uint8(gsflt));
title('Gaussian HPF Output');