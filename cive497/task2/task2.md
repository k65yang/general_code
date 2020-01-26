# Task 2  

## Problem 1 - Sampling
a) A discrete signal is comprised of specific values corresponding to specific timestamps. It is the sampled values of a continous signal. At all other intervals which was not sampled, the discrete signal has no data, hence its name of being "discrete". A continous signal is one that is continous and has values defined for the entire time domain.  

b) Plot of 6 Hz continous sine wave is below.  

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

d) 
