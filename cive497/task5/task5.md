# Task 5 - Homography

**Name:** Kai Yang  
**Degree:** BA  
**ID:** 20640696  

## Problem 1: Homogeneous Coordinates

a) The intersection computed using algebra is (4.3714, 2.5714).  

```matlab
% determine coefficients in the form y = m*x+b
line1_coeff = polyfit([3,5], [6,1], 1);
line2_coeff = polyfit([3,6], [-2,8], 1);

% arrange in matrix form alpha*x + beta*y = b
A = [-line1_coeff(1), 1; -line2_coeff(1),1];
b = [line1_coeff(2);line2_coeff(2)];

% compute intersect
intersect = A\b
```

b) The intersection computed using homogeneous coordinates is (4.3714, 2.5714).  

```matlab
l1 = cross([3,6,1]',[5,1,1]');
l2 = cross([3,-2,1]',[6,8,1]');
x = cross(l1,l2);

intersect = [x(1)/x(3); x(2)/x(3)]
```
## Problem 2: Homogeneous Coordinate (Conic)

a) The computed intersection using conic method is (-2.3333, 0).  

```matlab
% define conic parameters
a = 1/2/2;
b = 0;
c = 1/3/3;
d = -6/2/2;
e = -4/3/3;
f = -2 + 9/2/2 + 4/3/3;

% determine line tangent to (1,5)
conic = [a b/2 d/2; b/2 c e/2; d/2 e/2 f];
tangent = conic*[1;5;1];

% determine the intersection of the x axis
x_axis = [0,1,0];
x = cross(tangent, x_axis);
intersect = [x(1)/x(3), x(2)/x(3)]
```

b) The intersect of the two tangent lines is (-1, 2).  

```matlab
% define conic parameters
a = 1/2/2;
b = 0;
c = 1/3/3;
d = -6/2/2;
e = -4/3/3;
f = -2 + 9/2/2 + 4/3/3;

% determine line tangent to (1,5)
conic = [a b/2 d/2; b/2 c e/2; d/2 e/2 f];
tangent1 = conic*[1;5;1];
tangent2 = conic*[1;-1;1];

% determine the intersection of the tangent lines
x = cross(tangent1, tangent2);
intersect = [x(1)/x(3), x(2)/x(3)]
```

## Problem 3: Homogeneous Coordinate (Lines)

If the 4 lines are not parallel, each line will have 3 intersections (each with another line). When comparing the intersections of any two lines, there will always be 4 unique intersections and 1 common intersection. The quadralateral bounded by the 4 lines are comprised of the 4 unique intersections which form the smallest area. The code to compute the points which make up the quadralaterial is as follows.  

The four points which bound the quadrilateral is (0.5797, 3.7246), (3.8462, -3.4615), (-4.8889, -3.1111), and (-2.1429, -5.8571).  

