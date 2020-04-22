# Question 2

The output of the ```ComputeCe``` is noted below.  

image

The code my matlab code is as follows. Also included in the submission are the .m files.

```matlab
clc, clear all, close all

%% Define Parameters
nodes = [0 0;
    1 0;
    1 1;
    0 1];

c1 = 6; % "f" from student ID
c2 = 6; % "h" from student ID

Ce = ComputeCe(nodes, c1, c2);

function Ce = ComputeCe(nodes, c1, c2);
%ComputeCe for Cive422 final exam question 4

%% Initialize Parameters
Ce = 0;
syms z n

N = 1/4*[(1-z)*(1-n) (1+z)*(1-n) (1+z)*(1+n) (1-z)*(1+n)]; % shape functions
GN = 1/4*[n-1 1-n 1+n -n-1;
    z-1 -z-1 1+z 1-z];
J = GN*nodes;

%% Compute B-matrix
B = inv(J)*GN;

%% Compute Integrand
integrand = N'*[c1 c2]*B*det(J);

%% Evaluate Integral Using 2 point Gauss
W = 1; %Wi = Wj = 1
zeta = [-1/sqrt(3) 1/sqrt(3)];
eta = [-1/sqrt(3) 1/sqrt(3)];

for zz = 1:length(zeta)
    for nn = 1:length(eta)
        Ce = Ce + W*subs(integrand, [z n], [zeta(zz) eta(nn)]);
    end
end

disp('The Ce matrix is')
disp(simplify(Ce))
end
```
