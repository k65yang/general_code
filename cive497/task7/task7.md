# Task7: Image Stitching & RANSAC

**Name:** Kai Yang  
**ID:** 20460696  
**Degree:** BA  

## Problem 1: LoG and DoG (10 points)

a) The Laplacian of the Gaussian (LoG) is the second derivative of the gaussian function. The LoG filter is commonly used in edge detection. Being the second derivative, it can detect changes in color/intensity of the image. Also being a gaussian, it has an image blurring effect as well. When the colour of the image does not change, its derivative and second derivative will be 0. For these areas, the LoG filter will have no effect. When the LoG filter is convoluded over an edge (an area of change in color), its response will be a sudden increase in values as a change in color indicates that the derivative will be non-zero. Measurement of the sudden increase indicates an edge. A change from a darker colour to lighter colour will be negative and vice versa. 

The LoG filter is also commonly called as a blob filter. A bolb filter is one that is used to detect regions within an image that has different properties, as compared to the surrounding regions. The LoG filter is shown below. Note the value in the centre compared to the rest of the values in the matrix. This filter can accentuate certain features of the image, provided that the "blob" of the filter is around the same size of the feature in question. Furthermore, to identify features of different size, the size of the LoG kernel would simplily be made bigger or smaller (or more efficiently, the size of the image would be scaled up or down).

b) Application of a gaussian filter will blur an image. The difference of the gaussian (DoG) is the subtraction of one image blurred with a specific sigma against another blurred image with a specific sigma. Since a gaussian filter suppresses frequences above a certain range, subtraction of two images convoluded with gaussian filters preserves only the frequency ranges that lie in-between the range of frequences orginally preserved in the blurred images. 

A DoG filter can be used as an approximation of an LoG filter. It is especially useful in blob detection. Images filtered with different sigmas may be subtracted against one another to detect edges that appear at various images scales or degrees of focus. In other words, DoG algorithms may be implemented such that blobs of various sizes may be detected. 

## Problem 2: Least Squares (20 points)

a) Approach 1 and 2 are essentially the same; both methods seek to minimize the sum of the squared residuals (errors). Approach 1 is written in terms of summations, whereas approach 2 is written in terms of matrices. Note the defnition of error for approach 1 as the following.  

![](https://latex.codecogs.com/gif.latex?E%20%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20%28y_%7Bi%7D%20-%20mx_%7Bi%7D%20-%20b_%7Bi%7D%29)  

The error term in approach 2 is defined as follows.  


The subsitution of the Y, X, and B matrices into the expression results in an expression equivalent to that of approach 2. The next steps would be taking the partial derivatives of the error with respect to the variables. For approach 1, the partial derivatives with respect to b and m would be taken and for approach 2, the partial derivative with respect to B would be taken. Afterwards, it is just a matter of mathematical manipulation to solve for m and b or B.  

b) and c) Both approaches resulted in the same answer of m = 3.6540 and b = 3.3197.  

```matlab
%% Load data
load prob2_data1.mat

%% Approach 1
n = length(x);

m = (sum(x.*y)- 1/n*sum(x)*sum(y))/(sum(x.^2) - 1/n*sum(x)^2)
b = (1/n*sum(y)*sum(x.^2)-1/n*sum(x)*sum(x.*y))/(sum(x.^2)-1/n*sum(x)^2)

%% Approach 2

X = cat(2, x', ones(n,1));
B = inv(X'*X)*X'*y'
```

d) Approach 1 was used. m = 3.3348 and b = 2.6458.  

e) RANSAC approach with a threshold of 0.35 and 5000 iterations yielded m = 3.3331 and b = 2.6053.  

