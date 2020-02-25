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

1[](https://latex.codecogs.com/gif.latex?%5Clarge%20H%5E%7B-1%5E%7BT%7D%7D%20%3D%20%5Cbegin%7Bbmatrix%7D%201%20%26%200%26%20-%5Cfrac%7Bl_%7B1%7D%7D%7Bl_%7B3%7D%7D%5C%5C%200%20%26%201%26%20-%5Cfrac%7Bl_%7B2%7D%7D%7Bl_%7B3%7D%7D%5C%5C%200%20%26%200%26%20-%5Cfrac%7B1%7D%7Bl_%7B3%7D%7D%20%5Cend%7Bbmatrix%7D)  

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