![](https://lh3.googleusercontent.com/OCeFFBC7sAGiRkAQvl8iLNmgMYTpVG1w0I9wUlL8hTX7gkzgG-BCSCmxyLZrkUSlaLK5RCJ5RLyojwRlYAdudJhY4exyppPLKm_AMfTO8t6kxBRSWVUpc5M_gUlyxOCOml5Kv5mBZVKzT9Rq0Tca7PY_e8wmsD2iXSYScuZbm_4xzHtAtcnq1KrumaJxAlcQ9fAzcc2y3kVb3RE8i-vnV1tkp1B6FM5BaonltUk7FKLXavyCzWP1JrWm_a5f063kJX7CmoWaD9YR2sv0nw2J11IeKWEo1BNR9ZYglNwwE40woIMK936J-gkqFwoD8j3RoOoPILV39W_rWcRe4CikvcV0oUXTfMzG92nfN_pjij08N-A0XesDWRpBmix6Xyc02ZUHIQBA3WNK2K8ZmdkNuRyeGF0VHRxxpypzs4eI2flacQ2_tbvPUxTZ1hnBhE1OfBYvP37WAPMEVkfEF37grs07dQqZjh9EfiGQfRnZqr5nyJNb1XQWEURvyia4tv_ugRrJYS3W5mUpsYGdmwsE7CG-YYdiphOJQ16JOsL9Ep5Nn9k2ijLqIyvAON8uyjqCJm9irwrojQ8zmjAQqSdooq_Q8NWlwGhQ9CTi5iRgDlJO1AsN9OdH4yzmlfyZgQgkMoMZyGUxUCe1z_XoEo1EmZPRt7wEQMQLN_LbGDZKeZf3odfuc3aFTw=w1006-h443-no)  

```matlab
lines = [1.25, -1, 3;
      0.4, -1, -5;
      -2.2, -1, 5;
      -1, -1, -8];

% every line will have 3 intersections
intersection_x = zeros(4,3); % the specific intersection is indexed with row, intersection
intersection_y = zeros(4,3);

% find all intersections of the 4 lines
line_index = [1,2,3,4];
for n = 1:4
    compare = line_index(line_index ~= n);
    line1 = lines(n,:);
    for m = 1:3
        line2 = lines(compare(m),:);
        x = cross(transpose(line1), transpose(line2));
        intersection_x(n, m) = x(1)/x(3);
        intersection_y(n, m) = x(2)/x(3);
    end
end
intersection_x
intersection_y

% For any two lines, there will be 4 unique intersection and 1 common
% intersection. The quadrilateral will be the 4 unique intersections which
% has the minimum area.

% Compare lines. Compute area of unique intersection.
quad_area = 10^12; % start with an arbitrarily large number
quad_points_x = [];
quad_points_y = [];
area_compare = [1,2,3,4];
for n = 1:3 % only need to loop 3 times because cannot compare line 4 to itself
    area_compare = area_compare(area_compare ~= n);
    
    % extract x,y intersection information of line 1
    line1_int_x = intersection_x(n,:);
    line1_int_y = intersection_y(n,:);
    
    % compare line 1 with the other lines and determine the unique intersections
    for m = 1:length(area_compare)
       line2_int_x = intersection_x(area_compare(m),:); 
       line2_int_y = intersection_y(area_compare(m),:); 
       
       x_common = intersect(line1_int_x, line2_int_x);
       line1_x_unique = line1_int_x(line1_int_x ~= x_common);
       line2_x_unique = line2_int_x(line2_int_x ~= x_common);
       
       y_common = intersect(line1_int_y, line2_int_y);
       line1_y_unique = line1_int_y(line1_int_y ~= y_common);
       line2_y_unique = line2_int_y(line2_int_y ~= y_common);
       
       area_temp = polyarea([line1_x_unique, line2_x_unique], [line1_y_unique, line2_y_unique]);
       
       if area_temp < quad_area
           quad_points_x = [line1_x_unique, line2_x_unique];
           quad_points_y = [line1_y_unique, line2_y_unique];
       end
    end
end

quad_points_x
quad_points_y
```
## Part 4: Linear Algebra

a) The tranpose and inverse of H is as follows.  

![](https://latex.codecogs.com/gif.latex?%5Clarge%20H%5E%7B-1%5E%7BT%7D%7D%20%3D%20%5Cbegin%7Bbmatrix%7D%201%20%26%200%26%20-%5Cfrac%7Bl_%7B1%7D%7D%7Bl_%7B3%7D%7D%5C%5C%200%20%26%201%26%20-%5Cfrac%7Bl_%7B2%7D%7D%7Bl_%7B3%7D%7D%5C%5C%200%20%26%200%26%20-%5Cfrac%7B1%7D%7Bl_%7B3%7D%7D%20%5Cend%7Bbmatrix%7D)  

```matlab
syms l_1 l_2 l_3

H = [1, 0, 0;
    0,1,0;
    l_1, l_2, l_3];

transpose(inv(H))
```

b) The row space is the vector space spanned by the rows in a matrix.  

