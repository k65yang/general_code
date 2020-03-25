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

![](https://lh3.googleusercontent.com/D_sjCardn_RR_dOxfIqJlVW_kMIYZVpx7e8GdFJzDWI7tkE-SAVgqmqoxsiulm09dlly-BaYVqYwYea6VOBg7RPza4uSv8ajT_aMtlGGCLn_b6pg9MkcKauSGjt0uvoVfJmxlrQWyMO7l1WH79_zAsTbsRmb23o9F7IjEKn_KrdRBd1JKy2vuDEyVTkjdhOyQ6_m1ACQpiAxcGgz6pF3M2jzewP78epELIBzftbPSjCgPjHM0wLACKRuUFU4n5NfZ509bOG_-5FvoPxvRmEw_suldsulHDor8fW2-fgGV7WSj_Qa1IoKeFteaeONb1D_RBaoNhGcyW45MvVDCHleV_E-kqbbnP32Z-XnTB9a6xFylr51RTvT7y1JdlpxTn8hH5t-a1QSjkoHI4jKQgtsKowXbnqAfk7DRzR6wqCofOJFDnEUDWC-UqU6mYAUctmjD1TXMvMzR3vPFOQkKyT2JqVm9GrxhvbaniE1KG2Nw8Cau2pGSh93yvZVNMrhhrVzLeuhFI5cAONscEh4UVqKlH64V1dOP4Ol24fsArS_ZB4HXAFF3xHmNRfNUcY56K8SWkcd7WZoRvmd9Qmost59Hmoi49jFxo2D7H_P_pQ8JVOdbdTFTL36bY2QhX-kKVmzd2kTEDuv5yuIF2hNA91MSaPtP6i-Aus1mKmgL4bvmX46NOVVdqyA32qOcSZv=w699-h140-no)  

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

![](https://lh3.googleusercontent.com/2xeyIa5fE_1DksWCVlSV2CmQhoYaqT3Ukdpp1AsKCpyamQiBGPO7sqCImkvxLmHd_S3YbFbjaTKMqiYusmcPgxKLC1xBDlxz1vo8npDxuRzAHlwXpiijFZHCU2my0cz-s5J988YgFkTpbmi0cMT9_hhqp-57HOoE3diAUqw02JUFQ-g2XEQ0zpdfynKZq-ki8obYcdFjCJDEeAWt1ZBRgyFGXe99nG1iHk826ByKCyTxbpICXuY2TrGmdiTA8FKqjIFJnGhgbfiADfSmOwZ5jt9uzwgDcH-WZtCU7Ob0c0iXBmDfutI9UA49CBRwE8Tk9rDBAqFNJVlovpeE0SAETznm2w83aoTeEIuY1Uh1CdF8BKLQK22PdyMGuLiyz6TgmfIEZGP6a8kfiHw1-gUghXgc5WxjG-lKwGprLOVCbTvB1-JhF9YjHQoqdpRXNAB2FRwXgMEJsbH_bYkWqgEE1CecApCBvtRhNUL2_O8lh6w7CMensZ0wJRxT68dTnvpvEhEbKJNGOc4UPwvSbwjglMorOQgEkoLkfV2I1Dt1odT_Pp4Ns-aTixpzQVWqJW3eXbL1kt9ofsjkab_EyO0GqKTDrDInZbXUAZDDH_MeOfpBNkNct67vtQu8XdIz0YgSxXW1qUGTM702mIEvmluSrBu6kPY2-kc9MJ3cp5Cw7GEbq2zcipZznX-RbiDy=w560-h420-no)  

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

![](https://lh3.googleusercontent.com/hBtPCXIpPLR7Ej3h3RnAy8zIlQmW7ZXZ30Hq_7AEcn-DItsoU1tyQJwXy9as1a7Wzn3s_Gfy3bF86oDJntsoC2ZSzJrr89Dd7wA6EFmuxXVlCzcWzGgLarUdapy0o5fM0kGV9GrNUDajEDgYcHPO3DSs29CI50ZQghWMfIY9r-00tjZeoA3BKnjsMXl-qXOuSJ6bcIn4fiBB47GlxAzq0n2-Qt2CvYO7kfrfoB9mWE9M_KPi3uID38Ts8MNs31Y9e8ncWZn2MBi_t1Sw6rbhGj1geLxjs8AiKLa8xGF1R5ioTdQdP0-itNreoq88QooRtPGJzqysjkwpy1ZzoSvfnoPa6at-ScaJA9uLjkta15JmTwbewRnERAGbEW3Cflsi78hx2HhVL5SKH3MgqCC-9yuNxJTCHEVDkaNQvhZiR5RNadIA7m0khRAU9ZCZJ1B3NONsDkyG3shlTVU1m2w2eluzUT2h5nsbqEhLsFgF3FWMOmr3mQtqZVTMB6FMynGCmNA9e6ioNf_QkAaJTUyBZOdVhDg3nrNvyvf45uf96Sbfiz6PfcwFfZfl2bKG3EHtJ0CyqqxZlUaiPCHYCaRPNqXSztDuzL0oyTAMKnKcbLrpGCYPQ-yXagifTUWMn-nJ_Ck3PWV0xAPZJ2AWB1Qy35zX1gvz6Ew4D4ehPWdpMzJHXNrSEhTiSeCbPKVs=w560-h420-no)  

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

![](https://lh3.googleusercontent.com/W0eD95k1CCzsCCQY1y7atJzz1lYudgdGywadm8e-Z_LZUExWJGXG2SxOVEMsiGlqZeTEEDd_YW_jlhUiBaI90BEdAm5CHQO5wDo829HlxutxW6YqnoIf7hE0UtlV2p3aS4TFslpAAqAV-xOcEHUUpizloFb-AqkVOgNQJ3q4RBguYKqGSAhx70uZB10sX2L_No8ta1lCKSIR4n4_ORJCnFGjUjTY2ilUQL_fGm7Cd2y_IDMe3I6zYlyP7WzPF_uNdcO2zOd2B-21UjrDsNvgK2j47iFBTRQCbPfT5xy8va3nLuvKzy8ucekS8JQnSHjju1EZdX99eNSdvMwAQPRHqo8BENE7GtBP-YaM8UVb2LfYsg9fInhoSx7WSkFmkT4FGdbPkK6URUy9VNc7UMJHhaZHD2akBiVKbHQ5nexHx9GZfLhE46aEl75rUrXaRxMkdKUGQD7mCHbmzvngDefPTJ9ebjlnJLLEKesbvY9cTis3ITJYL61353lrfswHbAMqw0D07phALqrSRmSgm_Kv_j1M3yV85Ht0OUhVJs4haZm6iF8PrA6Z8C9HE-RGgVrsxPA067mj_-ef4oJDbJmluJ3AEW9ZYA6EDdjrJMwfJCtPfVMvk04hB0lvp2KA7ydpE-Ru_Ild0ftFwW-oS_YaL8w6KRLHzL6JmZn_o4JMrHuwM01dQ-Nexr9ZA29m=w560-h420-no)  

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

![](https://lh3.googleusercontent.com/kvLZMVmrc2A9AEaDWQfUzUtfsY7-pvfGCtt3aRZ5YHB-c39jaoR9tdGyodUbcsNRO4ATX1I58RQ6ukDowm2tE3UtcSul9jvXpaMs65Hu7ykipB-dbdz5zuoABfJQrNWClcZtCEq0KeNThm_Z3sPWJJ1fiCLiZAVITeolCCpmuWWk1pDRu0FghtN8nylED8UFCtuVCG4NIJy6lBqa1s0oyPbCmd_MmEN-9-FWLfcSFbdEbwLcY2c6uVNXXrXq__ZpKy81HyYxwf4_xm03B8jKauMw4BQGPcF8bphtXH-vD76c4A3m86XqtE5Y1-TFMIobEIqXlQhBg5CxOWKIO_ACtM-pr-ay2vI5znx71IQ6vqb3aPy-pR_lMNJyJrUxkzONMS1Z7t0mVTpggCYpVBwYdYCZ3NNOL9OBkP25kN69iAjF9r0R1KacSPdmAiJVorP1GfKoew-c49wxRdbePnPFyVU0HdABwMUTKaHXrRHdyCWFJ2sCyWzxV2SJkCWj5VU2cQ7GjJ73fEo_yvuuALEnMvLoMZNtHcp-TVkHD9BwejBXmHaCkpirDKqAWPmoDxEPTKVZDFhEc7sHNbIynxuDRNef2wpicCNSexq1mDSAMcKJAsGK3b7uMLVQnetiCNw6usQ7pZvxx4s5UR0RRQ0SnjvzvUBkJGC203Bo7aHgivoey62LsnteTW3RmzdA=w560-h420-no)  

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

![](https://lh3.googleusercontent.com/htVc6A-tQLZCSpQMMPhHSdh7qCgdyzHnXTAGB5zKS5zNYDK-AayTTeIj0XrACm7xbcLHgRh6-N2-QwMU_zCKRTm3EMeZmel3HfK3JEWMRV9FRfe7BlCFuNAVGCoF5zU30oCzQH5taj8ekxYwIESWKlg3oenMf02TuAKfOhx1UoYOvBX0hvWDk5NsHnlrPbX2VjT5vKUtcnLMLI-5QfyKutF862AurNigeYC5KpWgXNSbEf8F3B4Dh_M-8ty_WLnuuj-v6o66DdYRfsOrLNsiEZidpDOmK7nEZBZDSUymziGgFX3OsC1sF_5-5TVhw7K5TciYv_ouYX7JRCYLOj_oieKbpYUgTWnN49wvQ3hAq0jjzaItYktLCVkfUWr0hjU-EiSCUx1qH9FEA4aM2cvLB2LJwxx-xzUbFsl-cJ3y5SJRfqKAThTJyINB8Q2UZ4iDsBBnh8h4gzaBziLn8BzSkxAEFf6Bj4sWbIqpllPYMAvh4ZzP8TW_ftHdRlbjHaW8AqPt5d8Ar8z_kfL-CY6OEWebjrcgUkdOTNgyy0ik5GC7n6cP-YD6TfEAsAgmCzUYZrf4XLiZ-QiqdQDH6tSoXVxGLg8_JUTkUidXeaokqwLWwgGIeGa8F7a3Dxq1ZAes3uQ3WKW5LY7RW3tuZ0NgmLaAlsgaD5WAmtW0yd4ZUEF5FHEdGLV0hNP37b-z=w972-h625-no)  

![](https://lh3.googleusercontent.com/Ofnamh-ilPEyRHojV_Gz6qH-MXvznHL_nSbyJscZvErYKFO3ZkvHvrnfxGp4tAyzDct4W4J9Co0kbTP9OyY5vbkrBwLbjJtanA2sKwclG1GQIHB6IXpC3L1tHsYYDP8kjCWIcAROpSFvXhptuCjtX5yjLQFRMrxSUDU7IREu3bzjxP73E0wzwfSK6TWHy5NrfJskx0AJ4UOZmWrHsfU8GPDk-D824z587DQIVS5fS6To6NLJK5GyqeCBMf0hInJDDtmo14WBCyyqckv-mjLF0gc0QpDzbK6u0kQ25IKKfP0KyV4eGTQEtmHqyKuLxRIneFIN4h_IUUzv3cDUgOFifjSbBbkZbQsjzRDh8HQV3kIVsm5WPvveSPu2IeSA3DWcVTdiyypzu-6Qi2zOCP1jVh4UCf9fNwy3ttMUr15DlUC95c4q9N2WRF1NiJ-Y5VTyk3jkU4jzz5piPnZE2kuitRov_KzzGXu7c74NMdeapi1YRupG-HVrLJKlV3TglJEnYLx0UPuUonQjjbAQF5vHXqTNaQ6hUxVzd3h8wzRGVY22oUPfg0u8uvIdMMPESnB8C6_doKKYDXSQlQIQqdOXqiiEm8E4EKyv80IGXpB4t3Y6XVZiBnYZYY_5c_cVqn-vTQiZ1SVkS7dkJHQdfwXqlm9iiHyn_3rq4YMxGXSkj3WaATiWs_aB0hg90HfD=w972-h625-no)  

![](https://lh3.googleusercontent.com/EBq9bIb_R57jhew8P0nYzPX0jpRKb_zMom8Uea_BV02g78yN92eegEAFBp5XqghWZwrLGYH3V-_1hzn2UGcguWtUZkNwMB1DfA9_k3vgL4eC-sLbbvAB4ICjKRFZxNweD0OdLpSsN167-hDly0Z-ry6qGCSOFKXGKfSF0trZq3Bbej49USi2HcJrtbD6T4n7tBzAmAkGiiK-5hEkMzmGa7-OC5c6MkucZaLdP-PxxOLUXPPoD1wWp96AnN9Ih835iW9N9m9CYea2vJjD8QJTskepajzHFBe4zO-jrlLvVCACsCXU30_GREaRYgQut2jKakyWhOOWu3RWgFilSIU_5sKQLS1qT7N43Pyz_rbYiUJS6c8MBhSycaDkOOm-xgeGk2W0i_-wjMtWx82Mck6-29zMsTIG8BmN3FP8c6HYg14d1EIyH_E4SJyJXUwZPlECG4PANXRTgBvfOfJy1wngEA8ISUIDizOavOasoWSzM7z-iKHgzUIndm8acPIDsOI_j0lmbJLxGjI_sTlX7Pwa1CzrivKgPGrtGP9OMK3mWeBCxXLT28cJpAC2Msfe-X84x4KwitU0F0SaAunpCFAYnrSzcBjM_J2BZunQme4Vw7OJrOhI-MTPOSKL8Sl9l50vv-EYCtzRFzHrg7h9UgjDEQ2T8GvNLkYRXKEt65W04HU1CUrrgZOAulOLRbPu=w972-h625-no)  

![](https://lh3.googleusercontent.com/WJh3r167OSaqS6kQqfGr76EBU8-Qb8KfgfinwFrtSAF-pw4O3GkojwilNJfMniJOxxM2GjOEfb-vo743_Y3-kA_ANSV41fYTs8CCNDEHJs36kqYbIWmfH424-RABxxpurZu5cQqKBVkSS7czFcAVR3FKx-cTQVkfzKCFeAX8dUazIXVAgL3mNEc5kgZ0vPh9aUuzdoyKP8pya4YCHK49RUDpwX9fOMQO9rgxQDfh8Bgwy57CUpxn7M90sAMEIvFl1gOu16_WjXHU5rTaIrPZlaikZLPUGFNQ7HjXOkF8d7JM6RQZ6Tgwsqczx_su1eHmfGiNGMZqOC4vcv98SyPheY2R54HM8_vlXjwhPUt7WvUEGRVXlcqOxuuM0J0EOwjN2RNANJrn_BwItj2w6Sc9xmNHNgseIbQNhAILJMxUGhkz2bZHLh5xoKyk8u6kP5gjFq2TaMcttYGPUaXUrumPhDPXq-Sv1M6KigcY3-v01bS49YhhwJKnF1d93vJl1lP8CO1Rm1F-473InJVKZ5axvOdZZb5Q7yvgVeUQCvPv3D5AJen6bCIbh_Q1meCzvzsy5W6-keppgmTj0Znr96VBMrEjatNLoKZtyZ5QTGgB_3i-hHAgzNFpSGho3DvXbDfnHE-jy40t94USFyoE8IvuxBMniOGI1uaUnBHfWKGv9iZ4UvCBaV0zbT2mhLo8=w972-h625-no)  

![](https://lh3.googleusercontent.com/2v2TI-aKNFWKPSfdSuFnmp8UzDJv8hikyrg6BBJGOZBBHqk-Cp_w-NF5hCW0rw0mjg1HzEr_w8r0sXS3aQ_aQ6D10LS6f_Nixvl2_YqdnbdxUckilUjD50HgNOg0MU8RRK7NDIyao1q_DqNwFMrqsQVP8EP-LYJV6cOa9NxL30dGIa3t_w6kGDtxDcP75_tkvNfUCGXM-lLE74JC5nwZGUUe7mzHbgVN1i3cyo3Rf5vGY9ayMMr9FBItzWn9PuFdcBciSBO2NpF7KuOvw4fpmV8Ma56ssAADcltnhs45k-x7RqvAicGf2ikHw-COTeHWQ_5m8Mb_asyg8AugeJyqedFOzhXsT3WitKvrKe4bvSIhSlt-VKhdgAnJO3MALpkQgcVyO52By_k5loQ2piPPpoobN8r34BRZxtweoEUoe3XFuLgpEVjyzIg9qArMgRRGShGLoEtPSyPCz_ntdnyhPeNLLTgi9--gOifK_wRnbZrWoBYONxbA5ffih-qhV_gYD2qxAHr6UjeSqb8TDiMFuLe8w1xzjfM46zJYXKOBE99tmGXJDHEphcD8mYH2akZ2o-lu1djG_Pg8-EZAWAQrRNZZR1tUHNBrLz75Na-VVgNK9X3vPcA7JWytkuXGi9nbAIQ5t7E1Zk2qwbjDnb9VQ9Y_ax3B1lEITbLcoMxyT5kWal2jOm8N7RTUyjw9=w972-h625-no)  

![](https://lh3.googleusercontent.com/KqRi7qwcrXYpiVTvNSktPbswDvJZ-wdeCoLAQSSYTtQ4xj49fphUjLh18NdHa4b-V7Jq7CcQ5DUSs-a8XmMH3czeR2cG32xM9BYTMjK6AZs-8U1g9-kQ55dR8SaecD7PtjLPRgBxMS18x8jSl7uwAS8CBeXVE0jsJ8f86VZ_eniVk5atxzbn7uwzV-rhjOumvXP9cViU8Rpb_63Q7y0DMZEofUc_w_qrTcS7TOueWfzJkxLKew4mGoEzAaoPoAk6dvrRL3JQPNWGDVFsiL59NeGD4QakulOES0K77SgKd8IPyU5XZ4jdCYfjviD8d3FnJy-S8FwFCiik_em2u2OxBOgf-aFgMJrYmboAGNWDblD3GrOKMd7Uf5rJReWnXz7wMQf2bG2abnvJZyIyMRGOe-EYZ5rFNPmIJGslnPPSvbppSng5v9LRe9u6qfTU_0MZ0oSGhMeSzMF36I-d0Qb0kQFSvXLjg6utjMOCRGtiQzbN2ydPaVwyLqvS0SDCcMP3d10T_zC7wtxW5blf25B5WDbqayUE02cm7IhOdNXXhdRWEwzOicu4iDb23sOWZa0JNh4q0b3hS0tfS3D_wR-liTVTkqNLllCwGCAQa4PpWJ1cXBLJykCeCgL3WaGRvaQn8VOlkJYzCspn_fzSFidZul9ZAkRkzXYHIh3_Es9iCOTuhnGa4-u7VmqVqtCE=w972-h625-no)  

![](https://lh3.googleusercontent.com/advaSrDUWoICgvUTOKw23gpept-bkAmUw8DYqBgLnvDYaIrztmo-aTdc-oKOVuNbn7U9jLHJPHaiTMzwQbRxwTGO64NNLyxgUwHoYDiePeAXvRZFgVP1JTpsU_5Hx_aQg5u6WIsBqNz5CiDchCWqaV4YNsjoU5mWMwPfgqOKxuSWT3QS3zexVTkVCrwc2u2mm4nTgopfLG9FWVrxFvo2VnxT9p1SZ0qwiJp_2ljPd-B5c02R4ZxIms_udj_oN9ZTBddQ8v0vvX6_z9Wy71ZyA8qD921bBMr6upTbRy2E5sqW-AMiT5TB03Gd1viJ42Fpr-sTmF8ZoY1Z_iCmSJS4kiaYGKBabHYK8KLSVRAUUoTGZAgKe-yWl7CL4zskUCpqGT166xP9qhT3LGin2h11ThZYRT8pGNb0wg5vVDFY88AncF1m0bXW30KoSSowH6hHWTcBHkJ8vxvwL_VUlDSFDOKUNqo7q1aG7gFCXhp6FYmDkHIzgUn4it-YNHZbBhNQ9IWyumHRXBYg0JbnS92fd9j2ocYSXFfLwE765Hw1P3LP3ka3Is-ctodwBy62vAHcT-M4ySrcc_Gumfgyz1RGgTzE1FbR-8rK_n_wqolGY8uMcDabLo9Es7FQglQHd5TDxwuz-H_a8IMJWhgIzoTm6thVeA-MLkpTksn_RkrE671q4idW7n_xIg0wfH9j=w972-h625-no)  

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

b) I used a book cover as callabration. The dimensions of the book is 165.1 mm by 236.22 (6.5 in by 9.3 in).  

![](https://lh3.googleusercontent.com/awn5quRaonA8iMFAsaSv97Qg31cfW8MRLj3kYp3B06Jhp9stXQUr7Y4B2j9c53z3ea3eLchvabPxEdtOXvaLFJf7JW-L_zDM-OmDkWno2uA-KTim_uToI5SERbWSITveTlMd9P0y3_GWoEawtHtmLjwg7ajw4xx1ls8n5Z74DRuU3Tl6AOlDy2mGY6lMRRc_cxObKbG-azrT4NE6bqX25yeYjWt_1XoamS5Ju5W_KhDd39_8mHbWK7CH0Pn3mX14XWMtFg5VQEomRqZzTjtUW89NakitmBTMfv5NS3z18UlctGgaDRyi6z7BfpRS2dPXqwgn7-BhfX7PtUYAt47JRcVtC5r9x3rbSyTQU__b0OcGhlG7qt7QqDIbLjhfyVtPChI32hU2hVLGMRzitDEhDPnwvXOJlQ9dlirPjq5M3BxzGUiiEp2JDdjgZm3RcSg14Wdae3bZqptoFjwGvpXZojUyNX2fYsfdtfIBIfNDkuSxchvyNfhK_JTKFWsNNpoDzWXANOFBflq46HCud-LAUB20yeDa9Ib0N6qX238-XTVCrZL3svRRAl-Tj1RNNeXQfhTaPJa9AJzcSL_Af10NoWJNCVecwupYSYu3MRfJTn_ng5nq3UhmV3IScsMOV-tvCQYTrRcDFiX4Kt2kJLeF_0ba4ehGf2lKWp-tDbPWaHmqjUV49xj71PlKZmGh=w315-h475-no)  

The results of the measurement is as follows. The actual length is 150 mm. As can be seen, the accuracy of the tool for this test case is acceptable.  

![](https://lh3.googleusercontent.com/aPO6FKR68u2bkJn9jh_bfZ0HA7MO1npx18yRrz0DbfT1iv8lhUcb6fnEyrRe4AnriR3iyJl_evATvViLsgeJFckedTFsnQk1haP9LcUWXQ3Yiya5VFeGCPfFUMDkW0ngfszHteM0kGUvbfJK4VMdUiLnlSLh2kDsCUJLTRQtj7IAH1pAs50SJLAV3f-5wwInZJM2dAOkkumsmmVGB9JJuq22YI9C7EJthFiAk2U0HIbJDtlUt45HK9XMkmgWQiQzRHrj-2l_XfXaSO7EH03S6yvIsQ9yrcyX80J1aK5WlNUzNIHPtCjkLisxuN-uEMpj_5JRjFyFOblQRU2FnIlW6_HpIExqR_0rV81tBHC_wkHh4Qm8kuHP-V-JqZr8nnOX8nAmpcbhLxxRBBhJqVIR9LTUUXm-o6yC6EI1ELW1wdMrDahvEHxLCs0U9bJVi7PARDdSCMMWknxTaiBrYZe0udkdrAiToFt01c3wa-zYCT-e37ycvDvXi3YVIRxRVn7t-YohEKYeVmtSdxGud71LzYYilF9y8kIrzpsoQERafB2FMH8AX9LpCu3tY7D-qIu0OHqfPYmyw3CTmdKISPE6_473CsNt64VSJpKIsUacAhI1Pl-DxWw0f8Rr460KRyvyPultg_vrYIydEvc-1qK35Gz8jvWoMElKUjqjeZ63H-AyNm_iFWcSWICSRb0d=w552-h597-no)  

c) The measurements are comparible. Obviously, both tools will not be able to accurately measure the length with no error, but the results are very close.  

![](https://user-images.githubusercontent.com/58671575/77339114-b65a7d80-6d01-11ea-87dc-0dcc2df60cea.png)  

## Problem 5: Book Classification using SIFT (30 points)
The results of the book classification is shown as follows.  

![](https://lh3.googleusercontent.com/nifgm_iMyTlIiobWU7rZiF5-mguOd2QNFTZdO3F02Yrs0HyWJIuNvKWHF48bkNk2YD5i0zD-a4bwqn4B9dJ_udRgtjR30Aryw_-pTchLZH6a_ZkGvlF_H6PW2JWx2AkO9acfLOtrTIG4uqkB4DMOAqYkBoK5J8GG7ml-BFnos1qZJFMv1lHqNNMCO27m9MhFU4yvApvLuC3mDHrAgi2P8l6R540jnZ4MPr5xF8DyvwX3p2s3ZzDJ_4N9X_zNJVYYOwMe-t2zA9z90hWxXuGh6EkkEJ1D4ghW9LkjjflWzE3tzVVNcVA6mAygVybtV6DcZbjvW44YvCvwsGJnQV0psebskYMxwiYpb8Ye2Jqb-qKnikkPgGjEjStx74BUSQtfE8MGYpQgI5RTKcOjfJoAjCCqarwF3jqqA8lQKJo8J3c5maqLIEyAedOGs6lZ0hAl56Rlx8w41fIv8BSmzvNsBVG1zaauyIOBUmmSVpxklKho54KIdQkXEFOXN7wq-IB5Zr9ff7mn-756ASSwNdR72OXb7FaHRxl-Enqb1GPk0m5I3cMHA7MU2zr_wPI8fBtEgdxqm9jrS34ZY6G2Q0TXbLqQ-JOI55gMpMFl2POGJJIvbS0Ueo2HJcEXnTSW5-_LJ5y_haIxqcPa7TkNJBEZtFKpKOyOagvPLZvshLcZWda23IvtUCKOc9v9QZFr=w972-h625-no)  

![](https://lh3.googleusercontent.com/Ju7Lo-pcxZ2MCBhouZxSwjkdWZot4Jhi7X73zZsKVqIuHU11wOeVnkRfur2hEMwU2o6xx9SNlp_O6reqwlSQ-fkRqg2xlmNNoiYPgMZsS5yvjH3medB5Fm6RMg-oG5Z6yvRUyEllZPqoGH6NVlrMQ34tV276BEfbPs3FhGDFs4PW9LmoLPGUuaw1lq8B-SGJzE4N8EI3vXMyxqV6rt_iG9q772BqzieJBFLdqXGo6DbUSH1n94re8uQjT9u9D7R7fz_ZFa0pFrtLc2PjjPz_5sSGw4AWJtQyyk1SMDYVwFw7KhPTtVmxU-gJXdGx5d_63FQcHoedGNhHsa_l5y3SjO1O91HYgtNMGaQ2WqTHDSwTAx6aGpM2dXaF-0KhtYHLalLRBKyb6I-jlzXoB4Li-agbDPo7u53Rq25Roft54EvvkiUx8gr7q3_VU0SKXfD3Rp-xzUy53tij5EXC3kYo_DScmB4bbseOyt98P4Ju74L9MVTPe5CNrUXbnAHxcgOoJml-2mNYt57ALYZshimbw_BYAW2uTZcLs85C4mD-8BckOtgSWim26QhNwQyfEt9RKiaVCCFNKb_GvurJHfpsXd67vqcmuiSysK4ZN6NUxYQTo-E7Ixoz8rlh_wkRUVPUx0yCASRKNq1ssvCwWovt9vSV2MD2Vp9EDbCdrCLLq7FBzHJvYQQt5-97xHuu=w972-h625-no)  

![](https://lh3.googleusercontent.com/xsh4uS6KIgYypHUxRzABMSEhh31smA4w-nzW7GfRyWSZjD3hJn812AAU61PtmL-tvODJn4j3gMOSynwmqYkDKacMHiH8Ifs3DzrLd0XSKEDUodCvEQhPicbg0cBRTEZA6mKs8RfTgBw9ngY6wkeLiHEHqtmFy4UG4dmEU8Kyi8IxIJNJ5zlzCGwN-tOn4IK9C-6KQGwvUcoxgNzwv0b2k5IRG_L5pjFMscDIypFLYaUSHsEVi98V52kTF3S7YIesp9bu_VjrikHJVNWCYBCwjeBlEIzAylWRXv3xqDyKZT6Vc3S4hkxSIHr2bviutqqGrLmXHQ852JCYcY_80fsI2G0HWe5M8zmR7YHxeAMuYMvPoPYHLCK-E9SQgAuMGNnoZHu1nnCKKqhHADaUwuhxy0gzSmWGE19xms5o7dnN4ad8Gvn3DiU34A69rvLkeXS-NwXhU7OUBBAuSIWgLWaWOa9WJhMskTLtHCLSHKg0czcVNEyj2nhpVyybeRqTAoh1d605-FpzBMTZ5CUeUU9Q3Gd6aHOy3-N33j4lcIgmK8Mh5X1HGj7p8iwHks7EH1QDUUj2BRyUNpFvStX0Dcu_sOGJyzHuMBy97PzDj43b7ElU0YpKP9p6lQ-JMYng9YCYkJNIcK15raNKJmLpv1kWERwfxGDLprD4eVWtE5H0HKUaajbsByLfkTh9hzwZ=w972-h625-no)  

![](https://lh3.googleusercontent.com/3dSzJydal108_XUzjTsETEyYz-EitpMZKyfgLMmmvluvX-nyIlLEXgXK5cZbB7TWyZDZmUyWPuC38HvHqlNI0yX029JqEJzKfOsyXyW7tfPgnhz6Y6lEXuJ66orsCAZvkuHATABzdYmCvZVhcOYgW97-3Cc4pse0RkVEQYNxPt0Kl0Hkt55lNP7jkxHssCGPhMlYEAD6XsjEZmg0eb_sYHDA9Bw-t3hCzDPhLiDqoJRO9iCO9-F6_fr4ok5aepxAQtynFaMXWpy9r60AWN90Gg_P9SXEKKSGJ-4KCikZ1m7Dol1SM0l5zl35VVf9S3yGH7GQQS0HATbbjJBQx1IlllyW_NH0eHr1s28ZHGIzD0NQmUkewc6rm5fDOAHvNjyJlyDW4Qj84BrmLJFfL7xyW0mh4N1Q7AArlhAcw9y6ESKVjM1NzVi5uRpXCTUqvr2hHPY8K83gg3TC0hxiMFiEGgMS__XmjljeZ0hukUS7HNB-TqUGiW2sh-KS64mC-azYc7E-o4P5ye5d-UorNDphwYBTN6-XklqLfewuGbsROreew5JrZrMAf7YRWEtpaA4Q9Cf1XQahYHkjevvo1HvMfB4dgHHn5T2RoIgga8uF5KN1NNbX4qt13HIzhf3_561XvCaIMpYPBVcKO6ingj0o_R1r8HRIg194cOv3Kxe26XW3TNQWnCSPoxjKCiVd=w972-h625-no)  

![](https://lh3.googleusercontent.com/HxsNG4GdzEy9VfIIbPnEtDs2dHY5udKppqFC_B1PwFhvCqxoCFTorfE8Vqz7Pgzs6zYrUvrHPHg3HuEjOTVAXvakANABuoYjGfjKlMh4IU65F3iaHnUdbLAkAu86GMyXyWOKedl_s29lB0fmKVkydnf6eJXUmZV7IhEs8bajMmbJv1xHBnyNN7PGW15IerghMnodki3JMOBd-CpPXtx2DEEM4GSNpfY6aRED54U9YwcbnezRS4b2LvUlE6VJuVrEpO03omMvD1ZzyvjGtoqtchZXIOMPBa23xZZpvMFpdu3S5yCbRmzItjZLuQPuqBvY2uFotJQ3O8FpGWHNsk8a3fSNU5v5h9NrfkSUclMpIzguf7Va0mqxDCYTPzn6AAN3afMzUgJh2Mm6wU7-u0oKh6HKTyPddytpfnIlWhBx6D1bLSI2Qyst_DRadnRAc8idyqkARUYTfzuB-1p9lYsuQOHqAHOZ4uiH8-WS5kPHQzqQhNsM3Pq2QRIdHiIEdZTlq5vAWZ9mcmcGcXGmOjScX-JSu3MnoAh0OIqRAnVkxMg2Z3EsM_kp31CNZB4vss0odu7Lv12HAMLyY5XxT99lk6sFfBL6N5_6AyZ5FsT1i2qsZNJS-8Phd75_xs0kRuXk6tSQTyki1Tlxr6PUx2zFIaar4PeneQjKnAxD43HS1jfaJ08bfVWShzxw-SC0=w972-h625-no)  

![](https://lh3.googleusercontent.com/Z0KWC97DQ_VDIB6otQKoGvqujPsajFxGBRRDm9r0TMZhkLS1vvMrIUaH9Q-g1XB2g1wOSxMBi4ufQbtnaAELDhQSt_bSM6vb4gB-vG6mQ63JK2bY2fT0zrlTXIeLem6Hxt9h045khNDLTMpgBiTb2LLxzmDMTeBbl7k3Xh5YvQTjHmrm82QmtrpBMAtKHpudDRwgspiRPcEZRn87p56rEwJaUmQdx7jT2_vaBPMwajAvRy2DYkim3cLMzB7Sxyw4O_MFIE9vrznSEIA4_PHAY4NIVPdPt6c3dceYlUpNFiVPBFfJy4KfqN9cNT4vunA3SJVnrreB4EYQjl7Q42YOUU60ATbsBBPhvj5YVkE0RmblXjsScOcY2_4BWYJFZeva77ozRENpltRvZtzg9phbyy08pZkGt2OU8XPFX6JR6Ye8LYSo-Xhq2yb5xsNf5dEswV4N2lnT2Rgh-GolVOz6jOX9emf1G2MK25TnDlR3WWrP1dN6DzDwE4Q8Ora-uZPUfg1xjwo1fdlbkEHSntf6fsf7kPJs32rBEzfHXptWRisn3Jy6dL7Q2nFbRLavMtX0VezFEQw4NQTZCEWTgfUvR7nUZkysHBlSR7GnumTFWJ6NLH6VB8azkU6YkC3xeMa8kGqq9IdIZ5pC3hMxIpypfi5NR9LLiF3VjRxxdFmpOnyXWVZLQt810UXD0buW=w972-h625-no)  

![](https://lh3.googleusercontent.com/mH_-AL8JGmkUpNn25I0pm6OSBKCEIdUP3TA_txw3hAD4Nw-6g5h1ObfcPp4tlPRvBv7e5GesH5vq4pdLItAZXWtdtt1VuHoZE7ifDwhVmIAhtp2K0LbAHB1dKK6dmCZ9hbA9z9SU-BjeuPnliRiFBoM756bSBZdDB9PjpIEPjQHcr3bPf3zxy-FPNPikd3DrUeCYcH1QJ_DsQRa2NP5zVd2XL27hdcQaY7k492dzVfTuYv2ho2PF-8HjiJOu6crB6TbSVpUNBOb_HfYMdbEXTQV9GDEa8axYfl0gjemurCSktaknc_X0vWL-I8XWBS0DYOs_8W_Pf0q3PkUTzSz6QASNJ4cg6pUU5XZJv7DvuuiM53f58VD67qEXV48esFLLvyBZSzCl7dR1SESqVm-tZQ10zep-Xg1c295PiUEhko8rgKvQn6NufAzACo0K6LAnPSVkPyC_HAZelsa1QKvpP9dbbwDHu4cl1-WR9W4J-85ecR91ZsP5LJAA55WVnl595vrbaIsU46V4kY9v2_G181umCFGprkJ1_rql-bhdsdTTR2WEX-zvLcdIWUMkvwWjbm0VAGm0_lFdl3z3dLr1qS3Sq3opC7UznRe3tOvp_-5ggQ4NG8rSNO0lBo2zq0fan6cujf1LlgdE1_L1gmIuQ-YK-4OuW_B1QWr1nClwTT_G0aPVoe07LnMRmmVL=w972-h625-no)  

![](https://lh3.googleusercontent.com/WqviLLbjOVwZnjmgU60YauN-FsjIASmen3hmevkvwo8v0SzOFErf6qoJ9pD2Ui9Whb81Ila9xJwT45KgdoEEUxm1WZwJeZEidbFZE4w31qDwO8-_agpC7MjjqLmU4NTyMijHAQ_wErHIF20LbY4YZVnQEvB6T7ViJ_TpZ4OgXrLAd8Eb-QFj1z7SVPSmX2iXoVx-rYO3-SfrZwGwndL_XkmJsDFE5Mh1rhhCmX7B_QUIlm273Sll2ZzMkLnSxtFHVjunrOiMVNUxuFwhtmU1GtINtwOZbgzFTRPOBHhFCRSYPhQ4tSid8Kw_bQTPHC_MxM1-VZ53ZFNeNPWvBpActsO85JxxvIZmNWNngcRhK8I-ZyrOPtO1RDcdo7AEalmTkAfMFwrGrCO2d0H_DD_tbJiVG4rIinM89pRBrjKT8soLiBLHsY6wRhHfQNynVLV08I2jf7IY7h1OQ4z0bV8M76qBmWnoeRxY-7s1kMok5zKukMIfFYnSgUlEYXeItmThPFcaxKCXbhp_c-xgIFa7L1p62EcPHV3Kh-ml6LgF2a25oz53-62pN7P5TyVxb_krV6bh7OcXUs483P1Vf-0P3VKy6FDLeUnI9olNDdXoYYfgnzMiUwQgJ33EY2KP0uW020v8zUENJ-zKNMpagN9o1JRhPmtBVbQdsiRFhxebhq8ExLs99MlbbvBwZg64=w972-h625-no)  

![](https://lh3.googleusercontent.com/39a3v5-5BgcbxlfO1Zu77WD4ztk6RvbwP9Eh19dz8MGwpxMuGkTPHh0FapQynV8s57npI2iOQJ_OOLd7jsXltClOw4jSR7SBnc07xH3pxS5o36RszRrVsncwiZyB3BA4IT2CaXJflN49zfIgfPDz1Hns6kk3VYgeT1W07_jyCvPU86OFgSU8ndqZxNxTzVSF-o7X8JYSAX1D2eNF2D2gba45LUEhjNdxcn2xbx3jq0S9hjnfb6CpFwfja8LaHQgZ26ffGE0f2we2SN_7-kcXDQggEyWm0GR-m-zUq2C8r163NzqkdgtKjaoMDQlcGYhLuxG5acQlQ4uZB_01c0H_41D6FXkMr3qRdCiQDNmSH23kP5jcgmhRZBP7s7HOpwBKXJsVmpEWtjuGxz-6PnaA5qmDUxoT1dw-MJwpJaay4XB_hB-Dsn1qWAT4uE-qj2vcDhZKh3dkE0-Po4I56nEQ4KWp8rzc457JkAoHF1wcF6jxnge0Ktd9a-DmnU9yViwIL7va-hJWSvt2hV3qyKYgmtwfWrEC2vYyFXCR4v-N3TA2PV-pCCOAc6-GKTAqu0r5K2D1UV5w7m8WgYuD9gzhWqHEqD2IApusib7YKE83hzccdc-cV5IZnfBKKauhGJGCJnmopIIO8hG_CnF2syjKgKWmYvIF9Dr24tMv3-QSkV0ycwrQtpZvT0xOk_nc=w972-h625-no)

![](https://lh3.googleusercontent.com/5P4rr1xyO5ZAzpPEPVONqu50UQS6p2KtIxvuC2G9KnpzgW_aZUMJBPSH35tsxnsTSfJUyqKV4JmhKXhOxyCJWWXb-erL7VJa76VKC5kADrKWjE0bL3QE3lyldLwdkAR_rME-LcG7AG4nACWFdMhEYvWCNg3VwkQlm8US9YGRshcKQ6fkqvSHG6RNSmzOIhsK6sLjk_9MCiNzNmex-gFKteYzVTRr04xxmv1xttDWDmu-r9NfInJEMYqrYlVS48ROqIBT_4jIistwcNT2EEuul7VkTVii1j6VC6-LD0tmrdhGcMen7DzqQPrCtWGTebA-jE5CZEWcQWgTdyBcmCWlNq2L_KcG5AOZiu2pxn1wywKDlT8YKg6UzvcbBiJQTmApM7Cjey4jsAaJAMadJzpUQmS9OQZfOr2spxxxEr6Sw7006fWX_lt6sMwMNE_S8LVQsw74eg6FxY4hz24Oq5CziBRSDOVgwkaNaUoHpCRWL7OQuWYr1jJTuJ142xlW1DSUZi3QFT6gAuIQMaDlmpIX-TqjIrK_oPkQJoyI1yaMKNdc80qMU4u0sjeA_LObc-812-_DVYWfOQOQyG2N0KK7FQ-C3fTJYwHmZJN0b7TbeYGGbLgqxPVO546t1I-HqeMheexVnif7mDy8J_8d5oE8xZiY2Fldc3xjPixd00bttMAL-JSAMmyhdpRvPgrg=w972-h625-no)

![](https://lh3.googleusercontent.com/zmR7UDqF9u2nHKI31ArCFErHuzdPzw2AGimNUtSF3uMow0IiG6Xhsqj7txkQTJvWdwICGSEhkbQ9Dp3_Abh-a9uMug6i4zxHaFPtWaSBaJu8J0MRgjBtGB6GPY9adqCxccQosGTsPn8oz_cNcDb8ZGIlUP6UqiNLxDikIItlLhZ8qCbzra1kS5oXR5UwB7BKtONcm9KL020Wh9beynxhGMD2HtK7SINAHLhBbWuNEVnsn7ShvbJJFlWJsFC5l0xUHbYUQx8EgLw6Tl-W1_OkttZbQ1OoxFj_5d2TiNaNKoo5OwhnBYeeP8SfZmMR5-jgStXFRFToAeVFBxpZsYa2Erof6vp4syT_hkWcZnW1vmLTaqiWWEPAmm7zEh-MtCSQwkwZGfFghe4Muee4abqN7Em6MDrgdWN7qnfZDYr7FO7a6HGKa2I6ai8R8gnidpoKEJLeP5fIrada26cgvb4x5kGuKbnJeIsKi01_Ugi8uIwNYDnnl8VlFWJzGYnK8K47n4RR6rPCoiRS21fE4UB1W4YeXMjtfEo4xaJVo419XdAXwJqpfHfzxzt__OuvPJRWkCfncLN82bXAixRv64NrHvTJ3fta5h_adLTYSgT1-4K2P6dzS_uwkg0TfpZgo3E5dBtFnNUFPqJqWNG0_L6rZduEUWDDKdPCRy_NnFkOUc2ElO1W7fja3SCHI0GU=w972-h625-no)

![](https://lh3.googleusercontent.com/hVKi3-okxE5e7NoRKdoi0kv_PUQk1cUKJzgp015JgyXrggm9HfiyU4N75ZQLnR8auMEfnDxcKDlA0Nk5vO5-5X2YsV-SLZWzeynzF0xJA9jCuKNJjxHuqxU6dzBbXwKN1nyeOXBLVPOVgsSrx8Ya9H_ou1zymKxj9eN-fpqrqUx72p3ncupzmLZod2MzzQx_R6nI-ndb9996mfpcj1BpA6JMoIedpFILPwQYtwjegr_k4JZ8p6XUEfo-m9grl9sPp_9XlmWWTJx_399FFPTe9ol3vc-lZ4jBurFDL4MHKbHI6InLhtO8kcfTysSU9jm9thg6OwlWyZN4RdyT-koyMpl0wu1l-DkTeriocXOy4hDlpnypEUie6om9SKbbIsZA_Y6JfC2_xNLS8AwYMr3wE_hucnwcg-jNUU8z5Cn1rqH-MH2fLh3EKEwqDKgiORr_620_bt8Cvx2ssGPmSwC4PHLoH9UXBtM4L_zezsilnCe8tUdlmfwAQHMITtCHFmukktm3mqjioa26_mhDTPCh6ezHcG2Ej_JfbiSb-wRp4R-x7FQfVN5AqthkkPVb6gO5XGJkBxu1Cgl9buE60KyG11lwgomWTRF7xfT2G39Ty0GxTnYHMl6drjT_DHCxY4iMkEjoX70_kVIx0SkC-C5V4Pe6sPuhUKiX78d0NjcgHF0knAk9cPeeMgYQobuO=w972-h625-no)  

![](https://lh3.googleusercontent.com/tFbYvyvReTugZHxUOxSdSeGeWbI1sv6koL7f1HvwKKnWfxzkhnvr3AJK2dn4T2xlALpo3XeNlfepIaCZ5w6Ay0MiK8iZ47MQ8-PvcdUmEz-42fAewJ-vROCAKiWtZyYv5wRO9f0BRX1W83nv25A0GOBa1XgufuRdN9A7j4bGNo9A44b2MCu1El35PCG90-YC7pimD2_TDiLKc4Vltp10G3Xxy5t1MBe0dWkGJYQXItr0IlweHij4vIyfMfBEPVvtQqLpQfQ5_sT2Gj4gaS40rpva5TlknmPjdWyQXaYKRUiIA4QjsaEE7jxVm5DTPhoOohiQVfxNInooR3SJ7H0SeZZ6d7oA4H4kFDTODnBUCtROAsVRYkwIzh-E_8zkemQL7Imgw3pssPAsUqjbLN0r_zBXOU17P0n8aVVyLNN0wH2uHwH-FMeeJLhTUfYL5Fuvl6ZJypT1TorY3tcuXWedLYW8X5bFgBxoFAM99eEpb-ZPI7za7czpBqQhkefcqcq87atZQ_-cPj9pT-MHEJyQ4ZMDZE4Q3XTmDkg3h11b0uCkTKTDq-cmnI9u9mSExyPBJmq3QbjtyTXwCdsRmVjIgWVDM7aUav03W_ZTqJKAVtWVPfqCgbXlIywgOYHYIsO6wYGv4Sq71V1XBGmVYddOjE9fzEKmJBRd_mn7ZuLe1lgyruTpHQ0F_xSnjrxG=w972-h625-no)  

![](https://lh3.googleusercontent.com/pMtrB5gCCAvHF7_ufWqqDz6iSh_j4Ehy_Oov9zOvaDGJhEBfI5sZfDBp7kt7a42uj4XKdJkQ_gMMVxpm8MDdg3lijm2sdZmauJmRnKnhUhhmbvckDkauRPOuBcSq0s99NcbJYO9RoYCtn8Is8VB51f65NlDIp4m6flpjJ1YUuUJZgeRhvGi8FyKmWBXXlE4QrCg5wPJxxsXAblikaANkUFJa90NFtstuKBshf6YfYpFOLnLlDxlEDJxuVr-gle92GD8eByG1tpvRoVZk9isbGu8ZeLBjrkbYEklcnmO2lXeNmHT2R0VP4sYNvt9hbH6VZd1NkEM_6RsqzuZ_l-s2oYObNHjJjaPB8afdRrw0mBAb7-FKL-5TP38c1XWE0ZQ3igkTDoxh6oEjfux1_r83CHQJ9_gahBp79WunSg_Gff-XDo6ilmjcGexWbwXLAoyV28Tdi1yQg4aEAO6zgrgtgTvUQPW9b4_OKhJyPU_bAnBoCk8d2hC16X9jsLYSacK0lHfL2QTqeT9O0nef9S0f7s9eV4XZFl-gnmnj8N_b8_cfcZ4rFwTlsdkyyxKrhxqHSMqU5PVVrY2uWkDbRGNJA_ms0nqCNG2QFTo4pBsAZWCiBUPyehhwoXejFx_xwL4yNOyafToV1UgZdJoyvvR5coxOWmXYMwoQv4zGq4G3wfLNIpwCENw26yWuJqdt=w972-h625-no)  

![](https://lh3.googleusercontent.com/swoS3wJJagQZFf9ODDBOW4zdFlpA53sZU2F3dMCE8KB3xUiOPFKt8jk3o79rIQEWQTt_5oHtvRVHEsqtfRifc_cDU853NL3jkstWCh07PMpVfP9BIriCvKcw3wZMpoREmI-h_7w4Fd0ROmpu9I7wvhgQk25iJtYE_g2R0jSITGtMGfK9XYrBjMlXOqgooreuTRQ_hFa3faAB4IuKyU0hSdpk92JbRNiWBvLyQQgS93vuIO-V_K09eE6YbOrj6Zzcf9fOvDZv2ClQlIZ7bb7maTHTccFJg4y-JwwYV9gKFz13xgBrIdx6T2jJIHu5lQV-1zk4DhylBCJ0d_jcR-HpGbagfRCWCTnUrhHMaYb4WIf9eoHXLV1I_OH7W65CvCgl0A3dZpEHRyeRKmy0KUryE9-7uLmmXzJfxSipEM4YjwbFL67vtGbZFE62vKdyehqD-LcsS3Jli53yvEt2-cqXctw285YeTBxYzzq_zzTDqglksX9ao0gB-SWqRzrlbeDW1lrA5FhKjzHHQxQjn_junGam6bEmG3Qabs9vnXlsPZsa2F3bz3L6VeMj-pzDIVw-1gVI3icQoXzTwlZOrXMe8jHLFnem_XZVAjbzxQmmNq0E-HK6x6aksZev5tApc09TNvriXmFirZxQotl9q96nezF9m_jEEz939M6zSvmDWpBZvtOD_saXvxWtJIpD=w972-h625-no)  

![](https://lh3.googleusercontent.com/XPUyXMMK0tz-4N9-_2GkOGc828n-llUEPgu3SOh2stKTTiagzJRF2LYc2rZo1k6fIIyhyhNUu3gj_b_JUF7s4FPtrYf_ij-1EUN7QRh5_UMzCy8IPtSnYMprlAfpZfMcDZvZZ5tsbkSJoM515rmthArNgNgSapZIe6HYTv7rmy735YVt6H-miSy0dzOGUQ1aM7MqXf9zF6T7NYritYEKHBmd2EwnS8OqhhRK-mWXkYZnKmpkaIHBt_vtQgdwAOdpewwEWfM6o33emEdVVSq-BmN22UntWOmoGDJ_FQpl07KhSHLj__SG0tKbuTHHR92g94_As_fAOGue2U_U4eQ9HT_hB1KUWafkCqsNHwE3rjU4JlbHPmJgYppjKmp-uVf_sMgjPL67Nl1rMxFP3ri9j-V43It4LsIXObRSImq7JYPT8jYi2WlgooHpeM7Z66oYqIunHF1qcsXOZ1TecqUgtlDgUmedtU1M3-DJFN8Q8ckrMsctEGhMhmXNrb0aQVRyzMntnOlN_K8bJ6jqd8vxoUEuoSfzU3JYdrg1kGHDIyw6Tw7Hi7lwQ-kjpNhwJxFmIsNaNk0ZfSiWDyh_P0VMNxU1mK1cnyN6fESMhCOGLF27BpFhQIQh7hxHeh8N7GFCRr9rI6FHuHfdMzlp6IgIefyxxjQv6zByuYephg6Rd1kfWKiOwj9ka4Ze9KJK=w972-h625-no)  


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
