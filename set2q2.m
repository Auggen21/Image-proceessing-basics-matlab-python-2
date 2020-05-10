clear all;
close all;
im=imread('galaxy_pair_original.tif');
im=double(im);
im=im/max(im(:));
[row,col]=size(im);
noisyimage=imnoise(im,'gaussian',0,.1); %AWGN with zero mean and variance 0.1
k=2;
sumimg2=zeros(row,col);
for i=1:k
    sumimg2=sumimg2+imnoise(im,'gaussian',0,.1);
end
avgimg2=sumimg2/k;
subplot(2,3,1)
imshow(noisyimage,[]),title('Original Image')
subplot(2,3,2)
imshow(avgimg2,[]),title('Averaging by 2')

k=8;
sumimg8=zeros(row,col);
for i=1:k
    sumimg8=sumimg8+imnoise(im,'gaussian',0,.1);
end
avgimg8=sumimg8/k;
subplot(2,3,3)
imshow(avgimg8,[]),title('Averaging by 8')

k=16;
sumimg16=zeros(row,col);
for i=1:k
    sumimg16=sumimg16+imnoise(im,'gaussian',0,.1);
end
avgimg16=sumimg16/k;
subplot(2,3,4)
imshow(avgimg16),title('Averaging by 16')

k=32;
sumimg32=zeros(row,col);
for i=1:k
    sumimg32=sumimg32+imnoise(im,'gaussian',0,.1);
end
avgimg32=sumimg32/k;
subplot(2,3,5)
imshow(avgimg32),title('Averaging by 32')

k=128;
sumimg128=zeros(row,col);
for i=1:k
    sumimg128=sumimg128+imnoise(im,'gaussian',0,.1);
end
avgimg128=sumimg128/k;
subplot(2,3,6)
imshow(avgimg128),title('Averaging by 128')