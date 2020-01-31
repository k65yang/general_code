# Task 2  

## Problem 1 - Sampling
a) A discrete signal is comprised of specific values corresponding to specific timestamps. It is the sampled values of a continous signal. At all other intervals which was not sampled, the discrete signal has no data, hence its name of being "discrete". A continous signal is one that is continous and has values defined for the entire time domain.  

b) Plot of 6 Hz continous sine wave is below.  
![test](https://lh3.googleusercontent.com/6xQEzCnyXJU3RLDocwNuSLuZ8rSzVYG2i0TmoeU19bclHtWJd0PDt_YqHshj7m4oy26kly-JNktLJe7TUtLlR-jABsxFf8aLTfM_8PPny136C7reV-RYw7CIaNf_sD7iVWOSi-F9_xMzQLcwrSns_wsKLMMjaA3S_8YwlefVHw48trkPIsTuqoBpPWI09fks5GkBe6Zoi6rIUUg3CzeJMfaeltrvYVQQZx1rg9_qLtQLy2oCU3QJvguD1sA92JvDXpV5I2U-G2uHw6fTKET-x3iuzHE5T7-dGj-xVdxIDAx7SXAYmJLr9WMZZVdpDWCwx0216Fl073XBQnixAeaJtC2MSUM1DLdKikGy7yamP6ZNhmjtTntEoaBTwzqttHHdyTR-FABsB97GQfpj5jbGtTEy4V-zh04qiJhi214k7PLzScJDEDGrvMa8gbffk7uHW8KeKGSawdt9nwRcYeVefRe0CpSx844ELRbA9QZdvlJbhzgrwgIUJFdm0Dyc4Mux4Qop2OjsHaRkliapmJf-gK8i8qR2LdrYNncOUNOqQeBvksQfL51G31qJerTYhj3e3F55KS44Po9hg3d8-AKms-9JJm0EURSGO8bEMovthrrfujeIDhnpJfhdWIrDv2TTG8XEAOtgpdwMagU3xRdW6PDgkv8p9xs40VDW-yly-YeaQtNrQz9JSvLi5qmsLc82sXC6NzEcu669_wFH6t6pX1rCZY4c3XbW2mItUueldS_WcGc=w323-h137-no)

c) Plot of 3 Hz sine wave with sampling frequency of 10 Hz is below.  

d) Plot of 6 Hz sine wave with sampling frequency of 11 Hz is below. It is not possible to reconstruct this wave with the given sampling frequency. The Nyquist frequency is defined as half of the sampling frequency and it must be larger than the true wave frequency for the sample to be successfully measured. The Nyquist frequency in this question is 5.5 Hz, less than the true wave frequency of 6 Hz.   

e) The plot of 6 Hz sine wave with sample frequency of 12 Hz is below. It is not possible to measure this wave as the Nyquist frequency is not greater than the true wave frequency (Nyquist = 6 Hz, true wave = 6 Hz). As noted in the plot, the only thing that can be determined from this plot is the phase angle (φ) which is 0. Adjustments to the phase angle will not aid in the measurement of the true wave, rather, can only help in the determination of φ.  

f) Direct current simply shifts the sine wave vertically. It does not aid the measurement of the true wave in any way.  

## Problem 2 - Aliasing 
a) Plot of the 6 Hz sine wave and sampled points at 8 Hz is below. Due to the aliasing (wrap-around), the alias frequency is 2 Hz.  

b) Plot of the 15 Hz sine wave and sampled points at 15 Hz is below. Due to the aliasing (wrap-around), the alias frequency is 0 Hz.  

c) The sampling frequency is 100 Hz. The Nyquist frequency is 50 Hz. The frequency content is as follows:
* First term. True frequency is 25 Hz. Since Nyquist > true frequency, the frequency remains the same.
* Second term. True frequency is 75 Hz. Since Nyquist < true frequncy, the alias frequency is 25 Hz. 
* Third term. True frequency is 125 Hz. Since true frequency > sampling frequency, the signal cannot be correctly sampled and frequency cannot be determined.  