```matlab
%% Load Data
load prob2_data2.mat

%% Approach 1

n = length(x);

m = (sum(x.*y)- 1/n*sum(x)*sum(y))/(sum(x.^2) - 1/n*sum(x)^2)
b = (1/n*sum(y)*sum(x.^2)-1/n*sum(x)*sum(x.*y))/(sum(x.^2)-1/n*sum(x)^2)

x_ = [min(x), max(x)];
y_ = m*x_+b;
figure();
plot(x,y); hold on
plot(x_, y_, 'r-')

%% RANSAC

[m_ran, b_ran] = ransac_2Dline(x,y,5000,0.35,0.5) % x data, y data, interations, thereshold, inlier ratio

function [m_ran, b_ran] = ransac_2Dline(x,y,iter,threshold, ratio)
% implementation of RANSAC for a 2D line

numPoints = length(x); % number of total points
numInliers = 0; % number of inliers
m_ran = 0; b_ran = 0; % output parameters

for ii = 1:iter
   %% select 2 random points
   p_temp = randperm(numPoints, 2);
   x_ = x(p_temp);
   y_ = y(p_temp);
   
   %% Compute the distance of all points to the line defined by the two points
   % See https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
   d = abs((y_(2)-y_(1)).*x - (x_(2)-x_(1)).*y + x_(2)*y_(1) - y_(2)*x_(1))/ ...
       sqrt((y_(2)-y_(1))^2 + (x_(2)-x_(1))^2);
   
   %% Compute number of inliers within the threshold range
   numInliers_temp = length(find(abs(d) <= threshold)); % temp store number of inliers
   
   %% Determine if this current model is the best model. Update if true
   if numInliers_temp > numInliers && numInliers_temp >= round(ratio*numPoints)
       numInliers = numInliers_temp;
       p = polyfit(x_, y_, 1);
       m_ran = p(1); b_ran = p(2);
   end

end
figure();
plot(x,y); hold on;
xx = [min(x) max(x)];
yy = m_ran*xx + b_ran;
plot(xx, yy, 'r--')
end
```

f) Least squares takes into account all the data points and approximates a line of best fit. An advantage of least squares approximation is that the math behind it is very general, hence can be applied quickly and without using a lot of computational effort. A disadvantage is that the outliers will skew the best fit line and in some instances, give an obvious erronous line. As such, least squares should be used as a "quick and dirty" way to determine general trends. Some applications do not require absolute accuracy, making least squares a perfect option.  

An advantage of RANSAC is that it will determine the general trend of the inliers without any influence from the outliers. A disadvantage of RANSAC is its lack of robustness. It requires the user to define the fitting function, the number of points to test, the threshold, and how many iterations it needs to do. Additionally, because of its iterative process, the line of best fit may be different depending on what parameters you choose. RANSAC should be used when there is an obvious trend visible but the data has high scatter or a large number of outliers that make using least squares infeasable.  

## Problem 3: Fitting using RANSAC (30 points)  

a) The parameters of the conic determined through RANSAC is as follows, a = 0.1104, b = -0.0053, c = .3044, d = 0.2497, e = 0.8732, and f = 0.2652. As mentioned during the lectures, the data only had noise in the y-direction. So, I assumed that the x value is the correct value and only varied y during my analysis.  

```matlab
%% Load parameters
load prob3_ellipse.mat

iter = 1000; % number of iterations
threshold = 1; % threshold of inliers
ratio = 0.5; % inlier ratio
numPoints = length(x); % number of total points
numInliers = 0; % number of inliers
a_ran = 0; b_ran = 0; c_ran = 0; d_ran = 0; e_ran = 0; f_ran = 0; % output parameters

%% Iterate for solution
for ii = 1:iter
   %% Select 5 random points
   p_temp = randperm(numPoints, 5);
   x_ = x(p_temp)';
   y_ = y(p_temp)';
   
   %% Determine the parameters of the conic
   M = [x_.^2, x_.*y_, y_.^2, x_, y_, ones(size(x_))];
   MM = null(M);
   a = MM(1); b = MM(2); c = MM(3); d = MM(4); e = MM(5); f = MM(6);
   
   %% Compute distance of points to the conic
   % As per lectures, the noise is only implemented in the y-direction, so
   % rearrange equation of conic to solve for y
   dd = sparse(numPoints, 1); %array to store distances
   for iii = 1:numPoints
      coeff = [c, b*x(iii)+e, a*x(iii)^2+d*x(iii)+f]; % coefficients of a quadratic equation
      r = roots(coeff);
      r = real(r); % remove imaginary numbers
      d_temp = abs(y(iii) - r);
      dd(iii) = min(d_temp); % y distance to the line is assumed to be the lesser of the two numbers
   end
   
   %% Compute number of inliers within the threshold range
   numInliers_temp = length(find(abs(dd) <= threshold)); % temp store number of inliers
   
   %% Determine if this current model is the best model. Update if true
   if numInliers_temp > numInliers && numInliers_temp >= round(ratio*numPoints)
       numInliers = numInliers_temp;
       a_ran = a; b_ran = b; c_ran = c; d_ran = d; e_ran = e; f_ran = f;
   end
end

conic = @(xx,yy) a_ran*xx^2 + b_ran*xx*yy + c_ran*yy^2 + d_ran*xx + e_ran*yy + f_ran;
plot(x,y, "bo"); hold on
fimplicit(conic, 'r-')
```
b) The fourth degree polynomial was fit using RANSAC. 100 iterations was specified with a threshold of 7. The polynomial equation is as follows.  

