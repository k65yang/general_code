# Task 5 - Homography

**Name:** Kai Yang  
**Degree:** BA  
**ID:** 20640696  

## Problem 1: Homogeneous Coordinates

a) The intersection computed using algebra is [4.3714,2.5714].  

```matlab
line1_coeff = polyfit([3,5], [6,1], 1);
line2_coeff = polyfit([3,6], [-2,8], 1);

A = [-line1_coeff(1), 1; -line2_coeff(1),1];
b = [line1_coeff(2);line2_coeff(2)];

intersect = A\b
```

b) The intersection computed using homogeneous coordinates is [4.3714,2.5714].  

```matlab
l1 = cross([3,6,1]',[5,1,1]');
l2 = cross([3,-2,1]',[6,8,1]');
x = cross(l1,l2);

intersect = [x(1)/x(3); x(2)/x(3)]
```
