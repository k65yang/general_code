# Problem 2

The outputs of the program as as follows. 

```matlab
function Problem2_submission()
%%  Description
%
%  Solves Assignment 4 Problem 2
%  One 6 node triangular element

clc, clear all, close all
%% Define Coordinates of the nodes
k = 2;
x1 = 0; x2 = 0.5; x3 = 0.5; x4 = (x1+x2)/2; x5 = (x2+x3)/2; x6 = (x3+x1)/2;
x = [x1; x2; x3; x4; x5; x6];
y1 =0; y2 = 0; y3 = 0.5; y4 = (y1+y2)/2; y5 = (y2+y3)/2; y6 = (y3+y1)/2;
y = [y1; y2; y3; y4; y5; y6];

%% Define quadrature points and weights
nq = 3;
G = [0.1666666666, 0.1666666666;
    0.6666666666, 0.1666666666;
    0.1666666666, 0.6666666666];
W = [0.1666666666, 0.1666666666, 0.1666666666];

%% Compute Ke using triangular quadrature.
Ke = zeros(6,6);

for i=1:nq
    zeta_1  = G(i,1);
    zeta_2  = G(i,2);
    w_i = W(i);
    [GN] = GetGN(zeta_1,zeta_2); 
    Je = GN*[x, y];
    invJ=inv(Je); 
    Be = invJ*GN; 
    Ke = Ke + Be'*k*Be*det(Je)*w_i;
end
disp('The conductance matrix is: ')
disp(Ke)

%% Compute Body Source Vector
%domain subjected to a constant heat source of s = 10 Wm-1
fe1=zeros(6,1);
s=10; % W
N = zeros(6,1); % empty N matrix to be popluated

for n = 1:nq %three point integration with degree of percision 2
    zeta_1  = G(i,1); % define zeta terms
    zeta_2  = G(i,2);
    zeta_3 = 1 - zeta_1 - zeta_2;
    w_i = W(i); % weight function
    [GN] = GetGN(zeta_1,zeta_2); 
    Je = GN*[x, y];
    Je_det = det(Je); %|Je|
    
    N(1)=zeta_1*(2*zeta_1-1);
    N(2)=zeta_2*(2*zeta_2-1);
    N(3)=zeta_3*(2*zeta_3-1);
    N(4)=4*zeta_1*zeta_2;
    N(5)=4*zeta_2*zeta_3;
    N(6)=4*zeta_1*zeta_3;
    
    fe1 = fe1 + w_i*Je_det*N;
end

% compute body source vector
fe1=N*s;

% add point load
fe1(1) = fe1(1) + 7;

%% Compute Boundary Flux Vector
%Two constant fluxes of 10W on edge AB and BC. Since fluxes are the same,
%no need to caluclate twice; simply calculate it once, then apply result to
%both edges

fe2=zeros(6,1);
qbar=[10 10 10]';
N=[];
[W,Q] = quadrature(2,'GAUSS',1);
nq = length(W); % number of quad point
dL=sqrt((x1-x3)^2+(y1-y3)^2);
fe=zeros(3,1);

for q=1:nq
    zi = Q(q); % quadrature point in parent coordinates
    dzdx = 2/dL; % jacobian of the transformation
    J = 1/(dzdx);   % inverse jacobian dx/dz
    N(1)=zi^2/2-zi/2 ;
    N(2)=1-zi^2 ;
    N(3)=zi^2/2+zi/2 ;
    fe =fe-N'*N*qbar*W(q)*J;
end

% apply flux along edge AB
fe2(1)=fe2(1)+fe(1);
fe2(6)=fe2(6)+fe(2);
fe2(3)=fe2(3)+fe(3);

% apply flux along edge BC
fe2(3)=fe2(3)+fe(1);
fe2(5)=fe2(5)+fe(2);
fe2(2)=fe2(2)+fe(3)

%% partition matrices
Fdofs=[3 5 6];
Edofs=[1 2 4];
KEF=Ke(Edofs,Fdofs);
KE=Ke(Edofs,Edofs);
KF=Ke(Fdofs,Fdofs);
ff=fe1(Fdofs)+fe2(Fdofs);
dE=[5 5 5]';

%solve for d
dF=KF^-1*(ff-KEF'*dE)

%solve for reactions
rE=KE*dE+KEF*dF

%check sum==0
sum(rE)+sum(ff)
end

%%
function [GN] = GetGN(z1,z2)


z3 = 1-z1-z2;
dN1dz1 = 4*z1-1;
dN2dz1 = 0;
dN3dz1 = 4*z1 + 4*z2 - 3;
dN4dz1 = 4*z2;
dN5dz1 = 4*z2*(-1);
dN6dz1 = 4 - 4*z2 - 8*z1;

dN1dz2 = 0;
dN2dz2 = 4*z2-1;
dN3dz2 = 4*z1 + 4*z2 - 3;
dN4dz2 = 4*z1;
dN5dz2 = 4 - 8*z2 - 4*z1;
dN6dz2 = 4*z1*(-1);


GN = [dN1dz1, dN2dz1, dN3dz1, dN4dz1, dN5dz1, dN6dz1;
    dN1dz2, dN2dz2, dN3dz2, dN4dz2, dN5dz2, dN6dz2 ];

end


```