![](https://latex.codecogs.com/gif.latex?f%28x%29%20%3D%201.0541x%5E4%20-0.7259x%5E3-9.5369x%5E2&plus;2.4272x&plus;13.7417)  

```matlab
%% Load parameters
load prob3_polynomial.mat

iter = 10; % number of iterations
threshold = 7; % threshold of inliers
ratio = 0.5; % inlier ratio
numPoints = length(x); % number of total points
numInliers = 0; % number of inliers
a_ran = 0; b_ran = 0; c_ran = 0; d_ran = 0; e_ran = 0; %ax^4 + bx^3 + cx^2 + dx + e = 0

%% Iterate for solution
for ii = 1:iter
   %% Select 5 random points
   p_temp = randperm(numPoints, 5);
   x_ = x(p_temp);
   y_ = y(p_temp);
   
   %% Fit the 5 points using polyfit
   M = polyfit(x_, y_, 4);
   a = M(1); b = M(2); c = M(3); d = M(4); e = M(5);
   
   %% Compute distance of points to the polynomial line
   % To calculate the perpendicular distance from the line to the point is
   % too computationally complex. The distance was approximated by
   % computing the x and y distances to the line and taking the lesser of
   % the two
   dd_x = sparse(1, numPoints); %array to store x distances
   dd_y = sparse(1, numPoints); %array to store y distances
   for iii = 1:numPoints
      coeff = [a,b,c,d,e]; % coefficients of a quartic equation
      r = roots(coeff); % zeros (x-values) of the polynomial expression 
      r = real(r); % remove imaginary numbers
      d_temp = abs(x(iii)- r);
      dd_x(iii) = min(d_temp); % y distance to the line is assumed to be the lesser of the four numbers
      
      yy = a*r.^4 + b*r.^3 + c*r.^2 + d*r + e; % compute the y-values 
      d_temp = abs(y(iii) - yy);
      dd_y(iii) = min(d_temp);
   end
   
   % Hurons formula to determine the area of triangle
   dd_c = sqrt(dd_x.^2 + dd_y.^2);
   dd_p = (dd_x + dd_y + dd_c)/2;
   dd_A = sqrt(dd_p.*(dd_p-dd_x).*(dd_p-dd_y).*(dd_p-dd_c));
   
   % Distance from the point to the line approximated
   dd = 2*dd_A./dd_c;
   
   %% Compute number of inliers within the threshold range
   %dd = min(cat(1,dd_x,dd_y)); % normalize length differences
   numInliers_temp = length(find(abs(dd) <= threshold)); % temp store number of inliers
   
   %% Determine if this current model is the best model. Update if true
   if numInliers_temp > numInliers && numInliers_temp >= round(ratio*numPoints)
       numInliers = numInliers_temp;
       a_ran = a; b_ran = b; c_ran = c; d_ran = d; e_ran = e;
   end
end

figure();
f = @(x) a_ran*x.^4 + b_ran*x.^3 + c_ran*x.^2 + d_ran*x + e_ran;
plot(x,y, "bo"); hold on
plot(x, f(x), 'r--')
```

c) The 3D plane equation determine through 1000 iterations with a threshold of 0.1 is as follows.  

