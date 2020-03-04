# Task 6: Image filter and edge detection

**Name:** Kai Yang  
**Degree:** BA  
**ID:** 20640696  

## Problem 1: 2D Convolution (10 points)

a) The selected image is shown along with the results of the 2D convolution. The image was colour, so it needed to be split into individual RGB bands to be convoluded.  

```matlab
% Load image and resize to 250x200
temp_image = imread('problem1.jpg');
imSize = [250 200];
I = imresize(temp_image, imSize);

figure(1);
imshow(I);

% Define kernel
H = [0 -1 0;
    -1 4 -1;
    0 -1 0];

% Since baseImg is a colour image, split into RGB channels. Perform
% convolution on each individual channel, then combine back into image
IR = I(:,:,1);
IG = I(:,:,2);
IB = I(:,:,3);

IR_conv = conv2(IR,H,'same');
IG_conv = conv2(IG,H,'same');
IB_conv = conv2(IB,H,'same');

IR_conv = cat(3,IR_conv, zeros(imSize, 'uint8'), zeros(imSize, 'uint8')); 
IG_conv = cat(3, zeros(imSize, 'uint8'), IG_conv, zeros(imSize, 'uint8'));
IB_conv = cat(3, zeros(imSize, 'uint8'), zeros(imSize, 'uint8'), IB_conv);

I_new = IR_conv + IG_conv + IB_conv;

% display new image
figure();
imshow(I_new)
```

b) Convolution of the image using the same kernel but with a user defined convolution function results in the same image.  


```matlab
% Load image and resize to 250x200
temp_image = imread('problem1.jpg');
imSize = [250 200];
I = imresize(temp_image, imSize);

figure(1);
imshow(I);

% Define kernel
H = [0 -1 0;
    -1 4 -1;
    0 -1 0];

% Since baseImg is a colour image, split into RGB channels. Perform
% convolution on each individual channel, then combine back into image
IR = I(:,:,1);
IG = I(:,:,2);
IB = I(:,:,3);

IR_conv = conv2_forLoop(IR,H);
IG_conv = conv2_forLoop(IG,H);
IB_conv = conv2_forLoop(IB,H);

IR_conv = cat(3, IR_conv, zeros(imSize, 'uint8'), zeros(imSize, 'uint8')); 
IG_conv = cat(3, zeros(imSize, 'uint8'), IG_conv, zeros(imSize, 'uint8'));
IB_conv = cat(3, zeros(imSize, 'uint8'), zeros(imSize, 'uint8'), IB_conv);

I_new = IR_conv + IG_conv + IB_conv;

% display new image
figure();
imshow(I_new)

function conv_matrix = conv2_forLoop(matrix, kernel)
% Performs 2D convolution using for loops.
matrix = im2double(matrix);
matrixSize = [size(matrix,1) size(matrix,2)]; % rows, cols
conv_matrix = zeros(matrixSize);

kernelSize = [size(kernel,1) size(kernel,2)]; % rows, cols
kernel_centre_x = ceil(kernelSize(1)/2);
kernel_centre_y = ceil(kernelSize(2)/2);

for m_row = 1:matrixSize(1)
   for m_col = 1:matrixSize(2)
       for k_row = 1:kernelSize(1)
           k_row_flip = kernelSize(1) - (k_row - 1);
           for k_col = 1:kernelSize(2)
               k_col_flip = kernelSize(2) - (k_col - 1);
               
               ii = m_row + (kernel_centre_x - k_row_flip);
               jj = m_col + (kernel_centre_y - k_col_flip);
               
               if ii > 0 && jj > 0 && ii <= matrixSize(1) && jj <= matrixSize(2)
                   conv_matrix(m_row, m_col) = conv_matrix(m_row,m_col) + matrix(ii, jj) * kernel(k_row_flip, k_col_flip);
               end
           end
       end
   end
end
conv_matrix = im2uint8(conv_matrix);
end
```

## Problem 2: Different Kernels