d) The sampling frequency is 150 Hz. The Nyquist frequency is 75 Hz. The frequency content is as follows:
* First term. True frequency is 25 Hz. Since Nyquist > true frequency, the frequency remains the same.
* Second term. True frequency is 75 Hz. Since Nyquist = true frequncy, the alias frequency is 0 Hz. 
* Third term. True frequency is 125 Hz. Since Nyquist < true frequncy, the alias frequency is 25 Hz.  

## Problem 3 - Issues in Sampling
a) Quantiziation is the process of constraining continous data to a discrete set. For example, continous data can be constrained as intergers, so values such as 4.1 and 4.2 would be rounded down and simply represented as 4. This process will induce accuacy errors as decimal points are not longer being stored. These types of errors occur when analog-digital converters do not have sufficient bins. To avoid this error, if possible, get converters with a greater amount of bins. Else, adjust the range to more appropriate values such that the errors would be minimized.  

b) Clipping errors occur when the amplitude of the true signal exceeds the measurement range of the device. As a result, what is represented in the time domain graphs are horizontals lines near the peaks and troughs of the measurement record. To avoid this error, adjust the range in the measurement instrument to be able to measure all the signal. If that is not possible, get better instruments.  

c) Oversampling is when the sampling frequency is much greater than what is required to reconstruct the true frequency. As an example, if the true frequency was 2 Hz, oversampling would be using a sampling frequency of 200 Hz. It is not necessary to use a sampling frequency that high. Oversampling means more data to be processed, which leads to larger file sizes and longer computation times.  

d) The base signal used to demonstrate issues in sampling is a 5 Hz sine wave with an amplitude of 2. The wave is only visualized for a cycle of 1 second. The wave has no phase angle nor DC current.  

The An example of aliasing is demonstrated in the following figure. The Nyquist frequency of the wave is therefore 4 Hz and lower than the true frequency. Due to wrap around, the predicted frequency from sampling is only 3 Hz. This can be clearly seen as 3 peaks from the sampled points in the figure.  

An example of quantization error is illustrated in the following figure. The bins size is 2 and it is assumed that the range of the sampling device was set to -6 to 6 amps. Since the amplitude of the true wave only ranges from -2 to 2, all sampled values would either be -2, 0, or 2. This results in poor resolution of the signal.  

An example of clipping is shown in the following figure. Assuming that the sampling device could only measure amplitude in the range of -1.5 to 1.5, everything above or below those values would be "clipped" and set to the maximum or minimum value that the device would read.  

Finally, an example of oversampling is shown below. The sampling frequency is 250 Hz, way more than the minimum required sampling frequency of 11 Hz.  

The Matlab code to generate the data for the above examples is pasted below for inspection.  

```matlab

```

# Problem 4 - Fourier Series 1
a) The plot of wave1 is below.  

