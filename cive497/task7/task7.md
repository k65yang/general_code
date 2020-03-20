# Task7: Image Stitching & RANSAC

**Name:** Kai Yang  
**ID:** 20460696  
**Degree:** BA  

## Problem 1: LoG and DoG (10 points)

a) The Laplacian of the Gaussian (LoG) is the second derivative of the gaussian function. The LoG filter is commonly used in edge detection. Being the second derivative, it can detect changes in color/intensity of the image. Also being a gaussian, it has an image blurring effect as well. When the colour of the image does not change, its derivative and second derivative will be 0. For these areas, the LoG filter will have no effect. When the LoG filter is convoluded over an edge (an area of change in color), its response will be a sudden increase in values as a change in color indicates that the derivative will be non-zero. Measurement of the sudden increase indicates an edge. A change from a darker colour to lighter colour will be negative and vice versa. 

The LoG filter is also commonly called as a blob filter. A bolb filter is one that is used to detect regions within an image that has different properties, as compared to the surrounding regions. The LoG filter is shown below. Note the value in the centre compared to the rest of the values in the matrix. This filter can accentuate certain features of the image, provided that the "blob" of the filter is around the same size of the feature in question. Furthermore, to identify features of different size, the size of the LoG kernel would simplily be made bigger or smaller (or more efficiently, the size of the image would be scaled up or down).

b) Application of a gaussian filter will blur an image. The difference of the gaussian (DoG) is the subtraction of one image blurred with a specific sigma against another blurred image with a specific sigma. Since a gaussian filter suppresses frequences above a certain range, subtraction of two images convoluded with gaussian filters preserves only the frequency ranges that lie in-between the range of frequences orginally preserved in the blurred images. 

A DoG filter can be used as an approximation of an LoG filter. It is especially useful in blob detection. Images filtered with different sigmas may be subtracted against one another to detect edges that appear at various images scales or degrees of focus. In other words, DoG algorithms may be implemented such that blobs of various sizes may be detected. 
