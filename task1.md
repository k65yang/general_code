# Task1: Programming Practice

**Name:** Kai Yang

**Degree:** BA

**ID:** 20640696

## Problem 1

```matlab
% Create M1 matrix
consec = 1:64;
M1 = reshape(consec, [8,8]);

% Create M2 matrix
M2 = transpose(M1);

% Create M3 matrix
M3 = M1;
M3(1:4,1:4) = 1;

% Create M4 matrix
M4 = M1;
M4(4:5,4:5) = 0;

% Create M5 matrix
M5 = M1;
for ii = 1:2:7
    M5(ii:ii+1, ii:ii+1) = 1;
end

% Create M6 matrix
M6 = fliplr(M1);
for ii = 1:2:7
    M6(ii:ii+1, ii:ii+1) = 1;
end
M6 = fliplr(M6);

% Create M7 matrix
M7 = M1;
for ii = 1:2:7
    M7(ii:ii+1, ii:ii+1) = 0;
end

% Create M8 matrix
M8 = M1
M8_mask = zeros(8);
for ii = 1:2:7
    M8_mask(ii:ii+1, ii:ii+1) = 1;
end
M8(~M8_mask) = 100;

% Create M9 matrix
M9 = M8;
M9(find(M9==100)) = 0;
```

## Problem 2

```python
import numpy as np

a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"

```

........


## Problem 6

### Q.001
