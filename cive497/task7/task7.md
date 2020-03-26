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

![](https://lh3.googleusercontent.com/w2EOwI9b4_yycLDjh6gUMinmVj2uuIRjeNvkG5d6x1mZAItExCtqs3djdpCyfv_lFXoipS_sSAIpui0Y_A2IWul3E_nX8-kkybHX1rTsmMTpmKD2pdPL3v52E0zPw9coDcIEy5fnYGYy2GZhCe9R8cmPBH7-OVXhGCJ-NG9o2m-Sk44GcAgpvUTEsc9a_ezk_cQlshhpM8mVHfumyLQoG06cDGs25dmE7BHSwz71wtVWbEkIvgdBYNsItEET58Y0ipJcMoHxu7WhKrTSij9GF3A41NBfTYI_2F-bgHxPltUJYsHP_Hrl3xXLWODATxhWykXp_XXUJx9sKz8GcoPGXFYLyD0VxMLPoZwlnpDy0f9vEdh0DcIe3hntL_NCe98K7zL-excj7KG86FeghnlYRwrX_r0T5Nk7ZDaxfptmJp8oKB-JW8GMnQ3OyO_Yv_cJDgNT9wkm9XpSGVYGxqMK1JQc7EPVHrAmqatcbY4jEY42K8VPkS3EEP-mdZD0yMAbhMIyoY7heicXdCxrYjR1lOdg88nymKNXThZOKLt76XAu18pqfEBa83kFHucQSHfEawfiZHIf1preygOhka-k2NK2IEwGAi9NEzJW4zr_uS6J7HhfmN0Vpntk8XEdOrVk2ZOcAIcNSr4YqhNC8DAQd6Hm6mXRtFUBRg0J1vtfC2uyb9yg8KkhqqkhXkl5=w972-h625-no)  

![](https://lh3.googleusercontent.com/_Ozy59p2_KIGrsO1GrGTRekfya_UMG8pYRs3Z_KVRT1rjjBdfGB3V_piaw0JDiXfGzpQncmNQiOUUI01DbQXrODReKhyGZeJMKjAuy06fi0nXB7_sXd7y3Ix6hfxsyTtfezbd0YmbEgzyC5P-ugaUx378XuKtrTEj-UwMKjw6oQaf2fkZFPB964nKRRn4CgQhoxZOycQ515dfSJc2w2qVrImaTYGtWk3vtEe6AWYZiuwr3mQKxujfbNGweG7zGAaKqITYhu2leITFzvhfLzY43xAKQBIAGOENc-9w5K_Tgaf3naOFNl56siHk5qtsupoINzQJzZnEy0AuvXut_5ek8jAcsS0LjFO3W3ZjQeA98oTH5S865ttD53kOv9xLq8Y62-BKTOv5p1U2cTKz0Ci7LdMbbXRGOz2HfnVr0vOW-6Z7BHjzU9CruAXYqzdneEYf75ofXyKSjSeX2tNklaJR1lgXsmsIDnE5-2_zDji1rFetbPpp-0x1-TufZhrEU8PlVKUnqTm3baL-EJTy5pCrD-3Ilo_iESov-gKwLfeZaAN3dcE6LSgKIZl96qcZuqITVxzmdNj9yLHeVVmBw43kTRRvYQXCOwS1ij3VIWDH_f-Us7yAENK26DTLsbVzLH3B9h6Qe5Iaov7iHRmcqLj9JLGtrJZheDax6wSQrvRFAtV2w0igP_CzOVwDoNu=w972-h625-no)  

![](https://lh3.googleusercontent.com/qf1hpjGDkwGZHTxxUNm9DYRJleF68OmTXW_Zbta5h8swIFeiFwjpOOQp3kCwLTbveOlXzef8gJz-kt3x6--dJfijSUna55bJOeTeAsXrl0smqqjkjIKcdYUfWt9ETmccn0sJcr2IT9Tw4YEyDeJYLJ4bBicawaESGYJQ7gJ5kueThIR3NbjA1gCpEozyB6EKdHskfUvcdzW1z5lgUMno0XhEhlh7RA2BOdQd0eVK0nGTJPWqM7SRk7kArcMrV7sxgFZcO2EYvxCzjoktQjwhp3c0rtswV-C1kgbZT3L9tSJMvJyzSs5Np_lPKVL6S-yR2B5FKEWpXGbVu89bGX9Z6-L-ptCpNSAmRXO5DTaw2bfuCDKZVnVbC4eskRLVqyWJPnMa-lVKKR6ISeZnowwlEccaFTOWx0nm6gG-qvGofrxHzAYE91chus6ztbwhfQdlCqDEDEacGsym5CJNHMEGX_HKjD5pnIvOWrNDGN5OOYAvIkumbcAgXZrtVaYlypQLAu3U4S2WWG40SRaa-qIwTgJOyzOFPoG9RdRufVYdu63N0hC8UxTrnhoxHz1FHpWRLjT0g2-JrQjKe8KWwpSybge8vskoCHI5ZpFQTPCp5li1bNmhtFRknlLqx0GbYZfn7uy1D7QThBB_2uSpUDSOsjp587h7_5lPwMrDpl7Ti_KzAGIRDmOyl2Y4MPH0=w972-h625-no)  

![](https://lh3.googleusercontent.com/CeJuNs2VpBJ6EZeBx2wDPHfLCYAW3MxyEQIFOunKPxA1phjcb7l4ttj2xxaM2JSOFLSqT3JJoDuUlU0pcIu9oWybamm58wmjgjLZOWRDXa3Dn1pG2iCH4mLFGWF4Nx6sndmg1zkojNEwV_Bv-TmDrc417ITxu1_QUA7oHB48ERAAbL5evis9rugIYlxI6JeS9SIxOiL9RLqMhIqQd13IFDubLI5-ievs1ZHcLp9vawTQienT9v8mcN9jesfzUpftGP598d63TlwBHRt4hrIi9-0tBfdYW4eAMb5BEjWm98dBPZdPApHPA7sQxQ_trKIOs-nhYosQeGktkByfcKl_ZMoemarDIu8F-rPrust9C8A0U9rBjQHqZkuBhzuPsGDJrFTZj9UmOqd7XC7qx3o8yc0I72BhQoeg8e2kbEML3NRFJ6vC__xZjxtydat9-rODc1MSJEed_bgxR9pA1GRNCa6xxyYWIoLaPPtiy7SBdRKuCXPmcjkgjH08_wLQfKV_RkqVmm4tsZFWqJLCJDUhFtTjBSmq60QqzI8n2bQ0BhroZmg2qcXd5eYN7WgixuH3yvwOVCJi4mwHybrLfOxmrb0WKI7LYL4-QFjF0hF8oBYcfFDcsrGQAsjwXgyXcWe1Ypdv3v7z1bQzVu5AZzU_OTfDIzgIdlS1BOfJntYWqXIUqhNOnaVaCydDxoWD=w972-h625-no)  

![](https://lh3.googleusercontent.com/XACgx223zJeMjc44itzM6ANiXlvm98fSpFJRDQfAXDxItMmZGFTvrHrwR5JWlXyeNCdq4e_5pbZ6_xppv14fz_Aka-z21jPRw_gVRpP0ccc06Uo5F_CqnBVfAgRDlYCnVMIf5eZK4NBrxDnH2j9SRqlwo_c3rnq0csc9PsxYWGt0Y66nvbez5hGfzS7WT3tyx-2acD8rKkRCH3Wjq922uiVXUScHCi1sovaaTHkqsYpQyh-PXPaJj5a2BgTp57g0-eS-mtxKOzOXhR0Zz55DiqCNt4P8HcfbnoMbJ8RTJjCGshSgYyT_UBbtq1J-Lx56trno14dM0PsIQ8b4y1WJfXalK431kaCrJRixuS3EB79eX5Z9J-IFOERgWqTCjD3-R_zrfGfIabSiityRryIh9ulxnG4_7tpbptrRlIU30V5OVL5AmC-i0KHP7RSHvMnk9pGz9n8hbxwdL7xvYrVUjaErMM_vdMfLZbCKW3W4zn0nJb7TRIb6Zjzr5erN4U2HSFKOn4TGaFgsr6zcTNQLQ2Wg-1OymmlUKTeAksQBbbLkfW6i5xa2P9Ib9-2UqI-HxjwIp5XKRlo2Upeb0wiN6FHrYKQZubgHaYJNpX3TLm2WexAuykwK_GISWtXlNYc7doOaFzZbmRvsBYVZW9SwzmWDN3-Q4oZvK-TVE6GjvQBx8wVHwKukutvmCZ4B=w972-h625-no)  

![](https://lh3.googleusercontent.com/Z0r5e8NePOc4Rw6UdVq7d-g5y-Z1MJ4fd1nqVdyIijftZPnB6crly7G-ApHofwmxqBalFU_SzhdnLhtk9Dg24q_tHjc4w6jblkfBGiLvEb6nPmx_PaNRpwGtfSnOcsYZvMMpjy5mPPTd2YZ227UAyrFb9ENjGjlX_itoHdoMBZHpwIxGkL2yedV_MUewYRECwRCznKEi9PvdtByXaB7ZNUkyuJsqBAO_r02viiPLVkIg0d6n76PHCpY6wdIxmgCF9OLIrYu3_d2OMOUjIRqkGIBrLQfjrGk94NxuMROnLLN1VZOK2ib9VQiYez8jXZRcQprfv_1mTnpJUMUfq95JjVAor0mdulemSoDWUJui-MdlCJDTllz81RSBV-MyEuqj8xjfvdoR1cvbo0GFj1Ykm5kfvIZFnjZfufcUj7vhePjuVOyqDCwg7RszLeS272zSZIjm06KLnjlIC6jlSaJA4n5Df8YMVv549GISmBUmiI7cVVzrzNQRdUkzbeyiJZkgRL1X_XskUtQeeVmJ-8hxGW9TTsAqSH6W4j8aJ-x4oG_S8rmxfHVplnbN0vtTfqKG8xqSnRqegwUlN0Tcrcy8e7_cwk6qWCjVyfWO148CNW7xeOR75XEbAjX2ONTEQoqno_7y8MYnPH7lZcgeV0Ifdg-z-rMrpl_WcwPTnYJ764yOm-IVvofffu-QZ-TQ=w972-h625-no)  

![](https://lh3.googleusercontent.com/E5lx63cg71QeN2bRC4yGzED0mFgt_bbm1OpmufzKGOIqNJdPjDQwXWHzUNsX6V_p4-EM_24Z8zhIPzyPqj6opSEua6qEUJTg40UPeIAYzqY9eTNXtxgPLA6yCSoQFOuD50WqxD8tL_51YgGG8QOj6IL3r0BHky1dvrDbllzkjDOvYkBNzoQATs6ALGQRtBvHJvUJEAsKbuuu_WnWiGxTKHVqCwKC97zSXeukQWfZovWuYW7Fvsq6eeCJLPeLN1z5fxvi8nFzbOxcCUXehpm5kXvuwjyd0I0yMpbMlFDzRj2ACi1aj-iTCYtTftX7EL-bi2qIr_xTxzaFg2MK-HK4pTqOi7XPJUHDlq3qIn40wqSTiacM_zZfn9xRVxfl4Hl8hq7bDSUYoKArWRy0o8NNaHNVL0oSnjmy0rO5qLbVBvuR9bfrLj1SqriHgVOofWdnA2vPwOyTzNBXIe6F2Aa8DTa0ul7NIprNAI7ui7CaaUdbLm2eGXcBOS0K00MVi6-lDtQ6-rSFjhlXuFYv1gB71gzYgeEyHMnaHg0MhEuKqOqkz8diKK05EaUSXjx78ybQm8JJ-h4mt63J2gWzAaZtBipqnrxFdAXV7apkVsZmNzZf4qDC_UZ94F2kAT6p1D7m6jXjl2wcS8u5IxtLDCm3k4wj3Eyg6rO2xoZcuMqXhVjbWmN2x6IqOJWA7k8C=w972-h625-no)  

![](https://lh3.googleusercontent.com/VV2F3oiVF69kJ-zSb7T5xfuacwngcJ_JQ_Hj4OGBQvMRDGUMaAOJ8N2EBHD_jnghuOk14IffWALfLVhUoCgzeruqxxji5neVw-bfX4rWeyG1Lj21zHEfo2QY2SjAw0iMMaSVtTAklA9TGH2psj04tinZEsagz7kLmo3PVoxHTQ3s33GzRcOdP5O1KKsPEBeHwM66WhxK0bUZif3szZIXBRA0-JD80pb4FNGJiLOkAXjMz3VfzENKgKidd54WVAxH28hXbOTIWKM-fomXGfhSEfYrPl0HkfB2fdtvE4T6wnh2r3UPe1OyAPXd_OHzDdms09CHwCAtPY9HIVWvWOUE0TkgChwUMJXu3_nVncdZhXkx8BZ_5tI4fS3yhB9AixRWF8mUcTWczCEofiFzyeD9ppNAX39Ka5wL5n4jnPrOCoPTGbmi6yBJhYa7-5aqLE1BIzyvqaqYbsFrd6vzly0-mR6CJYI1cyf3BgzTKuR-wOeTbA7WL60FfYJqEzHl5aqyNxnv95tiyCY-j7GO3TWoujNLAs-43ogbHkKNrVyU3akuZVdjzdHxMAsWWWh8goLU_W5o3XbjOrvEWFba0XN7XC36GmQSl36rxqhQbvljZZE3WxKykRr4lCdp74MmS7upJkS-sxvROHS4yG2MxNkh3R38XvWjUb4egNW4t0t3P4Z6utRy_OpVkON5wqvl=w972-h625-no)  

![](https://lh3.googleusercontent.com/27rIX6U3xmIsrJFmsUuJxQMu9gjsk4HwB6rScY7qJEyuJCDsPGGnW0IqrdUHPdKHJ45C4GaH2DmhXRkpdy1mnZS4VixNrjZKX5NIxTXTDJtDMbBeMGAzdDqjMl1yPhPcfLJ6qKQKJtvqkMt7vNHty51vcWQjffS3kpuzwUn1l7_X1m19a67mQDmDjtm6DlPnFvnXH5g2ypeOj8IVTPSZifJW8MUQ9iRtnaljuC15Qzoxk4GYNFU6kvT0BxKYsobLdkH3NEWJuETw8eQfOzutQbp7q4Xjx9K2G7LQ_qKKCKQqNzo7ejB8knlHwSyUJAPdxTy7PBsKlKO8bdamnNAyaH1QdMfM4LuumhJ787oGmolVCyHpLiiLGfDeuEsx_J5N3LuVCXuzG1J861roy_zhLEtaWjl7pymTQX0zKUgX6XCUfk_4DLRqX8YsXMtBKUGF5izUApiGcUzmaVYXTNCUJs6mViLdtpRBTI0xWwal5MoHEvmKntRAVicc0eIzmQ8yTcQBtHYJ_CK0GYpRUMey51jY_kMXgsD86IieKhaXdS9Cc3igYjGtRSBy1BUGnsWr_Qe8ZfbG13ncKJfHYmFTFE9FPpsAUL7VShuQT5vaZpFGgXnBoysNKDzH9KgwN5_zKwjh_ZQl8SOYZv3GTgQ__O69_kms46f2D5jzYD1GIfvOMQIDLcychNMr80ia=w972-h625-no)  

![](https://lh3.googleusercontent.com/h9g-Fax9ll5dPCAs6BpVlp10at7jLyUOExNaNjjo8pluiEm1RbosvtbYRvJhmfpUOR2a4M4GmuA_oozg8dFTf3wIavZcAER3jSiriHiY2Ipcj4ew6F5CvBBLFBvQsu38wfr1CBreUHJkWRoS_AMyUvTDm02eW9v1M1RTyPoQfN4zMtyt0xvkvYAGBY1DDHdloXKO48Ay0wH9JYZZYdpzLWQs9csJLQz0mgG-SxY2aBAz3-9b3tggnQRnnesSblVof3IlT1ivSzZq-mlAhddvVYL8tnZJFnMpp1-atCgYIxeeiY6SR0CPnXWbmGBcwN_jx1bswCfEagk1IUNr34g934XyzDH2x-eDgV3lDRAyDMi9L6rff3eet2F5uZrhIv9AMDrgQblyngpSKujX7PKt2qaMKxk6SXmEHR9GiMuC-S4qjzaF66XMxh_Y7FJolvgnixyMbeRvYotBGaxWeFyVeUpyKWNd10Ur0AxgRaiS_y0LQez9ogDa-97tfzjupH3RqhnTmBsptjmeibBmpXDUh3UsSss88_dHYqn4Ftko3ePk-EfUgCkiBQGxRWw9WEBe4D4NE6rXUwhx5nb9Ql5mkXqYfeRi5arVAIUIqI5iU3h5ur92ca-hZe_wXSe2VLfSj0qTVm3qzUO-9tc8IhnHkn-tWeQyeWMm1SpRw5iA7xX7YSL7WhZeFJaKelJ0=w972-h625-no)  

![](https://lh3.googleusercontent.com/sSEzNBk42rCmJcXc7Rroe3n03c64ULnFuFtriy5A_McYl9vMVzuVmZy-r14d7swK-DG3wo_T0MsjUecSNoRQlUEKIYFdhXxV9o_AFBbpqsRY1UZAwQJx95ORP7lqhQ9-6vBmagRATg4XRl2IsUIqN-ghnr1XqBySgmb39-fOeqMLkiv75V0aljhjrG-VIO5z9JfGcGe1jySgqGAkFHiwUG2W7UnSxRJ81GXv7JnGj8IuDkQC71yEAyjO4wrBIx-gaAK27OL9HRsP-sssjsMNfde02Y0CP_o1okfTiZWCyANI-euJA95byoZ4p-l2MrkLN5zeFNMtwalviK3MNK4I0M3VLBRBBIbcLPR5WPetRNQWa6rRSlhBqNDQ-Dc5lE1lx_qB_B6I1WqbWxUxLn8CFu9xn3ZcXsR9Tk5JMSnI9hW8f9Gc7VZKaWZNq_Ki62DdafKVtI101CEIvLC9qJ_MfzBXPzW2OpRuQD-fJJK5DPI94lup-1gyhYDqqKoKFdr43BVUvK-aL_F5P_wYM5SRu8NtT6DDookWBbIbHTae-6onaq1FKv5ZElKiHyWPXo75jviO1OkHBo-jqEXykRCDx72vCVLEupPswHIhDoeu8ixRkgaxG1-nrfn3RIE5dntjL7AzvvnsiOV-7ZO8lQCuKR_pAKnu2Zi2J6u3LWoB4MjG8kZ9-QAsN2IvOnGH=w972-h625-no)  

![](https://lh3.googleusercontent.com/LEdY0WmW7Pya2YBfowmKWMvljHAlFwfNfw2lw3GByuvo-uUrzFLjVXoNrLvkmCtvhRjT_YjkpQc7iseO048NcFroFV-CR0HtsbmqKQHL2kuL-cGK_iVLJEBjMX6NxcY_W-JieY-ujOTUDqTKZyCqN65x0BRPJrWBCdhMTiYGnnSJ70jSDHcbYMNbYaeufmvNodamnHf8Hpf9Lg7uUaUTd6tdaWhtR1e7hDWmp4Yl1qE6RbRJ43y-MOIxNhqyZb869JgId8qw8EQ8n1BMtzy4gdcZJa6rnfgvt1FmacNoDwWH6GoVmXVNlP_O961ubVj-hZSx6VnkqJg6XbZ6_BdPdpv25Ygf0EJhRdVPWpt5FS9s5GG8gC9EzuJbIJ1IiKface8_Wm15MmdiRXnniJleQOum7wOCU2UqA07rFKwIXxlRcuTK-mdno1TiKe0iJhw_xr7MqyOQScWe-rdf954-ekCUcJTLOJo3HnAQuhjcDO1Rii2qhyYugBv0KgE8TqaOkcu2wlMAzheyec35XmYJ29MvLgBmLC7bVGF1hA3SSdQDOd-c2T0ba8k54Xk4exzwBz-iAxkM0TyB_UmOfnlqJmKJveWbXyCzNSZJ3AT_wZ5vAZw1Q_P7IXOtLiJcDQOHJs2KVInIWhbv0HttJ__0iWlzxBlmUVm2k0JvmcPKrIbWQIOutUmX5DhdtadP=w972-h625-no)  

![](https://lh3.googleusercontent.com/1VAcsS_KB5yZFauv8_hS33o0gB-gWujLXESlyN_qs8KTHu8vlNwS-UCFjP9WeekSoxi8rwk2pF9BvupZa7B95TnEZGNUC61buW_J82c7v25DzwNhfjMVAvmX1-5qs_PSL_0guwe1JN8cN-tiQ1sXxsuTmQsEOoC0ptxUDWZcFt3Rn8w66RkRTxHHlpLf8h8hjmSSGn_FNcldVLcvwr-xppXTgGkNcDtGrquFkvjWxh2pjXJQ00Hs0SHUzYEqCpAxT98a6hb2zVGWcZiygPrwsHtPCI4oCj91Fp6U2pzHNzWYkw5hwQ42vv4CcBCtgx2EfehY128HhLetL-DQfFEJTTtLSuskP7SwSczEC3cLhhq2ZLDN4euTZeuel6Nk6vrCGZvsdDVmqPtR70TBZ90enevqUDN5paSwPS2dknveBM1UEmtroZ3ZyMcK7iuSwVmaB-fQYsFmvnbNz_-eJxeq1Hu5DGfWsqUulaUJ4RnvH3iE-jpofZua6rb5_HMolDGyK6sDA6fL1kvfBNTwcdZhPsewHOOPKFdfz1oNKd32eAPxXbqbxd1s8egj_bHKaY5d8PQfqm86rK1qRUgw_G40cohvZo_UVYOkm6YOSDh5-1H8u_dHhknnkLoXVV6QZGY5U1FfpNgQPjCMWyrh50pU7osIyROHbAob2mwe5Cir_hOPY3-skiK11_9tsyTd=w972-h625-no)  

![](https://lh3.googleusercontent.com/NaEybkRsYJqklLMQfRA4HNSXE8gW8p6bF2NEOYGMJwjA5eaAqxkUwAimcKu7TeLnDJk3PndpRRzw04LXX8O4enmueWotRzyri9G5cSwwnC46qvKO5v6IbWBtrVLxOAB61z_c2PIdPpzDzOfR_xI_IiPv6fM5cJOVg-DZpTNtAUTE6DBVXEyQJkKRKvm1yKlzWtkLOAaxqhGy4G2FNrp3ItPx5XlwjOCxb1QnCnmIrq1_vd2jQ1kECSZpKsZxpRPchVJXStY3EyUNSnFXzuC8TKbtPgXNA1uW_IRw2YYgyuQsHJusPN-E_Oh_VoBnsdrnb1LHLK7Djs9elfy3fhlLYAX0N32sP-ERpg3LaL2_Gb-sbxYTfC5hKHFI2R6rIeeueIz-bWv5CsdaWWxuy_MNTdIsjHvj6mi2Z44Bh7DWM5180MNf9SPP_HOExnYz-u0OidKUcUL8U9EvjLaDijS17PjwMy1S3Lj1rsJiNwLOXfj3hadXV7GxQoXBhmO-USLY_cZOQlzbPeXZFNLKYFLSPnMN8fadMOg2uRoiJ5X8qhovUuXlBx5g10LXuzb1cHvdKHQx8yNg8wT2ph1U3-QQJV_6BZ3WaB6SFzPPT8kW_hoW7zUdffV_u8XdO3PVnI4I_dLskGRw0T9sPK4kKbZ6bB37MZVHIBXtQANvTVYwEvP6zBKiwcQhMitSxJ3f=w972-h625-no)  

![](https://lh3.googleusercontent.com/LDWFJ3cGDnQK2ZldzGvFDKNvO1LHpt0DlBneuxE2aOTO_QfDu-3yCQ-iygJVS9gL_imLdF3oVkY2t0YcICQxvMMPQ-xWSKmjGdDCKDdFerrJRqvCm6QDcKCgDkkC8v6ycW_FcDyX9ltSEWBYCv7Rz1aJlvTIyOeJUOZ9A3AwjLqj-mVedv6xc7mobavEXfvTp4M1e4G6J6qNLBPIDC3wR6R8B7uIBaWV4tM5x2UyOA2cRICJfCoPQhRJGUIiFhbC6M337_px6iCydlGgxeGITO_K2wiSYAqn5oXZXudFJPAMWMNN0sSTDCa48EaU70EvUbXEjItdnb-LF1Ph4QwVpvA9Y3TrhGswBDvNskIYZFUht_wDM3w__sS3ixyYbA9yhtZAqkS73dKJ2Ulo9QwaX3ivU1B7Aatixms4jGS6H7DT_LFofi4f2cetLJzRRrc_2ErC-QDYpAyiqssrx4K3asYuEDk-Z4PsDAFBOcEe6kI4jETeJBtYnnNCL-KAY41GWgc6PteAyqOZ4s2o8ILi_D2PklTM1JdYBqgtJv9lT0m-TO_alCzwWg4FLKfDJjrFy7IggHLXxe0ACxT3YdwPFUdQBEBE6qksmUibLCu1R_LLqxp7hf4MwmXtebAS7Kmaqo609GObwQK9WlbzXCYSa3YY7V1gqyZ5xhWXA30GqAgASQB2ZTFyL2CQNss2=w972-h625-no)  

![](https://lh3.googleusercontent.com/i7qGc1P5c65rnfaqpy_IDgTY__ST-nbORjT8ZpAV_L3vxYUjFXDupJ0UqxdYT9Ltj5Ht7VD8Ylbm1tCafOq6QsYR8JuIDnaHD6Kk2kp-F3ahd273gUtyEMiZuXmdiytwV4xZ8vj7jR1HzqyKOvYtrRMEd5bc4d5np17KVlUFtm_jImuxqZmjgn1FCFMJ6U0CpD49kHz5qnwwxL9RDIT-_a2wf2his4YRL4tAW5rGetKD_y-860sPRV-h0KGHGz2259tYBNuutgC7XldPM3Czw06GM80Iq00mJFdXIUnV6XZbOUB5Ch-S-pLpsdzbdk0F9jLQ2Pm9TNG3zYp65mZrBsG2ndZaiDpXylkCtuGzEotUNQa_PdkYwCYKsiNcTbuRR0HmfoeQR7z-_34u1cx0rTYiOhk4Coib281ucUzWKAO4nMBP-8kdhdF2JqTNfedw5C9Ox2flU107m33_UnXTgcwU9YtMN8OnvN01LH6_5wB8zAFUZ5FjrRX0FMjU91-d8qAdEX78hzrbdDkvjlwm3O7--YZD67jphX8tD_ZmPkM1o5zSpa9AJMShrIFwVqwtt7SyBNWbojAf-F0w7yTfTo9vql8CflWTHCleMEyeKZa8np5VzQE7w2BOE0Y29q7WNMyk6G8luWNeUYke2mf7rtQcrlND37HsE7K3zcto5fFNuuDXVAjoz8ak-c7m=w972-h625-no)  

![](https://lh3.googleusercontent.com/RAyysn3-O0HJhIdKbOtsrgndEjSzeAXkZyby7yPmbvsApfkdQmOgwVpsVa8dokPXWhxfkqgWt60qZ7eu-QZ-ILHKhajXwH5zpheBuenxuREcLhatRBAONXQ-FXQqA2RIK1LiAdyFhQGqZCn9w7EbtTeWpzdwjT6r4CDFHon08G1Cn1zookOa7AGe_jrOgp3Px2eGVf_VfhdsoXaR_xXcNekTqEU9M4W2DWTHxlZjbe2qzKp833vQ-cGJFFGQa_UgLj1at1jylY2fGzvpsGcyO6V9VQvJNBFBgb3Wf8IYNvf7fNvBDroFRgD9f4RyEUhSr2Xt0l-7-09vBBphRfq-2tE2ifrj0tic4UWIRsoU2fEicbHpmoXVk0vobHj3FoqD3fYYF2VnNSUJbR0d6TSlCP3DE7Ke-I7V08C-ux1F-ALVV4uyhpB8xyEIAvCucIL3IzrRtTFT48XJMTvLJp656mqFC8-yE98LA9OZE63Rd4lP7QVzME7wW9KJxmIP_4S15e8t_GXhXJov5uxchBrYkFYfhy_TXWgSo4f6VQcWdN-Ijb3HQwFikonyDkqqni73w7rdVJBh50MPMwvH8Ey7wAS_964ktp-61s43QsfRY3wRhU5ff9HBlsOeCOoTOmUPWVZgQOaRzbLtOGVHeMxKMrgm5lUQMeJEhcr2BRb-j3L4qQgNzQ28znOGk4WO=w972-h625-no)  


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
## Problem 6: Image Stitching (30 points)

Due to unknown issues, image stitching could not be completed successfully. It appears that the images are warped to match the curvature of the panaroma, but they are just being overlain on top of each other. This is likely an issue with computing the homography martix, but I cannot identify where the error is occuring. I am estimating the homography matrix with RANSAC, the same code I used for part 5, so it should be working, but is not. The procedure applied to stich the images is almost identical to the tutorial The results of this exercise is as follows.  

![](https://lh3.googleusercontent.com/VJzvkUFHs8AQ9JIsv8lhVPivFI0qhcgxd3rlxIEiStLCPAVru1C20ZkBH8T6YqpTJgGD8V_FKsdl-uLMKWPRu2ZexD-FFf7lw01PH5t1XOl0fqb2PxQZxWeA3uji8fOp7lWN-nVqCQBfnoYh51xmRa_tVOeCYrYKFPb_1m85qVuQI85AKgrnwY1UEm4lq0yrzuAvl3ohBwFlxXu-LY_0pxT5Abmj2kHKfWqXnLEwXl2yi1TJ5bumM9pKRTuVuU6GVaZWZLfyob_kdmDx0qgvyOtLqd2QZIe7eEoww-d_iEOxzoD37fsLH-yKkQ7UwN8HOF8CC1Ymudz9bDk-levAfTr5nUjO_h8cEPxRAy2QRe4OUP8KNiJHbO4KBOf52AW176xRjziO8UD8H9PZpmYI1CMMj4GAeV27Tl8nzDYG-FpCm2F0CYoLF2-lQzVz3S49ZuhPLNcfqXgqIPRWTVDO1LpUTmpZExJIhdZbhwYYx8sCJ_JcJQNvomXTpsVr94sCClUyxOww_AGWDQ1I-alDLV6WIWpKUfVP-PC8Hx33lrHkcL6N-whhhcPHELeeoCKpMTQV_Qpb3xUfFYaPdYkQiKLU9qNze8-RcpL0hr56Iu6JbeZ4r48zaYxa7Y-T227s4cuNc9c71GHzLgyIfS22tRXIxT_OrQ1Dq5XruLTf4aA7lMP_eSJB_lDzCilJ=w748-h575-no)  

![](https://lh3.googleusercontent.com/lO_K4FwupLaatHRNICTFpPReWtulDcDzIKWprjjlB0f0ONgSy-nCL-GPArwCl0SK9z8EABAE1DL1YahnDZEyu3tGNbTHK5hbq2MtRYzuobR-JMFL1nkT1lJE-SIXfJEza7oZWl_LSNKbYXYwqmVS8XvlnYRhv5TglafNAB8eetmCq8jnor5Kh32yLCKS_H2YNsKI0WYRx4PIvHwimi-N-mCq-_Yz3yb2IWoiSPwvWOBVnIR7ANCY0XWVgfOfoVszZCxwuvokoZCzjqQ7vpozpKJfhvFvOGXo89TlDxR5x-CDITsw9vDs3lP7-InZcULCyiFhYDDPnWfqm0fL4FbDxSTqFOYNRVPIQKoT-ftMYp0hAcdMNwNkB95iKMKnjbI517vIT1197rUkoNMfyC74QV6lhuz30ZPZiz5gRWsDxDKg7n0t9BIPt5zpLn-ov4vQkNjzcthnqmvNOQmHfXej4SJpqvMJvUiOIK2R0FlwUb46Po9wmUkXogiPXGbul5fi_idiN5A9Hzw0BVMJpN7dXrMBwybeBPc7m-8-zu6-EgeIDY10xjtpZRUcIt-G2EmSZAkj7C9AZnUqKmtmycjZZphP5EO-Mn2FDeV_An42o1F53yT9YPYEwwURKDu1fyH1ZIxkb6QeespHfnqrmOcAQEjiRhnYshV5lWPbp-q2nTaV8xgH3pnN2uK1IPyX=w760-h625-no)  

```matlab
%% Load Images
panoImgFolder = 'PanoImgsTest';
panoImgList = dir('PanoImgsTest/*.jpg');
nPanoImgs = numel(panoImgList);

%% Read the first image from the image set
imgFirst = imread(fullfile(panoImgFolder, panoImgList(1).name));

%% SIFT the first image
imgFirstSIFT = single(rgb2gray(imgFirst));
[feature, descriptor] = vl_sift(imgFirstSIFT);

%% Initialize all homography matrix to identity matrix
H_all = zeros(3,3,nPanoImgs);
for ii = 1:nPanoImgs
   H_all(:,:,ii) = eye(3); 
end

%% Estimate the homography for the remaining images. The transformation of 
% I(n) into the panaroma image is the same as T(n)*T(n-1)...*T(1)
imgSize = zeros(nPanoImgs,2); %N*2 matrix to store images sizes
imgSize(1,:) = size(rgb2gray(imgFirst));

for n = 2:nPanoImgs
    n
    % store features and discriptors for previous features
    featurePrevious = feature;
    descriptorPrevious = descriptor;
    
    % load image
    imgN = imread(fullfile(panoImgFolder, panoImgList(n).name));
    
    % Save image size.
    imgSize(n,:) = size(rgb2gray(imgN));
    
    % SIFT image N
    imgNSIFT = single(rgb2gray(imgN));
    [feature, descriptor] = vl_sift(imgNSIFT);
    
    % Feature match between previous image and current image
    [matches, scores] = vl_ubcmatch(featurePrevious, feature, 2.5);
    
    % extract all the matches for future homography calculations
    imgCurrentPoints = [feature([1,2], matches(2,:)); ones(1,length(scores))]; 
    imgPreviousPoints = [featurePrevious([1,2], matches(1,:)); ones(1,length(scores))];
    
    %% RANSAC to iterations do determine homography matrix
    iter = 1000; % number of iterations
    threshold = 10; % threshold of inliers
    ratio = 0.5; % inlier ratio
    numPoints = length(matches); % number of total points
    numInliers = 0; % number of inliers
    H_ransac = sparse(3,3);
    
    for ii = 1:iter
        sel = randperm(numPoints, 4); % 4 random points
        imgCurrentFe = feature([1,2], matches(2,sel));
        imgPreviousFe = featurePrevious([1,2], matches(1,sel));
        
        %[imgCurrentFe, imgPreviousFe] = pointSort_p6(imgCurrentFe, imgPreviousFe); % sort in circular manner
        
        H = computeH_p6(imgCurrentFe, imgPreviousFe); % compute homography of the 4 random points
        
        testH = sparse(2,numPoints);
        for iiiii = 1:length(testH)
            tempPreviousH = H' * imgCurrentPoints(:,iiiii); %H*p
            testH(1,iiiii) = tempPreviousH(1)/tempPreviousH(3); % x value on previous image estimated by homography
            testH(2,iiiii) = tempPreviousH(2)/tempPreviousH(3); % y value "    "
        end
       
        % compute SSD
        dx = tempPreviousH(1,:)-imgPreviousPoints(1,:);
        dy = tempPreviousH(2,:)-imgPreviousPoints(2,:);
        inlier_temp = sum(dx.^2 + dy.^2 <= threshold.^2);
        
        % determine if homography is good
        if inlier_temp > numInliers
           numInliers = inlier_temp;
           H_ransac = H;
        end
    end
    H_all(:,:,n) = H_ransac*H_all(:,:,n-1); %T(n)*T(n-1)...*T(1)
    
end

%% Compute the output limits  for each transform
for ii = 1:nPanoImgs          
    [xlim(ii,:), ylim(ii,:)] = outputLimits(projective2d(H_all(:,:,ii)), [1 imgSize(ii,2)], [1 imgSize(ii,1)]);    
end

%% Determine the centre image
avgXLim = mean(xlim, 2);
[~, idx] = sort(avgXLim);
centerIdx = floor((nPanoImgs+1)/2);
centerImageIdx = idx(centerIdx);

%% Invert the H-matrix of centre image then muliply the inverse to all H-matrix
Hinv = inv(H_all(:,:,centerImageIdx));
for ii = 1:nPanoImgs
   H_all(:,:,ii) = H_all(:,:,ii)*Hinv; 
end

%% Initilize Panaroma
for ii = 1:nPanoImgs          
    [xlim(ii,:), ylim(ii,:)] = outputLimits(projective2d(H_all(:,:,ii)), [1 imgSize(ii,2)], [1 imgSize(ii,1)]);    
end

maxImageSize = max(imgSize);

% Find the minimum and maximum output limits 
xMin = min([1; xlim(:)]);
xMax = max([maxImageSize(2); xlim(:)]);

yMin = min([1; ylim(:)]);
yMax = max([maxImageSize(1); ylim(:)]);

% Width and height of panorama.
width  = round(xMax - xMin);
height = round(yMax - yMin);

% Initialize the "empty" panorama.
panorama = zeros([height width 3], 'like', imgN);

%% Create Panaroma
blender = vision.AlphaBlender('Operation', 'Binary mask', ...
    'MaskSource', 'Input port');  

% Create a 2-D spatial reference object defining the size of the panorama.
xLimits = [xMin xMax];
yLimits = [yMin yMax];
panoramaView = imref2d([height width], xLimits, yLimits);

% Create the panorama.
for ii = 1:nPanoImgs
    
    I = imread(fullfile(panoImgFolder, panoImgList(ii).name));   
   
    % Transform I into the panorama.
    warpedImage = imwarp(I, projective2d(H_all(:,:,ii)), 'OutputView', panoramaView);
                  
    % Generate a binary mask.    
    mask = imwarp(true(size(I,1),size(I,2)), projective2d(H_all(:,:,ii)), 'OutputView', panoramaView);
    
    % Overlay the warpedImage onto the panorama.
    panorama = step(blender, panorama, warpedImage, mask);
    figure(); imshow(warpedImage)
end

figure
imshow(panorama)

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
H = reshape(H,3,3);
end

```
