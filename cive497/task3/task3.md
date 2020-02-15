# Task 3 Signal Processing II  

## Problem 1: Convolution  

a) The analytic y(t) is as follows:  

![](https://latex.codecogs.com/gif.latex?y%28t%29%20%3D%20%5Cint_%7B-%5Cinfty%7D%5E%7B%5Cinfty%7Df%28t%29g%28t-%5Ctau%29d%5Ctau)  

b) The code is below. Figure outout is included as well.  

```matlab
% define functions
syms f(t) g(t)
f(t) = piecewise(abs(t) <= 3, 5, 0);
g(t) = piecewise(abs(t) <= 3, 2, 0); 

% create vector of x variables
ts = linspace(-10,10, 500); % 500 samples on domain [-10,10]

% create vector of y variables
y_conv = zeros(length(ts),1);

% Convolude using a for loop
for n = 1:length(ts)
    yshift = f(ts).*g(ts(n) - ts);
    y_conv(n) = 20/500 * trapz(yshift);
    n
end

% Output plots
plot(ts, y_conv, 'b-', 'linewidth', 2);
title('Convolution of f(t) and g(t)');
xlabel('t'); ylabel('y(t)');
grid on;
```

c) The code is below. Figure outout is included as well.  

```matlab
syms f(t) g(t)

f(t) = piecewise(abs(t) <= 3, 5, 0);
g(t) = piecewise(abs(t) <= 3, 2, 0); 

ts = linspace(-10,10, 500); % 500 samples on domain [-10,10]

f_vec = double(f(ts));
g_vec = double(g(ts));

y_conv = 20/500* conv(f_vec, g_vec)

% removing excess 0s
isEnd = false; 
while length(y_conv) > length(ts)
    if isEnd
        y_conv(1) = [];
        isEnd = false;
    else
        y_conv(end) = [];
        isEnd = true;
    end
end

plot(ts, y_conv)
```

## Problem 2: Convolution Theorem

a) The convolution theorm states that the convolution of two signals in one domain, is the pointwise multiplication in the other domain. In other words, the convolution in the time domain of two signals is the pointwise multiplication in the frequency domain and vice versa. Mathematical proof not attempted. 

b) The triangluar signal is the convolution of two box functions defined as the following.  

![](https://latex.codecogs.com/gif.latex?f%28t%29%20%3D%20%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%201%2C%20%26%7Ct%7C%5Cleq%200.5%20%5C%5C%200%2C%20%26%20otherwise%20%5Cend%7Bmatrix%7D%5Cright.)

The fourier transform of a box function is a sinc function (as noted during lectures), hence using the convolution theorm, the fourier transform of the original function can be written as follows.  

![](https://latex.codecogs.com/gif.latex?X%28t%29%20%3D%20F%28t%29*F%28t%29%20%3D%20sinc%5E%7B2%7D%28t%29)  

Code to compute the analytic and numberical solutions are as follows. 

## Problem 3: Discrete Fourier Transform

a) The following relationship indicates that the discrete fourier tranform of a signal is assumed to be repeating. In other words, the sampled signal Xs is the same as the summation of X(f) (ie. the frequency is the same).  

b) It is not possible to measure above the Nyquist frequency, however, that does not mean that problems are not there. The discrete fourier transform of the sampled signal will generate a frequency graph of all the signal measured below the Nyquist frequency. However, it will also include the effects of signals higher than the Nyquist frequency as distortions which wrap around and onto the sampled signal. 

## Problem 4: Discrete Fourier Transform 2

a) and b) The functions z1 and z2 are presented in the time and frequency domain in the following figures.  

c) Just by inspection, it is easily noted that the z2 frequency plot is much narrower than the z1 frequency plot. Possibly due to amplitude differences?

## Problem 5: Discrete Fourier Tranform 3

a) The code used to plot y1 in the time and frequency domain is as follows. The plot of y1 in the time domain is presented as well.  

```matlab
fs = 500;
t = 1:1/fs:3-1/fs;

a1 = 3;
a2 = 10;
a3 = 5;

y1 = a1*sin(2*pi*25*t) + a2*sin(2*pi*75*t) + a3*sin(2*pi*125*t);

nfft = length(y1); %length of domain signal
nfft2 = 2^nextpow2(nfft); % length of signal in power of 2
y1_ft = fft(y1,nfft2);
y1_ft = y1_ft(1:nfft2/2);
y1_ft = y1_ft/max(y1_ft);
ta = fs*(0:nfft2/2-1)/nfft2;

figure;
plot(t,y1, 'b-', 'linewidth', 2);
ylabel('amplitude'); xlabel('time');
title('Plot of y1 on time domain');

figure;
plot(ta,abs(y1_ft), 'b-', 'linewidth', 2);
ylabel('Normalized Amplitude'); xlabel('Frequency');
title('Plot of y1 on frequency domain');
```

b) The plot of y1 in the frequency domain is presented below. Note that the amplitudes do not match those prescribed in the original equation; a longer sampling time should result in fft displaying the correct amplitudes (as noted in the second figure).  

c) The code used to plot y2 in the time and frequency domain is as follows. The plot of y2 in the time domain is presented as well.  

```matlab
fs = 100;
t = 1:1/fs:3-1/fs;

a1 = 3;
a2 = 10;
a3 = 5;

y2 = a1*sin(2*pi*25*t) + a2*sin(2*pi*75*t) + a3*sin(2*pi*125*t);

nfft = length(y2); %length of domain signal
nfft2 = 2^nextpow2(nfft); % length of signal in power of 2
y2_ft = fft(y2,nfft2);
y2_ft = y2_ft(1:nfft2/2);
y2_ft = y2_ft/max(y2_ft);
ta = fs*(0:nfft2/2-1)/nfft2;

figure;
plot(t,y2, 'b-', 'linewidth', 2);
ylabel('amplitude'); xlabel('time');
title('Plot of y2 on time domain');

figure;
plot(ta,abs(y2_ft), 'b-', 'linewidth', 2);
ylabel('Normalized Amplitude'); xlabel('Frequency');
title('Plot of y2 on frequency domain');
```
d) The plot of y1 in the frequency domain is presented below.  

e) No, since the Nyquist frequency (50 Hz) is less than the some of the component signal frequencies, it is not possible to extract all the original frequencies even with a longer duration signal.  

f) No, the Nyquist frequency is not high enough to extract all the original frequencies.  

g) Yes, the Nyquist frequency is higher than the highest frequency in the original signal, so it is possible to extract all the frequency information.  

## Problem 6: Frequency Analysis

a) 