![](https://latex.codecogs.com/gif.latex?0.1831x%20&plus;%200.5475y%20&plus;%200.3649z%20&plus;%200.7305%20%3D%200)  

```matlab
%% Load parameters
load prob3_plane.mat

iter = 1000; % number of iterations
threshold = 0.1; % threshold of inliers
ratio = 0.5; % inlier ratio
numPoints = length(x); % number of total points
numInliers = 0; % number of inliers
a_ran = 0; b_ran = 0; c_ran = 0; d_ran = 0; %ax + by + cz + d = 0

%% Iterate for solution
for ii = 1:iter
   %% Select 3 random points
   p_temp1 = randperm(numPoints, 3);
   p_temp2 = randperm(numPoints, 3);
   x_ = x(p_temp1, p_temp2);
   y_ = y(p_temp1, p_temp2);
   z_ = z(p_temp1, p_temp2);
   
   %% Fit the 3 points to a plane
   M = [diag(x_) diag(y_) diag(z_) ones(3,1)];
   MM = null(M);
   a = MM(1); b = MM(2); c = MM(3); d = MM(4);
   
   %% Compute distance of points to the surface
   % see https://mathinsight.org/distance_point_plane
   dd = abs(a.*x + b.*y + c.*z + d)/sqrt(a^2+b^2+c^2);
   
   %% Compute number of inliers within the threshold range
   numInliers_temp = length(find(abs(dd) <= threshold)); % temp store number of inliers
   
   %% Determine if this current model is the best model. Update if true
   if numInliers_temp > numInliers && numInliers_temp >= round(ratio*numPoints)
       numInliers = numInliers_temp;
       a_ran = a; b_ran = b; c_ran = c; d_ran = d;
   end
end

figure();
mesh(x,y,z); hold on
[xx yy] = meshgrid(-4:0.1:4);
zz = -1/c*(a*xx + b*yy + d);
surf(xx,yy,zz)
```
## Problem 4: Improved 3D Planar Measurement Tool (30 points)

a) The results of the improved planar measurement tool is shown in the following figures. The all distances are in mm. The measured line should be 150 mm. The blue polygon is the area bounded by the homography matrix. As can be seen, the accuracy of the results of the measurements of tool is acceptable.  

```matlab
%% Load parameters
imgCover = imread('cover.jpg');
imgTest = imread('IMG_0092.jpg'); %change this manually for every image
coverImgSize = [240 315]; %units in mm
[imgCoverHeight, imgCoverWidth, C] = size(imgCover);

%% Sift Image
Ia = single(rgb2gray(imgCover));
Ib = single(rgb2gray(imgTest));

peak_thresh = 2.5;
[fa,da] = vl_sift(Ia, 'PeakThresh', peak_thresh);
[fb,db] = vl_sift(Ib, 'PeakThresh', peak_thresh);

%% Feature match
[matches, scores] = vl_ubcmatch(da, db, 2.5); %threshold value of 4

% extract all the matches for future homography calculations
img1Points = [fa([1,2], matches(1,:)); ones(1,length(scores))]; 
img2Points = [fb([1,2], matches(2,:)); ones(1,length(scores))];


%% RANSAC Loop to estimate homography
iter = 5000; % number of iterations
threshold = 2; % threshold of inliers
ratio = 0.5; % inlier ratio
numPoints = length(matches); % number of total points
numInliers = 0; % number of inliers
H_ransac = sparse(3,3);

for ii = 1:iter % iterate for solution
    sel = randperm(numPoints, 4); % 4 random points
    img1Fe = fa([1,2], matches(1,sel));
    img2Fe = fb([1,2], matches(2,sel));
    
    [img1Fe, img2Fe] = pointSort_p4(img1Fe, img2Fe); % sort in circular manner
    
    H = computeH_p4(img2Fe, img1Fe); % compute homography of the 4 random points
    
    coverH = sparse(2,numPoints);
    for iii = 1:length(coverH)
        tempCoverH = H * img2Points(:,iii); %p*H
        coverH(1,iii) = tempCoverH(1)/tempCoverH(3); % x value on cover image estimated by homography
        coverH(2,iii) = tempCoverH(2)/tempCoverH(3); % y value "    "
    end
    
    % compute SSD
    dx = coverH(1,:)-img1Points(1,:);
    dy = coverH(2,:)-img1Points(2,:);
    inlier_temp = sum(dx.^2 + dy.^2 <= threshold.^2);
    
    % determine if homography is good
    if inlier_temp > numInliers
       numInliers = inlier_temp;
       H_ransac = H;
    end
end

% show points on cover image, FOR DIAGNOISTIC PURPOSES ONLY
a = [1:4]'; b = num2str(a); c = cellstr(b);
figure(); imshow(imgCover); hold on
plot(img1Fe(1,:), img1Fe(2,:), 'bo')
text(img1Fe(1,:)+0.1, img1Fe(2,:)+0.1, c);

figure(); imshow(imgCover); hold on
plot(polyshape(img1Fe(1,:), img1Fe(2,:)));

% show points on test image, FOR DIAGNOISTIC PURPOSES ONLY
figure(); imshow(imgTest); hold on
plot(img2Fe(1,:), img2Fe(2,:), 'bo')
text(img2Fe(1,:)+0.1, img2Fe(2,:)+0.1, c);

%% Compute measurement as defined by user input
figure(); imshow(imgTest);
drawline1 = drawline('LineWidth', 0.5, 'Color', 'red');
lineCoor = drawline1.Position;

figure(); imshow(imgTest); hold on
plot(lineCoor(:,1), lineCoor(:,2))

L = computeL_p4(lineCoor, H_ransac);
L = L*coverImgSize(1)/imgCoverWidth;

%% Show the test iamge, the region used for homography, and the computed length
figure(); imshow(imgTest); hold on
plot(polyshape(img2Fe(1,:), img2Fe(2,:)));
plot(lineCoor(:,1), lineCoor(:,2), 'r-', 'lineWidth', 0.5)
text((lineCoor(1,1)+lineCoor(2,1))/2, ...
    (lineCoor(1,2)+lineCoor(2,2))/2, num2str(L), 'Color', 'b', 'FontSize',14)

function H = computeH_p4(imgOrig, imgProj)
% Computes a homography matrix

% define coordinates for original image 
x1 = imgOrig(1,1); y1 = imgOrig(2,1);
x2 = imgOrig(1,2); y2 = imgOrig(2,2);
x3 = imgOrig(1,3); y3 = imgOrig(2,3);
x4 = imgOrig(1,4); y4 = imgOrig(2,4);

% define coordinates for projection area
x1_ = imgProj(1,1); y1_ = imgProj(2,1);
x2_ = imgProj(1,2); y2_ = imgProj(2,2);
x3_ = imgProj(1,3); y3_ = imgProj(2,3);
x4_ = imgProj(1,4); y4_ = imgProj(2,4);

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
H = reshape(H,3,3)';
end

function L = computeL_p4(lineCoor, H)
% Computes the length of line

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

function [points1_sorted,points2_sorted] = pointSort(points1, points2)
% sorts points in a circular manner to prevent overlap of homography matrix

c = mean(points1,2); % mean/ central point 
d = points1-c ; % vectors connecting the central point and the given points 
th = atan2(d(2,:),d(1,:)); % angle above x axis
[th, idx] = sort(th);   % sorting the angles 
points1_sorted = points1(:,idx); % sorting the given points

points2_sorted = points2(:,idx);
end

```

