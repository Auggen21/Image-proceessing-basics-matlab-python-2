clc;clear all;close all
img=imread('wirebond.tif'); 
figure,imshow(img); title('Actual Image'); 
img=double(img);
%Horizontal
hz_mask=[-1 -1 -1 ; 2 2 2 ; -1 -1 -1]; 
ws=3;
pd=(ws-1)/2;
start=ws-pd;
f=padarray(img,[pd pd],'replicate');
[r,c]=size(f);
for i=start:r-pd
    for j=start:c-pd
        window=f(i-pd:i+pd,j-pd:j+pd);
        su=0;      
        for s=1:ws
            for t=1:ws
                su=su+hz_mask(s,t)*window(s,t);
            end
        end
        img_horiz(i-start+1,j-start+1)=su;
    end
end
%img_horiz=conv2(img,hz_mask); 
T1=max(img_horiz(:));
img_horiz=(img_horiz>=T1).*img_horiz;
figure,subplot(1,2,1); imshow(uint8(img_horiz)); title('Horizontal lines'); 

%Vertical
ver_mask=[-1 2 -1 ; -1 2 -1 ; -1 2 -1]; 
ws=3;
pd=(ws-1)/2;
start=ws-pd;
f=padarray(img,[pd pd],'replicate');
[r,c]=size(f);
for i=start:r-pd
    for j=start:c-pd
        window=f(i-pd:i+pd,j-pd:j+pd);
        su=0;      
        for s=1:ws
            for t=1:ws
                su=su+ver_mask(s,t)*window(s,t);
            end
        end
        img_vert(i-start+1,j-start+1)=su;
    end
end
%img_vert=conv2(img,ver_mask); 
T2=max(img_vert(:));
img_vert=(img_vert>=T2).*img_vert;
subplot(1,2,2); imshow(uint8(img_vert)); title('Vertical lines'); 

%+45 degree
diag1_mask=[2 -1 -1 ; -1 2 -1 ; -1 -1 2]; 
ws=3;
pd=(ws-1)/2;
start=ws-pd;
f=padarray(img,[pd pd],'replicate');
[r,c]=size(f);
for i=start:r-pd
    for j=start:c-pd
        window=f(i-pd:i+pd,j-pd:j+pd);
        su=0;      
        for s=1:ws
            for t=1:ws
                su=su+diag1_mask(s,t)*window(s,t);
            end
        end
        img_diag1(i-start+1,j-start+1)=su;
    end
end
%img_diag1=conv2(img,diag1_mask);
T3=max(img_diag1(:));
img_diag1=(img_diag1>=T3).*img_diag1;
figure,subplot(1,2,1); imshow(uint8(img_diag1)); title('Diagonal lines 45 degree'); 

%-45 degree
diag2_mask=[2 2 2 -1 -1 ; -1 2 2 2 -1 ; -1 -1 2 2 2;-1 -1 -1 2 2 ]; 
ws=3;
pd=(ws-1)/2;
start=ws-pd;
f=padarray(img,[pd pd],'replicate');
[r,c]=size(f);
for i=start:r-pd
    for j=start:c-pd
        window=f(i-pd:i+pd,j-pd:j+pd);
        su=0;      
        for s=1:ws
            for t=1:ws
                su=su+diag2_mask(s,t)*window(s,t);
            end
        end
        img_diag2(i-start+1,j-start+1)=su;
    end
end
%img_diag2=conv2(img,diag2_mask);
T4=max(img_diag2(:));
img_diag2=(img_diag2>=T4).*img_diag2;
subplot(1,2,2); imshow(uint8(img_diag2)); title('Diagonal lines -45 degree');