The null space is the solution set of vector x such that Ax = 0. If A is an m x n matrix and x is a n x 1 vector, then then the null space is trivial (ie. x = 0).  

Given matrix A, the rank and null space of the matrix are as follows.  

![](https://latex.codecogs.com/gif.latex?%5Clarge%20rank%28A%29%20%3D%203)  

![](https://latex.codecogs.com/gif.latex?null%28A%29%20%3D%20%5Cbegin%7Bbmatrix%7D%20-0.5350%20%26-0.4275%20%5C%5C%20-0.0324%20%26-0.6341%20%5C%5C%200.7961%20%26-0.1001%20%5C%5C%20-0.2091%20%26%200.3131%20%5C%5C%20-0.1878%20%26%200.5542%20%5Cend%7Bbmatrix%7D)  

c) The system is underdetermined, meaning more unknowns than equations, so a non-trival solution will exist. The null vector x, such that Ax = 0, was computed using Matlab.  

![](https://latex.codecogs.com/gif.latex?null%28a%29%20%3D%20%5Cbegin%7Bbmatrix%7D%20-0.5350%20%26%20-0.4275%5C%5C%20-0.0324%20%26%20-0.6341%5C%5C%200.7961%20%26%20-0.1001%5C%5C%20-0.2091%20%26%200.3131%5C%5C%20-0.1878%20%26%200.5542%20%5Cend%7Bbmatrix%7D)  

d) The system is underdetermined, so a non-trial solution will exist. The null vector x, such that Ax = 0, was computed using Matlab.  

![](https://latex.codecogs.com/gif.latex?null%28A%29%20%3D%20%5Cbegin%7Bbmatrix%7D%200.0000%20%26%200.0000%26%20-0.8944%5C%5C%200.8018%26%200.5345%20%26%200.0000%5C%5C%200.4927%20%26%20-0.3382%20%26%20-0.0000%5C%5C%20-0.3382%20%26%200.7745%20%26%20-0.0000%5C%5C%20-0.0000%20%26%20-0.0000%20%26%200.4472%20%5Cend%7Bbmatrix%7D)  

## Problem 5: Image Overlay

a) The result of the image overlay is presented in the following figure.  

![](https://lh3.googleusercontent.com/SV0ov4ER6Pw9C0ZX5Uz66PBZjKakME15hG7GTAdVYY4-S7ApvpXOH-SAgTFIHRN1E35x5K_U5n3GqGVJn4t8cYoKK9WLIX1dz8serO-m9q9b4C4SwW51OnxZwgolvdnBe-om12wpVO6MubDMyIV00OIVPHxhm07rB0FaScLHqpIyykTivmWDH5Y_JdtUOGOBKyf3juxYZICCAVDIhZYn-ru-wTOdEKr2_uw94lR4kwy8v5Miib0HSDa5tUSWQDmu_rVWbAQkkS_MjRYr2luGKQpJ3siIIDCojOvvRSsF3rDHDKj9ZtuEgtlhJwp88j0XcfeNFvmNRzmivj9-lO6E0IzrvLK1Qnm9xfuMiB959GXHiG12ZQ7eoMoJU9M9A7JY1HVSG40sdAz-jk_lmGVdAbiOZZvMwLZY5Cq_9lSxqygVFMOI8SvBqIkSHCh9bH1613sCeSOMPiaCKYJ_yd3RtfcDnkKFWalSMYHshITTojZDb35ohHCtq64TMfw2HfXlEnluqoDaYo9POSrRYd9Z_yJQo93WDjGyPm2vD8BCf8Bc3gbofFsH_8m_lG24qjbgCAPRFQf16fxJ6zizCWmeJ5AcOXUuBITBZ91knAlH7miTuBwgXNzOSwLE1mqbYaeb2YUtkEVWQsYQM0qOjtYB5ZWPB3IYJrRivpvX7j4eN08tNkGkCHufMQ=w881-h625-no)  

```matlab
% Image Overlay
% Author: Chul Min Yeum (cmyeum@uwaterloo.ca)
% Adjusted by Kai Yang
% Last update:: 02/12/19
clear; close all; clc; format shortG;

%% Parameter
imgBoardFile = 'my_office.png';
imgPicFile = 'lady_of_shallot.jpg';

info = imfinfo(imgPicFile);
sizePic = [info.Width info.Height];

%% Step1: Determine the four corners of the white board (a)
imgBoard = imread(imgBoardFile);

corner = [96, 360; %top left
          97, 952; %bottom left
          689, 830; %bottom right
          685, 438]; %top right

pgon = polyshape(corner);
figure(1); imshow(imgBoard); hold on;
plot(pgon);

%% Step2: Compute H (Your Section)
H = ComputeH(corner, sizePic);

%% Step3: Overlay your picture (I think there is a better way to do this)
imgPic = imread(imgPicFile);
[imgPicTran, RB] = imwarp(imgPic, projective2d(H));
BWPic = roipoly(imgPicTran, corner(:,1)-RB.XWorldLimits(1), corner(:,2)-RB.YWorldLimits(1));


BWBoard = ~roipoly(imgBoard, corner(:,1), corner(:,2));
RA = imref2d(size(BWBoard));

imgBoardMask = bsxfun(@times, imgBoard, cast(BWBoard, 'like', imgBoard));
imgPicTranMask = bsxfun(@times, imgPicTran, cast(BWPic, 'like', imgPicTran));

imgFinal(:,:,1) = imfuse(imgBoardMask(:,:,1),RA, imgPicTranMask(:,:,1),RB,'diff');
imgFinal(:,:,2) = imfuse(imgBoardMask(:,:,2),RA, imgPicTranMask(:,:,2),RB,'diff');
imgFinal(:,:,3) = imfuse(imgBoardMask(:,:,3),RA, imgPicTranMask(:,:,3),RB,'diff');

imshow(imgFinal); imwrite(imgFinal, 'result.jpg');

function H = computeH(corner, sizePic)
%   Computes the homography matrix using singular value decomposition
%   sizePic = [width height]

% define coordinates for original image
x1 = 1; y1 = 1; % top left
x2 = 1; y2 = sizePic(2); % bottom left
x3 = sizePic(1); y3 = sizePic(2); % bottom right
x4 = sizePic(1); y4 = 1; % top right

% define coordinates for projection area
x1_ = corner(1,1); y1_ = corner(1,2);
x2_ = corner(2,1); y2_ = corner(2,2);
x3_ = corner(3,1); y3_ = corner(3,2);
x4_ = corner(4,1); y4_ = corner(4,2);

% define homography matrix
A = [
    -x1  -y1  -1   0    0    0   x1*x1_   y1*x1_   x1_;
     0    0    0 -x1   -y1  -1   x1*y1_   y1*y1_   y1_;
    -x2  -y2  -1   0    0    0   x2*x2_   y2*x2_   x2_;
     0    0    0 -x2   -y2  -1   x2*y2_   y2*y2_   y2_;
    -x3  -y3  -1   0    0    0   x3*x3_   y3*x3_   x3_;
     0    0    0 -x3   -y3  -1   x3*y3_   y3*y3_   y3_;
    -x4  -y4   -1  0    0    0   x4*x4_   y4*x4_   x4_;
     0    0    0  -x4  -y4  -1   x4*y4_   y4*y4_   y4_];
 
% solve H matrix
[U,S,V] = svd(A);
H = V(:,end)./V(end,end);
H = reshape(H,3,3);
end
```



b) The result of the image overlay is presented in the following figure.  

![](https://lh3.googleusercontent.com/aHHsTEh5WWc6dNnAP84q-4AE1oX4pPIY6iAJlXqz4Zz6kNn2PhSMw8ylV4UpzWLMCAnZeNwmslBHbu7Liuf94te4CtOmMFo8gptoW5fYCNVzCHz7gQ4mdq4tX4DgT0B2SmZQIVCztpFR9TGUgTS-GMC3j7sY71N7SbqFUOhUEgaCHU7fY--Q6fvDJKLK2u_XGm3-iJVpHcm73wTFM_7Cqmgq1vpBB3LKb79q0GYzHNceaO0JvyfeICH-2FawqpCy4_ZufisYElux8d7Paz0zjKhCIalCjEhsfagYdxcIzFhGt7jtW2xNnyHlWWZkzaygyw1bl0anCpIEZLCoRIRYolwDjlajcn7C0uKQsyhdwaHjom-nVS8dlbVX6JsRfTK1qYeJrfKKLeenKyFBYOaWXRgn2sRtAJvWVQ7_YULEF9JbBLAUJ7TS2hAYqgG5uX44pjy3MEl51cOcBtKT0hbkGZzIyTm1HQ0NVcTc6AwPnGhtXkIaQSSwgxSUaCLbaBr1TKtnd5TDSAJl0iD8PUsWmk6tU4fIfWfyOm7S895usSzEn3t1nBkCX_quM3K8joumNOuWftfRixj842ZXeQmbavB46_8zXjs1H_F364mnI-51zjnXLbCzFnxYebOeOTW05SIDf1vLIem6xPHAYFc8e7g8H372cDD0ceyndVQxh-1OetYPwakXQw=w872-h603-no)  

```matlab
% Image Overlay
% Author: Chul Min Yeum (cmyeum@uwaterloo.ca)
% Adjusted by Kai Yang
% Last update:: 02/12/19
clear; close all; clc; format shortG;

%% Parameter
imgBoardFile = 'award.png';
imgPicFile = 'blursed.jpg';

info = imfinfo(imgPicFile);
sizePic = [info.Width info.Height];

%% Step1: Determine the four corners of the white board (a)
imgBoard = imread(imgBoardFile);

corner = [540, 560; %top left
          540, 950; %bottom left
          1033, 950; %bottom right
          998, 555]; %top right

pgon = polyshape(corner);
figure(1); imshow(imgBoard); hold on;
plot(pgon);

%% Step2: Compute H (Your Section)
H = ComputeH(corner, sizePic);

%% Step3: Overlay your picture (I think there is a better way to do this)
imgPic = imread(imgPicFile);
[imgPicTran, RB] = imwarp(imgPic, projective2d(H));
BWPic = roipoly(imgPicTran, corner(:,1)-RB.XWorldLimits(1), corner(:,2)-RB.YWorldLimits(1));


BWBoard = ~roipoly(imgBoard, corner(:,1), corner(:,2));
RA = imref2d(size(BWBoard));

imgBoardMask = bsxfun(@times, imgBoard, cast(BWBoard, 'like', imgBoard));
imgPicTranMask = bsxfun(@times, imgPicTran, cast(BWPic, 'like', imgPicTran));

imgFinal(:,:,1) = imfuse(imgBoardMask(:,:,1),RA, imgPicTranMask(:,:,1),RB,'diff');
imgFinal(:,:,2) = imfuse(imgBoardMask(:,:,2),RA, imgPicTranMask(:,:,2),RB,'diff');
imgFinal(:,:,3) = imfuse(imgBoardMask(:,:,3),RA, imgPicTranMask(:,:,3),RB,'diff');

imshow(imgFinal); imwrite(imgFinal, 'result.jpg');

function H = computeH(corner, sizePic)
%   Computes the homography matrix using singular value decomposition
%   sizePic = [width height]

% define coordinates for original image
x1 = 1; y1 = 1; % top left
x2 = 1; y2 = sizePic(2); % bottom left
x3 = sizePic(1); y3 = sizePic(2); % bottom right
x4 = sizePic(1); y4 = 1; % top right

% define coordinates for projection area
x1_ = corner(1,1); y1_ = corner(1,2);
x2_ = corner(2,1); y2_ = corner(2,2);
x3_ = corner(3,1); y3_ = corner(3,2);
x4_ = corner(4,1); y4_ = corner(4,2);

% define homography matrix
A = [
    -x1  -y1  -1   0    0    0   x1*x1_   y1*x1_   x1_;
     0    0    0 -x1   -y1  -1   x1*y1_   y1*y1_   y1_;
    -x2  -y2  -1   0    0    0   x2*x2_   y2*x2_   x2_;
     0    0    0 -x2   -y2  -1   x2*y2_   y2*y2_   y2_;
    -x3  -y3  -1   0    0    0   x3*x3_   y3*x3_   x3_;
     0    0    0 -x3   -y3  -1   x3*y3_   y3*y3_   y3_;
    -x4  -y4   -1  0    0    0   x4*x4_   y4*x4_   x4_;
     0    0    0  -x4  -y4  -1   x4*y4_   y4*y4_   y4_];
 
% solve H matrix
[U,S,V] = svd(A);
H = V(:,end)./V(end,end);
H = reshape(H,3,3);
end
```

## Problem 6

The test image used by the program is shown below. The paper is letter sized (215.9 x 279.4 mm). The ruler and the straight edge of the protractor was measured using homography techniques.  

![](https://lh3.googleusercontent.com/JtnB3PHLZ4gClAbrYcNzJXt5ws2ICr8Uf0MaxamBeOyiSRg4wxaMeqR41o2mtPRbmw9SccMLltTrGPcDXdaRcpOv5-zZtsGKjQnOhVfl-Da_zRhyTCNzVdyklBo6kyL-IJIxzyvveYq07gEHNeXYC7-UoF0IhGcjQ9EwPrS0oW_zfoNkwpfz5dOeHHemd34jvyYumeLlXbzPbgKkW1L9Ux72BPGGOHpqED4dGGKsLWfIqNXyldvndM8o5fZFKhg6YMfEAXOKo0u5R-flUzKqXKKaIlg_d8bxsdh8m9PNRt_LbOYUwAbNicOxt6yl8ZPCt5dJUW4xjA3eZXdgS6n4hVRNRKlUxWe4frdWLhpxEVj1S-rb6siO5z2Tc1fAhuuGEsGGS_Mz-NV_wrsjYjy78yenj6dUmdHKzlvFoNNewQeFzB_nHlDxn06hH_Xd8qlgyJk-mjwCOmWA5otzL2Vx8BorxcVnB4oVdeZGSH5SMuJ9vpvGbe6-t6kg8mSYg82g_TRqKqk8q5doTTxIdJEGXyWH1ONL_KDhUdfq1AJFWVeFarfpMKebLVGKSRJdNElJh_AvVqsSLuKgF_lftAiRRAduzmcSXIz9gHjLgAQGSkAFWzdX_nfSAK_jen_3jbkR2Xcpcp_kEP0QStvIbJjFKrO_38dkkeX7xE3ANRRH8BlRtndYF7gAbQ=w834-h625-no)  

The results of the program's measurements are overlaid in the picture. All units are in millimetres. Also shaded is the user-defined region of the paper.  

![](https://lh3.googleusercontent.com/pNafjne6snzQmHnfQ6oEjZ2a-WtqPZjntCoOyV9GMrsEN6Y9dhvny5vjV94veOxaCmOyTv9SSdpGyJskSRK73GrIm0wCPG-IGESN2VTubGQSfFjV0CZ9AS7p8jO4CZkfZuCxocv08FGNJZOhmya5c99P4RZLdCptZbYY_3GZO9QQCWv0FelKdklonb4Z11wTsw0xrsQxaj-cVUz2e-5qWX0U-A2oJtWKsmFsKogBWzwXpLGpzHpl8HfcrS_hCt9bcCXr4AGJjM72YaUfQ9DcUvn1j-8uwpumJrE3aGiqZS8-d7jxZhipk7ihImOlcgLAGFUrMGTAmX9QHv6TV2JnzOWmXb6z_lXqDVDy6j69qvedS_-G_IcgFNTSa7U7nqz6Md9_BMkXAhFZ3Ae9iFQSNxH7YmBM32LnhVxmBHiuVb46CPwhdmaQHCSUZ-PY9-QgqFkPwYbtpFd_mrdFdkAGNAmrthK0atKRfFvb2xw0pu9Aglnug7YKgUPt2nzS6mlTCSmNhetyvbhJ2zkQLP6GPTew8Ski9sbbBTk8POay6bTnMoaOQsAkbz-o5a84M5PURjBvEQT5sjIZDFINIoNUIAeC5v6PwZWgyzFjsEjHfibK0TukQeVxXg_ZKIH5JjE83-OC_6KXz86YWaRUtTYwlg55VFuzjRzlimG8stFmDqL1OlPNBL2RQQ=w846-h597-no)  

The true length of the ruler is 150 mm and the true length of the straight edge of the protractor is 101 mm. As expected, the measured values are close, but not exactly the true lengths. This can be attributed to user input error. For example, the outline of the paper may not be an accurate trace. Additionally, the lines may not start and end exactly at the correct locations.  

![](https://lh3.googleusercontent.com/F1YbLsfhFZhlVM2VHSh2U9UKZKikmfRzZROYOjeAZv90oIXN5RrzARE-hfVczQPJ__LOruOAzHUMh5K4iXEdDwY1BTQfggecQ986lLppzihv24CKacV8Mebj-A6m21LygJDsqidBh69QYbI76HofGRGo1_XOOUE5fZn-qBLVjcwm2UpU0W5_d__H2Q58bWApTaTGOuqDYc4juDsZ1cUWfeL3STkVRiYPoGY6GuYuICUNaIAqCwPoFJ3BWWyduJVrIz69woRggmIZQ8JMvIwCF8OvqICcQWy48kgax9tuLyvlWvf-LV10-fMxHEXca-jot-XlCvBq4QwxZQPzhTg6WjX9M0PAc29u7Qt1UtU24WM84ANn-5nOcEV5iskz23AJH__9xTPrmJvm_bo8XJO0Qo4wcA0eQ4l1vLgIqQTYI4nFysAk8dmsUO6pmTAVdifJI7mIonzDIZ-4HdWuuwgV38O5a9M5Sj8t3e4lnIUKMxzg9d_7Zv942ZIawC0ApERQlwCiYklxo6hxBCI5tpjukgBFZqjhfD-8VTzjgu4kVdSZ6g28saEIbkETZCm54OhIh9WA87qjMmDFu5Its9NoEKilVvgACKxQwELGWKNTYTKimJfK0xdMEMEIX9zmPD9NYLoqyVeIZB3ZmXTdvVw-GTZDzJevCPoRBfV3oaCU3lfbQSXXTcU7MQ=w834-h625-no)  

```matlab
% Task 5 Question 6 - Program to measure distances on a plane
% Kai Yang 20640696

% Load Parameters
baseImgFile = 'image.jpg';
paperSize = [215.9 279.4]; % 8.5 by 11 in paper measured in mm

info = imfinfo(baseImgFile);
sizePic = [info.Width info.Height];

% Determine the four corners of the paper. Start at top left corner and go
% counter-clockwise
baseImg = imread(baseImgFile);
figure(1); imshow(baseImg);
p = drawpolygon('LineWidth',0.5,'Color','black');
corner = p.Position; close(1);

% Determine 2 lines on the plane to measure
figure(2); imshow(baseImg);
drawline1 = drawline('LineWidth', 0.5, 'Color', 'red');
line1 = drawline1.Position; close(2);

figure(3); imshow(baseImg);
drawline2 = drawline('LineWidth', 0.5, 'Color', 'red');
line2 = drawline2.Position; close(3);

% Compute homography matrix
corner_xy = corner;
corner_xy(:,2) = sizePic(2) - corner(:,2); % convert to normal xy-coordinates
H = computeH(corner_xy, paperSize);

% Compute distances of the two lines
line1_xy = line1;
line1_xy(:,2) = sizePic(2) - line1(:,2); % convert to normal xy-coordinates
line1_dis = computeLength(H', line1_xy);

line2_xy = line2;
line2_xy(:,2) = sizePic(2) - line2(:,2); % convert to normal xy-coordinates
line2_dis = computeLength(H', line2_xy);

% Display image, selected areas and distances
pgon = polyshape(corner);

figure(4); imshow(baseImg); hold on;
plot(pgon); 
plot(line1(:,1), line1(:,2), 'r-', 'LineWidth', 0.5);
plot(line2(:,1), line2(:,2), 'r-', 'LineWidth', 0.5);
text((line1(1,1)+line1(2,1))/2, ...
    (line1(1,2)+line1(2,2))/2, num2str(line1_dis))
text((line2(1,1)+line2(2,1))/2, ...
    (line2(1,2)+line2(2,2))/2, num2str(line2_dis))
    
function H = computeH(corner, paperSize)
%   Computes the homography matrix using singular value decomposition
%   sizePic = [width height]

% define paper coordinates in image
x1 = corner(1,1); y1 = corner(1,2); % top left
x2 = corner(2,1); y2 = corner(2,2); % bottom left
x3 = corner(3,1); y3 = corner(3,2); % bottom right
x4 = corner(4,1); y4 = corner(4,2); % top right

% define paper coordinates for flat planar projection 
x1_ = 0;            y1_ = 0;             % top left
x2_ = 0;            y2_ = -paperSize(2); % bottom left
x3_ = paperSize(1); y3_ = -paperSize(2); % bottom right
x4_ = paperSize(1); y4_ = 0;             % top right

% define homography matrix
A = [
    -x1  -y1  -1   0    0    0   x1*x1_   y1*x1_   x1_;
     0    0    0 -x1   -y1  -1   x1*y1_   y1*y1_   y1_;
    -x2  -y2  -1   0    0    0   x2*x2_   y2*x2_   x2_;
     0    0    0 -x2   -y2  -1   x2*y2_   y2*y2_   y2_;
    -x3  -y3  -1   0    0    0   x3*x3_   y3*x3_   x3_;
     0    0    0 -x3   -y3  -1   x3*y3_   y3*y3_   y3_;
    -x4  -y4   -1  0    0    0   x4*x4_   y4*x4_   x4_;
     0    0    0  -x4  -y4  -1   x4*y4_   y4*y4_   y4_];
 
% solve H matrix
[U,S,V] = svd(A);
H = V(:,end)./V(end,end);
H = reshape(H,3,3);
end

function L = computeLength(H,lineCoor)
%   Computes the lengths of the line using the homography matrix
%   This function only takes line inputs (ie. two coordinate points)
if size(lineCoor, 1) ~= 2
    error('Only two coordinate points')
end

% define line coordinates
x1 = lineCoor(1,1); y1 = lineCoor(1,2); % first point
x2 = lineCoor(2,1); y2 = lineCoor(2,2); % second point

% compute transformed points
p1 = H * [x1 y1 1]';
p2 = H * [x2 y2 1]';

% convert points from homogenous coordinates to euclidian coordinates
x1_ = p1(1)/p1(3);
y1_ = p1(2)/p1(3);
x2_ = p2(1)/p2(3);
y2_ = p2(2)/p2(3);

% compute the length
L = sqrt((x1_ - x2_)^2 + (y1_ - y2_)^2);

end
```
