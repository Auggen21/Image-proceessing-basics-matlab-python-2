clc;
clear all;
close all;
%addition
im1=imread('cameraman.tif');
im2=imread('rice.png');
im1=double(im1);
im2=double(im2);
[r1,c1]=size(im1);
im2=imresize(im2,[r1,c1]);
a=im1+im2;
a=255*a/max(a(:));
subplot(1,3,1)
imshow(uint8(im1)),title('First Image')
subplot(1,3,2)
imshow(uint8(im2)),title('Second Image') 
subplot(1,3,3)
imshow(uint8(a)),title('Added Image') 

%subtraction
im3=imread('angiography_mask_image.tif');
im4=imread('angiography_live_ image.tif');
[r2,c2]=size(im3);
im4=imresize(im4,[r2,c2]);
b=im3-im4;
figure,subplot(2,2,1)
imshow(im3),title('First Image')
subplot(2,2,2)
imshow(im4),title('Second Image') 
subplot(2,2,3)
imshow(uint8(b)),title('Subtracted Image') 
subplot(2,2,4)
imshow(imadjust(b)),title('Enhanced Subtracted Image') 

%multiplication
im5=imread('dental_xray.tif');
im6=imread('dental_xray_mask.tif');
im5=double(im5);
im6=double(im6);
[r3,c3]=size(im5);
im6=imresize(im6,[r3,c3]);
c=im5.*im6;
c=255*c/max(c(:));
figure,subplot(1,3,1)
imshow(uint8(im5)),title('First Image')
subplot(1,3,2)
imshow(uint8(im6)),title('Second Image') 
subplot(1,3,3)
imshow(uint8(c)),title('Image Multiplication')

% Division
im7=imread('tungsten_filament_shaded.tif');
im8=imread('tungsten_sensor_shading.tif');
im7=double(im7);
im8=double(im8);
[r4,c4]=size(im7);
im8=imresize(im8,[r4,c4]);
rec=1./im8;
d=im7.*rec;
d=255*d/max(d(:));
figure,subplot(1,3,1)
imshow(uint8(im7)),title('First Image')
subplot(1,3,2)
imshow(uint8(im8)),title('Second Image') 
subplot(1,3,3)
imshow(uint8(d)),title('Image Division for Shading Correction ') 
