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

```matlab
lines = [1.25, -1, 3;
      0.4, -1, -5;
      -2.2, -1, 5;
      -1, -1, -8];

% every line will have 3 intersections
intersection_x = zeros(4,3);
intersection_y = zeros(4,3);

% find all intersects
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
quad_area = 10^12; % start with an aarbitrarily large number
quad_points_x = [];
quad_points_y = [];
area_compare = [1,2,3,4];
for n = 1:3
    area_compare = area_compare(area_compare ~= n);
    line1_int_x = intersection_x(n,:);
    line1_int_y = intersection_y(n,:);

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

c) For matrix A, there are less rows than columns, hence there are fewer equations than unkowns. A non-trival solution exists. 

## Problem 5: Image Overlay

a) The code to overlay an image is as follows.  

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

![](https://lh3.googleusercontent.com/SV0ov4ER6Pw9C0ZX5Uz66PBZjKakME15hG7GTAdVYY4-S7ApvpXOH-SAgTFIHRN1E35x5K_U5n3GqGVJn4t8cYoKK9WLIX1dz8serO-m9q9b4C4SwW51OnxZwgolvdnBe-om12wpVO6MubDMyIV00OIVPHxhm07rB0FaScLHqpIyykTivmWDH5Y_JdtUOGOBKyf3juxYZICCAVDIhZYn-ru-wTOdEKr2_uw94lR4kwy8v5Miib0HSDa5tUSWQDmu_rVWbAQkkS_MjRYr2luGKQpJ3siIIDCojOvvRSsF3rDHDKj9ZtuEgtlhJwp88j0XcfeNFvmNRzmivj9-lO6E0IzrvLK1Qnm9xfuMiB959GXHiG12ZQ7eoMoJU9M9A7JY1HVSG40sdAz-jk_lmGVdAbiOZZvMwLZY5Cq_9lSxqygVFMOI8SvBqIkSHCh9bH1613sCeSOMPiaCKYJ_yd3RtfcDnkKFWalSMYHshITTojZDb35ohHCtq64TMfw2HfXlEnluqoDaYo9POSrRYd9Z_yJQo93WDjGyPm2vD8BCf8Bc3gbofFsH_8m_lG24qjbgCAPRFQf16fxJ6zizCWmeJ5AcOXUuBITBZ91knAlH7miTuBwgXNzOSwLE1mqbYaeb2YUtkEVWQsYQM0qOjtYB5ZWPB3IYJrRivpvX7j4eN08tNkGkCHufMQ=w881-h625-no)  

b) The code to overlay the image is as follows.  

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
![](https://lh3.googleusercontent.com/aHHsTEh5WWc6dNnAP84q-4AE1oX4pPIY6iAJlXqz4Zz6kNn2PhSMw8ylV4UpzWLMCAnZeNwmslBHbu7Liuf94te4CtOmMFo8gptoW5fYCNVzCHz7gQ4mdq4tX4DgT0B2SmZQIVCztpFR9TGUgTS-GMC3j7sY71N7SbqFUOhUEgaCHU7fY--Q6fvDJKLK2u_XGm3-iJVpHcm73wTFM_7Cqmgq1vpBB3LKb79q0GYzHNceaO0JvyfeICH-2FawqpCy4_ZufisYElux8d7Paz0zjKhCIalCjEhsfagYdxcIzFhGt7jtW2xNnyHlWWZkzaygyw1bl0anCpIEZLCoRIRYolwDjlajcn7C0uKQsyhdwaHjom-nVS8dlbVX6JsRfTK1qYeJrfKKLeenKyFBYOaWXRgn2sRtAJvWVQ7_YULEF9JbBLAUJ7TS2hAYqgG5uX44pjy3MEl51cOcBtKT0hbkGZzIyTm1HQ0NVcTc6AwPnGhtXkIaQSSwgxSUaCLbaBr1TKtnd5TDSAJl0iD8PUsWmk6tU4fIfWfyOm7S895usSzEn3t1nBkCX_quM3K8joumNOuWftfRixj842ZXeQmbavB46_8zXjs1H_F364mnI-51zjnXLbCzFnxYebOeOTW05SIDf1vLIem6xPHAYFc8e7g8H372cDD0ceyndVQxh-1OetYPwakXQw=w872-h603-no)  