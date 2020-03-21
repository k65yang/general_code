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