b) The following analytic coefficients were solved assuming Tp = 1/15 and f = 15 to avoid long solutions. 
![a0](https://latex.codecogs.com/gif.latex?%5Cfrac%7Ba_%7B0%7D%7D%7B2%7D%3D%20%5Cfrac%7B1%7D%7BT_%7Bp%7D%7D%5Cint_%7B-%5Cfrac%7BT_%7Bp%7D%7D%7B2%7D%7D%5E%7B%5Cfrac%7BT_%7Bp%7D%7D%7B2%7D%7D%20sin%5E%7B2%7D%282%5Cpi%20f_%7B0%7Dt%29%20dt%3D%2015%5Cint_%7B-%5Cfrac%7B1%7D%7B30%7D%7D%5E%7B%5Cfrac%7B1%7D%7B30%7D%7D%20sin%5E%7B2%7D%2830%5Cpi%20t%29dt%20%3D%200.5)  

![an](https://latex.codecogs.com/gif.latex?%5Csmall%20a_%7Bn%7D%3D%20%5Cfrac%7B2%7D%7BT_%7Bp%7D%7D%5Cint_%7B-%5Cfrac%7BT_%7Bp%7D%7D%7B2%7D%7D%5E%7B%5Cfrac%7BT_%7Bp%7D%7D%7B2%7D%7D%20sin%5E%7B2%7D%282%5Cpi%20f_%7B0%7Dt%29%20cos%28%5Cfrac%7B2%5Cpi%20nt%7D%7BT_%7Bp%7D%7D%29%3D%2030%5Cint_%7B-%5Cfrac%7B1%7D%7B30%7D%7D%5E%7B%5Cfrac%7B1%7D%7B30%7D%7D%20sin%5E%7B2%7D%2830%5Cpi%20t%29%20cos%2860%5Cpi%20n%20t%29%3D%20-%5Cdfrac%7B%5Csin%5Cleft%282%7B%5Cpi%7Dn%5Cright%29%7D%7B2%7B%5Cpi%7Dn%5Cleft%28n%5E2-1%5Cright%29%7D)  

![bn](https://latex.codecogs.com/gif.latex?%5Csmall%20b_%7Bn%7D%3D%20%5Cfrac%7B2%7D%7BT_%7Bp%7D%7D%5Cint_%7B-%5Cfrac%7BT_%7Bp%7D%7D%7B2%7D%7D%5E%7B%5Cfrac%7BT_%7Bp%7D%7D%7B2%7D%7D%20sin%5E%7B2%7D%282%5Cpi%20f_%7B0%7Dt%29%20sin%28%5Cfrac%7B2%5Cpi%20nt%7D%7BT_%7Bp%7D%7D%29dt%3D%2030%5Cint_%7B-%5Cfrac%7B1%7D%7B30%7D%7D%5E%7B%5Cfrac%7B1%7D%7B30%7D%7D%20sin%5E%7B2%7D%2830%5Cpi%20t%29%20sin%2830%5Cpi%20n%20t%29dt%3D%200)  

Thus, the general form fourier series becomes  
![fseries](https://latex.codecogs.com/gif.latex?x%28t%29%20%3D%200.5%20&plus;%20%5Csum_%7Bn%20%3D%201%7D%5E%7B%5Cinfty%7D-%5Cdfrac%7B%5Csin%5Cleft%282%7B%5Cpi%7Dn%5Cright%29%7D%7B2%7B%5Cpi%7Dn%5Cleft%28n%5E2-1%5Cright%29%7Dsin%2830%20%5Cpi%20n%20t%29)    

c) The complex coefficient was not attempted.  

d) The general coefficients of Wave2 are as follows. They were derived assuming Tp = 1/15 and f = 15 to avoid long solutions.  
![a0](https://latex.codecogs.com/gif.latex?%5Csmall%20%5Cfrac%7Ba_%7B0%7D%7D%7B2%7D%3D%20%5Cfrac%7B1%7D%7BT_%7Bp%7D%7D%5Cint_%7B-%5Cfrac%7BT_%7Bp%7D%7D%7B2%7D%7D%5E%7B%5Cfrac%7BT_%7Bp%7D%7D%7B2%7D%7D%20%5Bsin%5E%7B2%7D%282%5Cpi%20f_%7B0%7Dt%29&plus;5%5Ddt%20%3D%2015%5Cint_%7B-%5Cfrac%7B1%7D%7B30%7D%7D%5E%7B%5Cfrac%7B1%7D%7B30%7D%7D%20%5Bsin%5E%7B2%7D%2830%5Cpi%20t%29%20&plus;%205%5Ddt%20%3D%205.5)  
![an](https://latex.codecogs.com/gif.latex?%5Cdpi%7B200%7D%20%5Ctiny%20a_%7Bn%7D%3D%20%5Cfrac%7B2%7D%7BT_%7Bp%7D%7D%5Cint_%7B-%5Cfrac%7BT_%7Bp%7D%7D%7B2%7D%7D%5E%7B%5Cfrac%7BT_%7Bp%7D%7D%7B2%7D%7D%20%5Bsin%5E%7B2%7D%282%5Cpi%20f_%7B0%7Dt%29&plus;5%5D%20cos%28%5Cfrac%7B2%5Cpi%20nt%7D%7BT_%7Bp%7D%7D%29dt%3D%2030%5Cint_%7B-%5Cfrac%7B1%7D%7B30%7D%7D%5E%7B%5Cfrac%7B1%7D%7B30%7D%7D%20%5Bsin%5E%7B2%7D%2830%5Cpi%20t%29&plus;5%5D%20cos%2860%5Cpi%20n%20t%29dt%3D%20%5Cdfrac%7B2%5Cleft%285n%5E2-22%5Cright%29%5Csin%5Cleft%28%7B%5Cpi%7Dn%5Cright%29%7D%7B%7B%5Cpi%7Dn%5Cleft%28n%5E2-4%5Cright%29%7D)  

![bn](https://latex.codecogs.com/gif.latex?%5Cdpi%7B200%7D%20%5Ctiny%20b_%7Bn%7D%3D%20%5Cfrac%7B2%7D%7BT_%7Bp%7D%7D%5Cint_%7B-%5Cfrac%7BT_%7Bp%7D%7D%7B2%7D%7D%5E%7B%5Cfrac%7BT_%7Bp%7D%7D%7B2%7D%7D%20%5Bsin%5E%7B2%7D%282%5Cpi%20f_%7B0%7Dt%29&plus;5%5D%20sin%28%5Cfrac%7B2%5Cpi%20nt%7D%7BT_%7Bp%7D%7D%29%3D%2030%5Cint_%7B-%5Cfrac%7B1%7D%7B30%7D%7D%5E%7B%5Cfrac%7B1%7D%7B30%7D%7D%20%5Bsin%5E%7B2%7D%2830%5Cpi%20t%29&plus;5%5D%20sin%2830%5Cpi%20n%20t%29%3D%200)  

The general form of Wave2 is below.  
![fseries](https://latex.codecogs.com/gif.latex?x%28t%29%20%3D%205.5%20&plus;%20%5Csum_%7Bn%20%3D%201%7D%5E%7B%5Cinfty%7D%5Cdfrac%7B2%5Cleft%285n%5E2-22%5Cright%29%5Csin%5Cleft%28%7B%5Cpi%7Dn%5Cright%29%7D%7B%7B%5Cpi%7Dn%5Cleft%28n%5E2-4%5Cright%29%7Dsin%2830%20%5Cpi%20n%20t%29)  

e) The a0, or bais, values of the two equations are clearly different. Wave1 has a bias of 0.5, whereas wave2 has a bias of 5.5. The difference of bias of 5 is expected due to the extra "+5" term that wave2 contains. The an values of the waves are very similar as well, with both terms having the same denominator. The differences of the an terms come from the numerator. Bn of both waves remains at 0, because the major constituent terms have not changed (ie. sin(x)^2).  

## Problem 5 - Fourier Series 2
a) Ten cycles of the sawtooth wave is plotted below. Note that assumed frequency is 1.  

b) By inspection, the average (bias) of the sawtooth wave is 0.5. Also noted is that the function is odd so an = 0. The Bn term is then solved by  
![bn](https://latex.codecogs.com/gif.latex?b_%7Bn%7D%3D%20%5Cfrac%7B2%7D%7BT_%7Bp%7D%7D%5Cint_%7B-%5Cfrac%7BT_%7Bp%7D%7D%7B2%7D%7D%5E%7B%5Cfrac%7BT_%7Bp%7D%7D%7B2%7D%7D%20t%20sin%28%5Cfrac%7B2%5Cpi%20nt%7D%7BT_%7Bp%7D%7D%29dt%3D%20%5Cfrac%7BT_%7Bp%7D%28sin%28%5Cpi%20n%29-%5Cpi%20ncos%28%5Cpi%20n%29%29%7D%7B%5Cpi%5E%7B2%7Dn%5E%7B2%7D%7D)  

Noting that sin(nπ) = 0 and cos(nπ) is either 1 or -1, further subsitution may be made. The simplied general form of the sawtooth equation then becomes the following.  
![sawtooth](https://latex.codecogs.com/gif.latex?sawtooth%20%3D%200.5%20&plus;%20%5Csum_%7Bn%3D1%7D%5E%7B%5Cinfty%7D%20-%5Cfrac%7B2%7D%7B%5Cpi%20n%7D%28-1%29%5E%7Bn%7Dsin%28%5Cfrac%7B2%5Cpi%20n%20t%7D%7BT_%7Bp%7D%7D%29)  

c) Plots are as follows.  

d) 
