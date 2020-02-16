# Task 3 Signal Processing II  

## Problem 1: Convolution  

a) The analytic y(t) is as follows. Full derivation not attempted.  

![](https://latex.codecogs.com/gif.latex?y%28t%29%20%3D%20%5Cint_%7B-%5Cinfty%7D%5E%7B%5Cinfty%7Df%28t%29g%28t-%5Ctau%29d%5Ctau)  

b) The code is below. Figure outout is included as well.  

![](https://lh3.googleusercontent.com/22GRKC9ycumJ19dUtHkDiNTMtTdde9uqtACKTXVSDR6lTC3vxc8Mc3ySSJbnwgQvYkoUMz6kmNN200uOIQ6CEo15JXJTpPvf7l2_cMD0VGoBg1Y89f_CrgsaJSQ6ac00VkN1P8rihlOUF9Y7TAMXYlAdQa5wYdLikl-IkoFg6JuArxKm1RwRJAI5vfHT6oQbD4k_0GVN2hIaz11_u6l2lhgK3X0vVXdoZuX3eLhx691a9TVxcWzu1kQDveGrZDlZHN0aPkJ4PBrVbBB0Mt2iovo6zPIB0YBQWt-u0Xsw2nOe95ZRxvlDqvk2Owiakf9xlNfWrp2ikJp3qQw8OwsYuxWzTgbud7fy2-YnJ0qwI5h_DMJIoXzZlrOwKYOScRpnMemQ8FDT5RJe04gbG499vIc3NhlEKgUM1c2jjB45HRJKHLV5Zv8sMNAO-0tBX_9SRGgR0hWW2FsMwMEaf9CjbmFQwuD-_p9MSHQeWIUZUg6Zp9Gl30K4mN3Z_kvUSfhXlk76TM5aaVdIrSWDnJKaCR2_t4bvG4oOSBW_-dKJ5sc-Y6jQ2sb022WdnJtZKGRJihOIR3j1NxioKbCVFJg9-YAW0Yf1V_B2JGB1W5YKdNCH5vMRyMRKuvNkM77S1FxKvfM4tIgXkq3pa7abs9ovjT9kilAQjyAu3peOS5I1fnhRZa8w2L6SWA=w560-h420-no)  

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
![](https://lh3.googleusercontent.com/22GRKC9ycumJ19dUtHkDiNTMtTdde9uqtACKTXVSDR6lTC3vxc8Mc3ySSJbnwgQvYkoUMz6kmNN200uOIQ6CEo15JXJTpPvf7l2_cMD0VGoBg1Y89f_CrgsaJSQ6ac00VkN1P8rihlOUF9Y7TAMXYlAdQa5wYdLikl-IkoFg6JuArxKm1RwRJAI5vfHT6oQbD4k_0GVN2hIaz11_u6l2lhgK3X0vVXdoZuX3eLhx691a9TVxcWzu1kQDveGrZDlZHN0aPkJ4PBrVbBB0Mt2iovo6zPIB0YBQWt-u0Xsw2nOe95ZRxvlDqvk2Owiakf9xlNfWrp2ikJp3qQw8OwsYuxWzTgbud7fy2-YnJ0qwI5h_DMJIoXzZlrOwKYOScRpnMemQ8FDT5RJe04gbG499vIc3NhlEKgUM1c2jjB45HRJKHLV5Zv8sMNAO-0tBX_9SRGgR0hWW2FsMwMEaf9CjbmFQwuD-_p9MSHQeWIUZUg6Zp9Gl30K4mN3Z_kvUSfhXlk76TM5aaVdIrSWDnJKaCR2_t4bvG4oOSBW_-dKJ5sc-Y6jQ2sb022WdnJtZKGRJihOIR3j1NxioKbCVFJg9-YAW0Yf1V_B2JGB1W5YKdNCH5vMRyMRKuvNkM77S1FxKvfM4tIgXkq3pa7abs9ovjT9kilAQjyAu3peOS5I1fnhRZa8w2L6SWA=w560-h420-no)  

c) The code is below. Generated figure is identical to the one presented in part b.

```matlab
syms f(t) g(t)

f(t) = piecewise(abs(t) <= 3, 5, 0);
g(t) = piecewise(abs(t) <= 3, 2, 0); 

ts = linspace(-10,10, 500); % 500 samples on domain [-10,10]

f_vec = double(f(ts));
g_vec = double(g(ts));

y_conv = 20/500* conv(f_vec, g_vec)

% removing excess 0s as a result of convolution
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

```matlab
% Plot function analytically
tri_pulse = @(t) sinc(t).*sinc(t);
ta = linspace(-1, 1);
y = tri_pulse(ta);

figure;
plot(ta, y, 'b-', 'linewidth', 2)
ylabel('Amplitude'); xlabel('Frequency');
title('Analytical plot of triangluar pluse on frequency domain');

% Plot function numberically
syms x
f = triangularPulse(x);
f_FT = abs(fourier(f)); % evaluates the numberical solution to the fourier transform

figure
fplot(f_FT, [-1,1], 'b-', 'linewidth', 2)
ylabel('Amplitude'); xlabel('Frequency');
title('Numberical plot of triangluar pluse on frequency domain');
```
![](https://lh3.googleusercontent.com/RlrP02iX1yPleAsaCwFeu4Vd6cFDrA2QS61y0zBigNlgn_gw2SO1yVXL9nn10fKwW-PcLJSF73maM9CZuafdVUUSof4dRbW6jGKZ6SXfUkNVlyZ0DWh441dXoDCYKglcuuAJey8Fp7jsl9sGWyaUrGh3wcBv9EaS1pJtekded5k5zAdi4GBfCtXMrOMbbDUrx_-Vy_sC5mCbX8SV8CXdB9L6Q20gmrH-FS-gGFHoXgIAmNtgMO5sg0Dz4RrGc2UUrA_LWQk5P-92lzlTI96lB25JZwWcKt_VNupnNwLeCHdnr6cNJFRdbi26ipAGIMkWBricK9vlupbeF1BGdGXPsQ_caAple9jNMx74lzh_f5q-h0VXo_Ouzxg39aSWy1jMtEY-VySbRMsK-FJkvh67CGSCn4C1Fvw_HI5qMQcOrNNkh14cnVh-VppfTITOv9ieHKkR7k410S5xf1tK924JPSq5MUR6zXtR2gh8RBFNYw3Fnyi5P8bM6-8OEbNI_xJ9VFbQ6lT0vfmEDn_uEbTnc_oBMQI7qpnl9XI4cws5rOE98IPM04GzS1O0F0wkHNAU3mvJEjhmgFj58wX82ukc0-mGkq4-xzX4XasimQ80nVm0VIIfBgaxFDetCAKnss-DiQxn4FSNoOSPOZVypyOS9oRm2u2vTR9_aLBlAd-ZZaCmyCK4It0wsA=w560-h420-no)  

![](https://lh3.googleusercontent.com/u6KJud2eD9LswoH6wTRO-7kEwTvdOm_3mxlN3_SQXG7cwfWz3sFW8O_TUm6tOpJ9Lm4jJNDKh9VpT9jjXPU1intvAqS6Qjvpy9xqfJ8XIbUzV6PREPplgM-7zfXA86ok013ZPQFPCMVd21K-qNjmv9tEIu5-lR9euvEHb6ulevxsbv8zG8zhVQiK0Zo5QJHtHHT-3EfPP7yKuFLiKDEpCX6TzpFwNUgn2Vt0U-fd2fcl5GQtUopQOCJekHJtO_HBFQm0JnQXbuiZMlatP8GSGZoXXivYwNPgaZY3cuUnfhC6TSMLsRHrf9Hyw-CK0ZJMFsSIgSsYVxXZYNRbePbxvHEAwKBTmrCB7DlwRlYXHt6idJq0i8vguUiGbWyf0QAUiQW2CSBhKj4LkEwKXM83SfOlXF3_PZQrIYJ2aI-Idlx2EpvrNqUvknmABn6K1VD4F2XVDHG52kpZIi2Fy1FoQ6UH1Wtqb3g6RPfIfg4S6dZibwXpAQS4bRa0iO6DhWgfhODNBoGElkliy7cfBcsyTp5XlsqCWJ_Y6VD4U2aDUxccCYiJwXOH8ZyB1x_VgPFYX-2jblOMjD91VAXGz3MFguJpK9fn6AeIqd6HAN8ywgUDWuLF1D18KkghdKLnDmopYrjHmKotJrCNQ4bolVFVzxwaKrEYMQ4xn9bWCF3Ko7OiYLaSYSmBig=w560-h420-no)  

c) A triangluar function is the same as a convolution of 2 box functions.  

## Problem 3: Discrete Fourier Transform

a) The following relationship indicates that the discrete fourier tranform of a signal is assumed to be repeating. In other words, the sampled signal Xs is the same as the summation of X(f) (ie. the frequency is the same). Additionally, because the signal is repeating, the frequency will be the same at every r/Δ interval.  

b) It is not possible to measure above the Nyquist frequency, however, that does not mean that problems are not there. The discrete fourier transform of the sampled signal will generate a frequency graph of all the signal measured below the Nyquist frequency. However, it will also include the effects of signals higher than the Nyquist frequency as distortions which wrap around and onto the sampled signal. 

## Problem 4: Discrete Fourier Transform 2

a) and b) The functions z1 and z2 are presented in the time and frequency domain in the following figures.  

![](https://lh3.googleusercontent.com/D9HaKerf0gOa1t5ewpR97hT2yzThnscAqoCEKRtbjyxYD84v5cg_-B4V3VkRkp23YBTg2jWouOdmrzs_Wz4Y12YPTY1yYIQDxQQpnVrrgImDGVvWuQQyLUiaTQlqh73EQxhzTTCxUgnqHB3P-SIF3OzlrpC81X5Qc2jmbYFMR8djQA17-7maoq5IsPOjFdLhvs5djhDlc5KFi9I_IEQg1so19PWLmy-wJQC3n3cXuV2hbatfkVKdXjxnnaUD2PzhAMYy74wgqariLBknNApiA0cv8Rk--nYWkUXfcORZN_D8aqXwPJW3p1TJhrW5w1whkso0Xjuhe4UtZgwqeFFOg9PhpUWD4tcIGVUx7zPkdTFu48xbXhhE1OEIufyRRpxh2I43CtTCOaOW5zoNaUtNYQTH1Tpi0sl1wZeimRejQmW21ZgcekAvOBE6J4gSNwaB4QWyrozwUXmYKvvgkDNCtMpoGILnEmZq05Yg8ls8ASxF6ecpiGocadp3CphkWUGUSe6vU7Z6UQbfarhdjx3OjeiC849k4zVCo0kAQBw97TdsbxkrOxqYphj-E18w9qJ8HMEsuaAKa5CFtGspH4EVUtOyaR2ON4kTnU3t_18XE_LDI-BiLO9C_PXALIeGfVUkDkkBTOGj0GUMrSmy9I5KCgP3aT4RigflzeZqHj-PGvOgR4iHe9TTQw=w560-h420-no)  

![](https://lh3.googleusercontent.com/VoXd3-r3z_e0doh5UvDZuoNI1dzvO3pcHajf27xxVyVqnjnzFaQmasvB0Dvnp6U_UY5RZsY-vSSx2kHdyRWiWGAatAsTW_1pjb0xofIpgEGMP-UYWJY-NlhWFYz9VZc5-Yk3j1Mba0Rg4sbKs6SfPvksh1ySjPJ8cHTurg6RevowAH_oHBPj2N-n6miEl1FR5UJzS4Jg1WyW70cttQxXRTSf_P7RfgziTAQQi81sOszPm_i7LFAyrbi-qkUCHHorraG-ku5ajJGTHLWF1vMjUXjymJKKqrk8jdZVojuuYdvaH-SQhjTCcUoapF-nBsLEzDZ5S5XeXao-TIvYRniKFWOv8sBtyzpmCjwixh43zNfTqH8EVsClmjZAuBzN0rZ6w23TmcfqN5q9VoyxlrTttuD5-W4A4-iKZDqAUYzV1NjlduhhhBgRhM0CtACHGXzmpsr8dHsvBMBz2HNdHjErQ1Rmg-usn72HBVmnbDVVnYssqWRV0-qouVGacwx0sSReUuDaJISBw7vPAk2OxUm7YKqrUKyLp7AdXFyFZaZBH-Qi6mi3Z-CJ1r924utIZqOe7NTocNDc8RIIlze58pojuPtQ63qe03pKYQoZdzk3vP0Wt694Jz9vWrrhD65PRk-JdDvsz0tfMr-PY90A-Xjni7YNgJBEiHdKgC4A619fedm97unhjLPNLw=w560-h420-no)  

```matlab
a1 = 2;
b1 = 2;
c1 = 6;
f1_1 = 3;
f2_1= 6;

fs = 50;
t = 1:1/fs:5-1/fs;

z1 = exp(-a1*abs(t)).*(b1*cos(2*pi*f1_1*t)+c1*cos(2*pi*f2_1*t));

nfft = length(z1); %length of domain signal
nfft2 = 2^nextpow2(nfft); % length of signal in power of 2
z1_ft = fft(z1,nfft2);
z1_ft = z1_ft(1:nfft2/2);
z1_ft = z1_ft/max(z1_ft);
ta = fs*(0:nfft2/2-1)/nfft2;

figure;
subplot(2,1,1)
plot(t,z1, 'b-', 'linewidth', 2);
ylabel('amplitude'); xlabel('time');
title('Plot of z1 on time domain');

subplot(2,1,2)
plot(ta,abs(z1_ft), 'b-', 'linewidth', 2);
ylabel('Normalized Amplitude'); xlabel('Frequency');
title('Plot of z1 on frequency domain');

a2 = 0.3;
b2 = 10;
c2 = 3;
f1_2 = 5;
f2_2= 8;

z2 = exp(-a2*abs(t)).*(b2*cos(2*pi*f1_2*t)+c2*cos(2*pi*f2_2*t));

nfft_z2 = length(z2);
nfft2_z2 = 2^nextpow2(nfft_z2);
z2_ft = fft(z2);
z2_ft = z2_ft(1:nfft2_z2/2);
z2_ft = z2_ft/max(z2_ft);
ta_z2 = fs*(0:nfft2_z2/2-1)/nfft2_z2;

figure;
subplot(2,1,1)
plot(t,z2, 'b-', 'linewidth', 2);
ylabel('amplitude'); xlabel('time');
title('Plot of z2 on time domain');

subplot(2,1,2)
plot(ta_z2,abs(z2_ft), 'b-', 'linewidth', 2);
ylabel('Normalized Amplitude'); xlabel('Frequency');
title('Plot of z2 on frequency domain');
```

c) Just by inspection, it is easily noted that the z2 frequency plot is much narrower than the z1 frequency plot. I believe this is due to a difference of scales. The amplitude values was shown as the normalized amplitudes, meaning that all amplitude values have been divided against the highest amplitude value. Y2 has higher amplitudes meaning that the peak would be higher than y1. A higher peak would make the smearing of the frequency less obvious resulting in the thinner look of z2. 

## Problem 5: Discrete Fourier Tranform 3

a) The code used to plot y1 in the time and frequency domain is as follows. The plot of y1 in the time domain is presented as well.  

![](https://lh3.googleusercontent.com/JTqrtiElbkDSeyPn2gL_YftG-LBIfUjinmrw3Jm-kfOzpK2VYEhSejr2LUAeWBy9RSC3KP8T0Bec2yujzc1NhHr7LhLdMa-4Z5wzNxnSdorwSem9ypTyTUwVlqP29T6N-Ef7s0bClhcCNAXNQOYqIgRHedNZ6lGNJu5Bw4KRVp5kAv79xW0hAARWgVvc3vyIm9kNn01JlpLl3YReqjg_1znYah6KcKH8mGj1X5EPBXTO7x54rCKl75WhUH_kzj05SyXlvT7G9xlpwGdygJbFGskpXmIjy1-1cER3Lsv8030FTX5Wk0Va317FTAYznZtoOlt7Vd-x9hBkoZxxyGGUbs_t1eR_KYEtYmyFCiErqLsRhtdbfQf4Mr6YqLK4lgWNye47ZNVFOqjYWSgsFY9gJT7fMFF7EgTREXgAbkpCKen4GLit_m6wjQPDq7sqMDCQQrOIUW4taC6duCiu4MxiuukS8DHHI5TKMO817QvhOS2CC0do6SMGjLIsQ4n4_ae-zTgupzxUz_LmcDyYgSTysxF6-E7CWdMqd8i5ThObDIGDEfRioSLUHYI2XsvhdVlfb3h8tuhFsBXzTZgcMEdkQoDkOZ_JNrQnlJgRzuYSkNre79obOntiuaD2aimxK0IyW5tLn5Fb0jOIbOuqGQ_ndKp4Cwp3oCCYHiYXPfGOecPgFq3eK7xrpg=w560-h420-no)  

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

b) The plot of y1 in the frequency domain is presented below.  

![](https://lh3.googleusercontent.com/o9vDBM_va5RUG1OpbX5W6LhaCbCzFjyUeXF-aRu9QxF19ZeljzuVIXJ6CeexZtCCPWAtWATzDVUuOTllU24PvpsCVkHpI8nuR-h4BwIgOL_drB3AknntRYSsVzty0ExQBcmPO68LWb0TyNvlW5D7dkvFyznf545MiZ-OaIavxO17OmJi2NWbiW0qmStmr4b5IK8tFwl-6uPj8fNEwCctxaUiUEybArQ3jdEnp0aNpoVBjrytrYcxh8rHKe54kQWDEiRqYX8EEfrxSlSyTv8JzS5VJimyH0HVB0OnDaPZGTQJejscXgX5NbvQGqUHXgeNcGE7LSEJtOR7PdI-o8lakgO9q0Hb9lWfrvO4cjM85SnWU1yrAqJUuXb6dNITljZfhrNs4zcmUohTktfmj05CiDgsDw-0Us32XtIlLdWy3OmxvWnNhhkF6KeNsmoUNtlcLPdMqXQ7hb7L-Cvb5nd_QwRgsJFevgCb6ZtSWtBLARmmHUeJA_HcSh0JZ5wrIasdv0oS9nkdsevywOHYzWSu00UYVFMYQ-wGfvssZP-7Vw3cNH1BsN_sGrPN3J2WcK216vrjRRyxZtcDecJXxooXnS4XktZBG-3JKuj-0-P-z6FwM4xpXvtTRIoODhUaPHwXWv7ODyYxdPc1jjNy3VbX1J-t49gTh5nnFyTR-U53E3Fk5b_AkyA83A=w560-h420-no)  

c) The code used to plot y2 in the time and frequency domain is as follows. The plot of y2 in the time domain is presented as well.  

![](https://lh3.googleusercontent.com/b18P_HiLj_mlGs8uO6NRz4kMWMFgvYKmRdLptTtNcgq6-8djeXNyxvEFv9xRYDPXqMHapF8qGNKZu7JatWI3BS1EzCojQ6CqmAnBcaPVAG0GwF9GVJeBtoJARozsMFt6HPiYPFqpGancgUB2X8nj1upKWDnRAzC1mDE68CXjdEPNcRezXK2VyNi5IQlZs_-l74OgZNxzALG74hVFI559dU4Wlvtgbz9WVHp1HMg5OUZGw78QvQx4Qp1IQudprNLNpKHBcjDruipBk0lCP0yEknCrZ1-FACUxvXAJOTJZcc7BVz0weibF9V8epApeGjGm69TE0O8pjrQPy0Zd-BgBPNgrPQG7vod8sLbLycpUTxdWl5geT-pANWSU_Qyb-2kk4_sZe42UiNEBRF3Pijge0vqScJoo0u3JPf75DHgIg30W0XaKw6PxV723yD8KVd6yeiMmQjzXIq6fs27mfgbfRB9peqw3JdAvmA8wybIljSBhE6zgvGi0hH34p9FxOQMDjtDROX1Udk0LGjC_IOOsRpe_zz6s--CgRrM1xChY7RUG8j5JHa4VgdHx_V5SLLU4t7meavQBJzYBrLDaJ7hE__K6jbwRJRXco-oEwIHkax9unAXlI2gBKOL0eJ9FELFXQJjP--x-uidVIK7Y--C9Bv7q5OkBlWuycKNNgf2p7H67NbvXcQ6_WA=w560-h420-no)  

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

![](https://lh3.googleusercontent.com/IEgoKbqwTDgG37auOVIbKQJYqlP8vZ_PKsXCb6CV0i-1MGCO5QbsVJvK76CaD0MEPQnGlXg5r_elSXIVAtSQLZU4b85EIrgGimMsATeewHxduW4V25XvB9Gf88yqcW4mn0CjOxqqop5eRnfC9pdOXD_fTdeklrXeQcG-erx8-ukqTrgVNuCYR6Wd1CrQ3paTGPy6posryQprMeFKz71g4xZXhecXRfWu1735kgh97y5Wuj8GIgVrZ3a90cLJTgKPlQAkdMGozcY0HpgCB5fY5nuGv-dmxl-eBz-shFY3SBJACHK5s4suD-7F9KGLLTbU186osZWgEHkj2-yUn0C8JjNAqvtwbtd0kYqLDMRVAWjIqRe6a48lPyicdsmlTjgz5U4xBduAmtH7Yodw7hCdglgOPO94I3Re4KbhJuCamX-v_ZPsliW4B--5_WjadXw5DHZXbc6OiMLbDI3leZ2GtdTJLgGYXBos-hf2knK6d0f3AyoVjzdcx6J9ggIJPIXyte97GMcrI8a6n6Z3pb6PZVa7CxfPXEZpg_KwUOo6V_CeATJE5AIvefqxI306TAoECIAcvKiYBFoww8T-n7HWGRJNIMwnwJSt59DnE8F61B5i9aUiR-FZR0DiuwzkA8jtGLE0SJfTK2zQFoSSNlERbOU1StXQUoEwgTnq4hxVPrOpgsPfFSQ2MA=w560-h420-no)  

e) No, since the Nyquist frequency (50 Hz) is less than the some of the component signal frequencies, it is not possible to extract all the original frequencies even with a longer duration signal.  

f) No, the Nyquist frequency is not high enough to extract all the original frequencies.  

g) Yes, the Nyquist frequency is higher than the highest frequency in the original signal, so it is possible to extract all the frequency information.  

## Problem 6: Frequency Analysis

a) The main frequency is approximately 2 Hz.  

![](https://lh3.googleusercontent.com/7cEsWcYYTivyil71A5yKHVMf5VnthPNp2znVEM7FTufLA-TRvng1QIXVgk_omrnFnggo9nnCZYRqxUbOcky7VUoRS8jUSd2Irevu1PJnhpJFwqVGviTlRVmb0kHkSoFhmMWAVQ-66WSGp6Zkbr_zI61FWK4BDUyX9Zes1imkEKHlgMzpsiJ8n7bQi1MwYTw70gOQogULxtXVWubBeV5cQJcplIhZMviYNvRzmBSVfMbX3EO-9Wk3N_rhYBykoVUlodK4CVwDOcj1_jIwVceKJ0DFDZVVXRKUktu2GOBOQKf_JYFELzDgEWeQmseeAQo0GATGdE-F8tapjyZlFndxM1onxn82HXLqY7R9hWtbMXPwu4D0hxlSsqaTPGTWdUgM7tdKpgyFEn-cmfhrpGGuvkkEPRkeiD7Lqoe3AWlCH1qt_ywmr6HEobcPChKL-xG8Ok_0fVChQ6CO5C2-fLWVcPq8xnbSBXMdLuHJXMPGjiR-t3LnFXNnGPuVv5pW5WP_OuxhlANkvsLNA2TS9J3Suod3UXzUqOkRukjw3sFDK9U--a_kQYdCw-TdI3mS_q9cM3GtzzKFy3GMwpwnGz7hjxXtamB84f5BzoINxum4gOEO2rYpyqtbpWcSHUuhKygA__dgVT61Re2t8DZEmI9xKyMJuLrgLhT04R5pFMFqyYQ0wLQ2JDUmpg=w560-h420-no)  

![](https://lh3.googleusercontent.com/_X5d0SEAXrQsXMpvoVYlHFD59f9tOxlyvoEgfHLr0-IaB5QZbSTRXzk0t3mwXRpAfXhKt_UmlFSTAs02qp_52J6meog_ubIZ5O_4IwLQnm2G6p2SJ9veaI7OWRl5Kgxty2xyUzAkhhySEoFxM9XvlMmieuUKHrNez5NDFGeHBxDES2wjbRxg7It6yhDLgwMFagjbtwbe0qgg40fr0RMiFDHrbwSi9IRkFyy0elT5Ku-DR9kJHrQL6Tp24r6k-N3OmFM9fLcwqWvvxcQ7iUPlM7s9tTAhoSGra1SxCqcUJ_9N3GevZj7bdxIGcmc731IlSptfPoe9_g_aZifvyNbVhtxmLdSl0nRKDRqxNUbAZ0DhAeTzeFpqSpkgFtT_KWmqsRdpSdwSjWMb9p-KfpIXkH8OMJUBEMOTYUu79kvJAT5Yc6pqLMmjqP7y18uSWl_7To6fIrlisd89L9DdZ7_rZnWqifuKMwzaT9wD1_qcseFNvEf9ixEFe8kqkPv04qL0POhTnHnnaPi89MZ6T-OgzcldkYMqD9tzLEM2SQRvrVQpCR8Adbl_QjZkG5UbNjr9ZdOCBYkyHK4pj_WrIdNPBIzbeHAgvvlzBnSV9GWeBk5LCMzDcANV-SMYp_xXacrNVjITkTQ2kG4n0ScW2IZJHYYd-HEV4O7O0vJVXLIHF7cgcoTr4GnYiw=w560-h420-no)  

b) The main frequency is approximately 1.5 Hz.  

![](https://lh3.googleusercontent.com/mR_kPopoAzqXsAYnwmjh1Z1J-m8s68HPZQx9onn0foawKUjN-WoFrIhTExbPtzz05KvgdR8rm4wwnNYdmsybyITXaL4XWG55ppA2402YtPJsdw-5Sil4I5Pc6oSsFgYidlHZ8-MCs3U7lvB_GlzP7dlptrGBg8ioHuEHoczjOwJlfT3dBbZ-bvYsMDYQPBuv-TbEJQIqVPXyAfA5ikCCB3isxG8RDf9mjQystsYJCRy3152_TMq-tj6vbV74eX-dHqUmvcbkn9Iz5Ltv0o2sI-mQGpnZ65_AYSvu8djdh8wsGUAe3rWaV5LGJteSoXSmkqiJlut_6RJ_E-iXQkwejxfcWH2Wn1UPXYTtD16wlw7I6HimQFNGj-H8qTBujDxCuioX9MfY0D-TiytZeh_iDDSrDmuz3R47p_AJo-mLSnW-wEnMOywGLN4q9iSOsRSf2OPw8mGgVglXDyi8jEwidMyLTYkHA0NbZ9n-TTDmTUQiDIkPtECtlF4-X6V7JzLuv0XmCguVu5sJyNnP6TG3vr6j1HXcdMPVQUuYzcp-myC5hNTPGZPjCBbM9eGfekNyKkNPSBkqol557-wo8jaNu0WBuiJavKS7gZHqpHEkRQ2ikV55umyClzc125oLgYC1ZbGPFnzvI_yKCJCiphWJCSin7_Vslfu9psaWvNMEYocT68ND3wnHPA=w560-h420-no)  

![](https://lh3.googleusercontent.com/_dvQ0YfnQ0H95B_WGHTIUzVhfEyUhgnyY06Qq2-mP0ks3dC_9v370_YzqbyTsO3ocAeU0iz9YRqDWvMxXzrvMn0u9cfhfFiygNfKKs1QMBDDs7_yBkkbRbH980fc5cx-CThsKHPqO0O1jJN447k8mwDinI99nhmYeFCcGIzjLuM0Na5X4e_15jVROZYj_sKPNfg4d6RGpf4Fo6nSCkEq0-d7wgWdH0ztTLNlqzT5n4c7kd8W3imdII5G4uZ0I8Owg4Iz330FTF6XLg_zHb5ndaGINFwUGiYIiz-So9NDUzSdlsMuw0EACNMtc3elkYRFPkxu0jz-uy2kNBZViDRlXzD7dEa4ppYdCDSal3vottcCo-0PXH3U-cxycS1Mxw1Eaz6GsD-R-KXviYCN6hrSohhh7awm9NKL66dJE7sjfePT_IpAUIBe9ZsLdCsBSXNlC39kC2pPzQylHOE0twwM0d5eEHZUNM-eCPLPratrmfmLsTul0S0S22bqrZu5Zx1ShOiUTzXZAtdBBF4suHJ_cw5JfvKRfSDKKPpfsEkRMY-UIZ1EoP9AhrHzvGX6nlPtA0UIz3O4hfkMArLYcT_SZ1O9Ufbv0xGCvdr7hxp6KDlBghKaTftrYR73lTzKQ_ADQk-0EgVzVhDjeYqqUIb2za-oo4MaHHG3Vaaub4uk7x5S2x4x_nlJcQ=w560-h420-no)  
