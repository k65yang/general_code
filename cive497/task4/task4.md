# CIVE 497 Task 4 - Kai Yang - 20640696

## Problem 1

**Q.003** In image 1, the red and blue circles were added on top of the image, not into the image (ie. the red and blue circles were overlaid). This means the image is still greyscale (channel = 1). in image 2, the red and blue circles were added into the image (ie. the red and blue circles were a part of the image), requiring the need for 3 channels because the image has colour.  
  
**Q.004** See Q.003 for the explaination.  
  
**Q.006** The maximum colour value is 255, which represents white. Using 'uint8' and muliplying by 300, the stored value cannot be greater than 255, hence the reason why it is false.  
  
**Q.007** A bit is a basic unit of information which can take on the value of 0 or 1. A byte is a unit of digial information that generally consists of 8 bits.  
  
**Q.010** Resolution and image quality often go hand in hand, but high resolution does not imply high image quality and vice versa. Resolution is how many pixels the image consists of, whereas image quality related to how much detail is stored in the image itself. As demonstrated, if image quality is low, resolution can be improved (by subdividing existing pixels into more pixels), but that does nothing to actually improve the image quality. Additionally, high quality photos do not need to have high resolution, they can be small, but still show detail.  
  
**Q.011** A color image can be split into three channels (red, green, blue), eash represented by a matrix showing the intensity of the respective colours.. Summation of the three channels results inthe color image.  
  
**Q.012** Loseless image compression, as its name suggests, is a class of data algorithms that allows the original data to be perfectly reconstructed from compressed data (ie. zip files).  
  
**Q.013** Image size is a function of the product of the resolution and image type. If the image is a color image, its size would be 8688 x 5792 x 3 = 150,962,688 bytes (approx 150.9 MB). If the image is greyscale, its size would be 8688 x 5792 = 50,320,896 (approx 50.3 MB).  
  
**Q.016** The double() function would change the number into a double data type. The im2double() function would normalize the number by dividing by 255.  
double(255) = 255  
im2double(255) = 1  

## Problem 2
**Q1**  
Typically, the larger the image sensor, the better. Image sensors play a vital role in collecting the light which forms the image. The larger the sensor, the more light the camera will be able to collect. Subsequently, more information will be collected, improving the overall quality of the image.  

High-end DSLR cameras are expensive for two main reasons. 1) Their larger image sensor (more expensive to produce) and 2) their functionality (has mutiple image settings, can adjust how the camera takes pictures).  

**Q2**  
A zoom in photography is enlarging an object without physically getting close to it. A digital zoom accomplishs this by taking the digital image and cropping it on the portion that needs to be zoomed into. The cropped image is then enlarged to fill up the screen. In an optical zoom, the various lenses of the camera is adjusted to enlarge the view. Implications of digital zoom means that the image quality will be poor because what being seen is a cropped then enlarged photo. For optical zooms, this is not a problem because adjustment of lenses has no correlation to image quality.  

**Q3**  
