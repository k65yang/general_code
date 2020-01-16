# Task1: Programming Practice

**Name:** Kai Yang

**Degree:** BA

**ID:** 20640696

## Problem 1 - Creating and Transforming Array

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

## Problem 2 - Bulls and Cows

```matlab
% Placeholder vectors to track the values of true and test case numbers
true_num_seq = zeros(1,10);
test_num1_seq = zeros(1,10);
test_num2_seq = zeros(1,10);

true_num_seq(true_num + 1) = 1;
test_num1_seq(test_num1 + 1) = 1;
test_num2_seq(test_num2 + 1) = 1;

% Compute number of bulls and cows
bull1 = sum(true_num == test_num1)
cow1 = sum(and(true_num_seq == 1, test_num1_seq == 1)) - bull1

bull2 = sum(true_num == test_num2)
cow2 = sum(and(true_num_seq == 1, test_num2_seq == 1)) - bull2

```

........


## Problem 6

### Q.001
