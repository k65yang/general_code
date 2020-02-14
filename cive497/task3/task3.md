# Task 3 Signal Processing II  

## Problem 1: Convolution  

a) The analytic y(t) is as follows:  

![](https://latex.codecogs.com/gif.latex?y%28t%29%20%3D%20%5Cint_%7B-%5Cinfty%7D%5E%7B%5Cinfty%7Df%28t%29g%28t-%5Ctau%29d%5Ctau)  

b) The code is below.  

```matlab

```

c) The code is below  

```matlab

```

## Problem 2: Convolution Theorem

## Problem 3: Discrete Fourier Transform

a) The following relationship indicates that the discrete fourier tranform of a signal is assumed to be repeating. In other words, the sampled signal Xs is the same as the summation of X(f) (ie. the frequency is the same).  

b) It is not possible to measure above the Nyquist frequency, however, that does not mean that problems are not there. Discrete fourier transform of the sampled signal will generate a frequency graph of all the signal measured below the Nyquist frequency. This does not mean that signals above the Nyquist frequency does not exist; they may exist, but will be distorted. Noted by the tips of the graphs, the frequency higher than Nyquist will wrap around and distort the sampled signal.  

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