b)  

c) The measurements are comparible. Obviously, both tools will not be able to accurately measure the length with no error, but the results are very close.  

## Problem 5: Book Classification using SIFT (30 points)
The results of the book classification is shown as follows.  

```matlab
%% Load parameters
coverImgFolder = 'Covers'; % cover folder
testImgFolder = 'TestImage'; % test image folder
dirOut = 'out'; % output image folder
coverImgList = dir('Covers/*.jpg'); 
testImgList = dir('TestImage/*.jpg');
nCoverImg = numel(coverImgList);
nTestImg = numel(testImgList);

polyTestCoverx = zeros(4,4,nTestImg); % matrix to store the coor of all corners in the images
polyTestCovery = zeros(4,4,nTestImg);

%% Begin looping through all test images
for ii = 1:nTestImg
    imgTest = imread(fullfile(testImgFolder, testImgList(ii).name));
    
    %% SIFT the test image
    imgTestSIFT = single(rgb2gray(imgTest));
    peak_thresh = 2.5;
    [fa,da] = vl_sift(imgTestSIFT, 'PeakThresh', peak_thresh);
    
    %% Loop through cover images
    for iii = 1:nCoverImg
       imgCover = imread(fullfile(coverImgFolder, coverImgList(iii).name));
       [imgCoverHeight, imgCoverWidth, C] = size(imgCover);
       
       %% SIFT the cover image
       imgCoverSIFT = single(rgb2gray(imgCover));
       [fb, db] = vl_sift(imgCoverSIFT, 'PeakThresh', peak_thresh);
       
       %% Feature matching
       [matches, scores] = vl_ubcmatch(da, db, 2.5); %threshold value of 2.5

       % extract all the matches for future homography calculations
       imgTestPoints = [fa([1,2], matches(1,:)); ones(1,length(scores))]; 
       imgCoverPoints = [fb([1,2], matches(2,:)); ones(1,length(scores))];
       
       %% RANSAC to estimate the homography matrix
       iter = 1000; % number of iterations
       threshold = 5; % threshold of inliers
       ratio = 0.5; % inlier ratio
       numPoints = length(matches); % number of total points
       numInliers = 0; % number of inliers
       H_ransac = sparse(3,3);
       
       for iiii = 1:iter
           sel = randperm(numPoints, 4); % 4 random points
           imgTestFe = fa([1,2], matches(1,sel));
           imgCoverFe = fb([1,2], matches(2,sel));

           [imgTestFe, imgCoverFe] = pointSort_p5(imgTestFe, imgCoverFe); % sort in circular manner

           H = computeH_p5(imgCoverFe, imgTestFe); % compute homography of the 4 random points

           testH = sparse(2,numPoints);
           for iiiii = 1:length(testH)
               tempTestH = H * imgCoverPoints(:,iiiii); %H*p
               testH(1,iiiii) = tempTestH(1)/tempTestH(3); % x value on cover image estimated by homography
               testH(2,iiiii) = tempTestH(2)/tempTestH(3); % y value "    "
           end

           % compute SSD
           dx = testH(1,:)-imgTestPoints(1,:);
           dy = testH(2,:)-imgTestPoints(2,:);
           inlier_temp = sum(dx.^2 + dy.^2 <= threshold.^2);

           % determine if homography is good
           if inlier_temp > numInliers
              numInliers = inlier_temp;
              H_ransac = H;
           end
       end
       
       %% With the homography matrix, compute the corners of the book
       polyTestCoverx(iii, 1, ii) = homoToX(H_ransac, [0,0,1]'); % top left
       polyTestCovery(iii, 1, ii) = homoToY(H_ransac, [0,0,1]');
       
       polyTestCoverx(iii, 2, ii) = homoToX(H_ransac, [0,imgCoverHeight,1]'); % bottom left
       polyTestCovery(iii, 2, ii) = homoToY(H_ransac, [0,imgCoverHeight,1]');
       
       polyTestCoverx(iii, 3, ii) = homoToX(H_ransac, [imgCoverWidth,imgCoverHeight,1]'); % bottom right
       polyTestCovery(iii, 3, ii) = homoToY(H_ransac, [imgCoverWidth,imgCoverHeight,1]');
       
       polyTestCoverx(iii, 4, ii) = homoToX(H_ransac, [imgCoverWidth,0,1]'); % top right
       polyTestCovery(iii, 4, ii) = homoToY(H_ransac, [imgCoverWidth,0,1]');
    end
    
    figure(); imshow(imgTest); hold on
    for n = 1:4
       plot(polyshape(polyTestCoverx(n,:, ii), polyTestCovery(n,:, ii))); 
    end
end

function H = computeH_p4(imgOrig, imgProj)
% Computes a homography matrix

% define coordinates for original image 
x1 = imgOrig(1,1); y1 = imgOrig(2,1);
x2 = imgOrig(1,2); y2 = imgOrig(2,2);
x3 = imgOrig(1,3); y3 = imgOrig(2,3);
x4 = imgOrig(1,4); y4 = imgOrig(2,4);

% define coordinates for projection area
x1_ = imgProj(1,1); y1_ = imgProj(2,1);
x2_ = imgProj(1,2); y2_ = imgProj(2,2);
x3_ = imgProj(1,3); y3_ = imgProj(2,3);
x4_ = imgProj(1,4); y4_ = imgProj(2,4);

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
H = reshape(H,3,3)';
end

function [points1_sorted,points2_sorted] = pointSort(points1, points2)
% sorts points in a circular manner to prevent overlap of homography matrix

c = mean(points1,2); % mean/ central point 
d = points1-c ; % vectors connecting the central point and the given points 
th = atan2(d(2,:),d(1,:)); % angle above x axis
[th, idx] = sort(th);   % sorting the angles 
points1_sorted = points1(:,idx); % sorting the given points
%points1_sorted = [points1_sorted points1(:,1)]; % add the first at the end to close the polygon 

points2_sorted = points2(:,idx);
%points2_sorted = [points2_sorted points2(:,1)];
end

function x_ = homoToX(H, p)
% Multiplies homogenous coordianes to the point, then returns x coor

p_ = H * p;
x_ = p_(1)/p_(3);
end

function y_ = homoToY(H, p)
% Multiplies homogenous coordianes to the point, then returns x coor

p_ = H * p;
y_ = p_(2)/p_(3);
end
```
