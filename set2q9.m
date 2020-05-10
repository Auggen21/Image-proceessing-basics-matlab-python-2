close all
clear all
im=imread('cameraman.tif');
[n,m]=size(im);

%without padding
DFT=fftshift(fft2(im));
h=fspecial('gaussian',[n,m],1) %create h matrix with size of img, sigma=8
H=fftshift(fft2(h)); 
F=H.*DFT;
f=ifft2(F);
f=fftshift(abs(f));
f=uint8(f);
figure,imshow(im),title('Original Image');
figure,imshow(repmat(f,3,3)),title('DFT Filtering Periodicty - Without Padding');
figure,imshow(f),title('DFT Filtering - Without Padding');

%with padding -to avoid wraparround error due to periodicity of FT
p=n*2;
q=m*2 % for mxn matrix pad size P>=2m-1 and Q<=2n-1
FP=fftshift(fft2(im,p,q)); %make im size of p, q with zero padding  
HP=fspecial('gaussian',[p q],1);
HP=fftshift(fft2(HP));
RP=HP.*FP;
AP=ifft2(RP);
AP=fftshift(abs(AP));
AP=uint8(AP);
Gwopd=AP(1:n,1:m); 
figure,imshow(repmat(Gwopd,3,3)),title('DFT Filtering Periodicty - With Padding');
figure,imshow(Gwopd),title('DFT Filtering - With Padding');


