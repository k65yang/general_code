# CIVE 497 Task 4

**Name:** Kai Yang  
**Degree:** BA  
**ID:** 20640696

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

**Q1 What is a good image sensor? Why are the high-end DSLR cameras expensive?**  
Typically, the larger the image sensor, the better. Image sensors play a vital role in collecting the light which forms the image. The larger the sensor, the more light the camera will be able to collect. Subsequently, more information will be collected, improving the overall quality of the image.  

High-end DSLR cameras are expensive for two main reasons. 1) Their larger image sensor (more expensive to produce) and 2) their functionality (has mutiple image settings, can adjust how the camera takes pictures).  

**Q2 What is the difference between optical and digital zooms?**  
A zoom in photography is enlarging an object without physically getting close to it. A digital zoom accomplishs this by taking the digital image and cropping it on the portion that needs to be zoomed into. The cropped image is then enlarged to fill up the screen. In an optical zoom, the various lenses of the camera is adjusted to enlarge the view. Implications of digital zoom means that the image quality will be poor because what being seen is a cropped then enlarged photo. For optical zooms, this is not a problem because adjustment of lenses has no correlation to image quality.  

**Q3 Why did the apple make "stove-top" iPhone 11?**  

**Note: the following Q4 - Q6, Q8 - Q9 was completing using the instructor's photographs because the only camera I have is on my phone and the settings are all automatic and cannot be adjusted. For example, when I take photos in darker settings, the software will automatically change the exposure time and ISO to get a brigher image. Additionaly, things like aperature size and focal length are fixed in a phone camera and cannot be physically changed.**  

**Q4 Shutter speed (Exposure time)**  
Shutter speed, or exposure time, is directly related to image quality. The longer the exposure time, the more light the image sensor may capture. Longer exposure times are ideal for taking pictures in the dark. However, decreasing shutter speeds increases the chances of oversaturated images. Additionally, slower shutter speeds will increase the blur of the image. See the following table as an example.  

|  Metadata  |      Image 1 (IMG_43)      |  Image 2 (IMG_44) |
|----------|:--------------|:------|
| Image | ![](https://lh3.googleusercontent.com/0-aMDh3kUZVWJ3W7QB-Xa86su2B-Sm9rXq6DZUNoAx_37_48zg359OdMRh3ww8_uzWZovixlWxlc_zRXYf84cjONP5tyzeRyF9n-3UYbT_LLGnJx5nneBC6gKOGuxEaYFWl0M0_b3wkBQMeqLuOA29DojDBqdJ2SWIF_Fa9WXD9-qcR-majasSo8BpEDUcnu82yM90LbzENhNizzTnvHK1_QFdUHCP6LfhFzVAS4AJ-pletLum8iFUryNbaHiUTWMo9BNWQVKmfqfxEI6IOJrxyvVvVRJhSgo2OothsxDuTF5_5y-ET-HQYoUSZC8UJJ0ZgP6W8OQZ3lunqhbXTtAwNwPeMJdjea3nPWr46OBLDCUiy8nQpcjGeZDx5luGE_IqJNYNoUVJfcYEH4GjuksqiaZn-G5SyppeM0lbFN4Soaa9VB-HRClTHgvFKrRbFQPuSp_2eRcw5p1aNfCYzDpAx7c6nIc7fDRGeGaLuQ5HqIlPfnSegEgRNozo7n7rA2_q81idajtlCCxpHFTuGbwF_6q9Z1vJEKjpHRS2IHzJyIjQ--jjz33Vy0bwRZsYfVAB7rusA20dhjD2xPkAZntvT1LB13sV2Acu8Fc8kRQnAAOObMdkSX0OGDf69QcIEZzYsAe5mv1YF6qX7dVNDen94Nm3qUSI_MlUVhMveFKGmmzhqqKBN_eQ=w938-h625-no) | ![](https://lh3.googleusercontent.com/MYEbuKz5KdIjA44Yu09OcJm4IqH8dBgRUBmmIJXe2GTl4gZrGHk2BtLDt2Wrc6a8Dafi35SAkLXTEQRGbwwWVlcJuzWu-8545sfGHhWh7x57ObVuRjJbmgsHb0TaJCO2OOGmG-TKTZwPoToFJm7K2AtPCYijLnruE_FtAoQnx4kZBSKhW4xDYSdRVu52o-1P8lFyZfUWDJwsLaeoaP0Qus_-QlSCDuyiEOwLkgrriGMb45Kd3itHhhWqDsOcGd8K3FyRhQfPjPdWSZTwMtMqTbxi5y81y4Gm7O7seacU2v2oM8QCJqvyXtQApuSKiisSbgpfcY4MlokjBcII65ASDUC5aGfOp1wGRym53GaGXDktujYBUXP0M8UX82qUEUVwXx0kBt4dNuNKEGKfvklVvFHKvxwUJkjxAraNFGvWjoVpeKv67ifyZDpRv1cKjYWJXR_WA9-IRB2vDNep4vtmjLfS69paaqZbkzlfUYphF6U_PCY3p3I9KNUorK0O9xcj6U2OnOFuCvybFfkdZZj58Y6yqqlPiLiTlmz1LTJqhuSjDE8fAXURYSLG0_CCOVc8gp_gVi5U72e7FzzT4T5F2xBc5-PSMW5BcXEjAEAv-RiCf3YxS213TfAtzg3BjpthLxGqCRZoSqatybTEm2CWHabJ-MdOn2ZHFw58xWwqi-H1B9Xha0QW3w=w938-h625-no) |
| Make | Canon | Canon |
| Model | EOS Rebel T6 |EOS Rebel T6|
| Date and Time | 2019:02:04 11:51:54 | 2019:02:04 11:52:19|
| Image File Type | JPEG | JPEG|
| Resolution | 5184x3456 | 5184x3456|
| Focal Length | 55.0 mm |55.0 mm |
| Exposure | **1/160** |**1/15** |
| ISO | 1600 |1600|
| F-Number | 5.6 | 5.6|
| GPS | NO | NO |
| Flash | ON | ON |

**Q5 Aperture**  
The aperature is the size of the opening (or the pinhole) in which the light may pass through. The smaller the opening, the less light will reach the image sensor. Aperture is measured the F-numbers. The magnitude of the F-number is inversely related to the size of the aperature. The larger the F-number, the smaller the opening and vice versa. Pictures taken with high F-numbers will generally be darker than the same pictures taken with low F-numbers. The following table demonstrates the effect that F-number has on photos.  

|  Metadata  |      Image 1 (IMG_46)      |  Image 2 (IMG_47) |
|----------|:--------------|:------|
| Image | ![](https://lh3.googleusercontent.com/ARCyhjbUso-6PSSIxBeeaHoOrpv901gU2hXVwZm4stgJ_HlowGwmfIF_ZZx8t2QE5VqNo8yRXlbI21eVq7lzQm0jEWHL-aUSGPM_pO_mSFw4IIFk3hZ4TLp8KE8bWsz4c7AIYb8cevOm3MUo2EildPofg1TDWbIgWtAPmW7XDqjCu4zYo5Fonw-zdp9J-DGfENZug_aWnfOGHrd95Ai0AaNGJW-QsmodDZ8BDaoxDIm3Q2v4cN0Dmepyoh2cMYcN6GB6MzMLUv2-d3LhTfEmOvt_ramL5bXohRSPw177b1_FHsZ89iYY8AEEJaVekykT-WDk3tdHZQilu4-ZWt6lpw1GEUXdZLzQZo0z9LFxtEcrqouTG03aCMS7O42n4HoxasqT3MLSgOK41-Fvm3VR8A0Ol_TQBRkdyfsyyCH5yjvVewWoQSRlsiNOBPxDfov8dWumna0f2gWrV7PM_qUqaFmEDlBqaFrB6uB4U60V7LLN0uiXKszSWakEAgMvHtW_jlTF7ifXv3BKxH9lVmokhtmQ7n0IaoEu4D50cUKe1AeYJwmf9hdU1VlIQcyBoZJS_pEceGY6IRKZQmthuVPgGRrOyl3bM8k953WC48U2sLmjtHEu-JGVd8gHT3g4uPhjkTh7RUNXJovaMFGshkuP_rLCaPcublHJlECzg40bg_cAJzXELNGb_g=w938-h625-no) | ![](https://lh3.googleusercontent.com/6mn4TKhzAqcAok_RC182-kWHeVEwIq_ehwyQ1uhM8vvvHZctYOPhziAglWH64sDN_8vZD5Ib2vJKEEfLpiP-bfaxvYEZKFsnO5lINfolGyRxzMIQVvRd8pS7pwhllGPxhOHbkWUzmV_ATKGbk6qn1BmAwxVlTIp8N6x268h9AkemGMdB6FaJC0oSyKdfX0tg7NRygQObIDhSWN5cLQnypO2R5iDCd6Klk1OcuBejjsapgoIdhTwKdru_RW3MIPEQde25s9IjPnZr22Z88qG6o-Aahmriv2wLS18Kv5Gf-8nv4s8zl6MiIS5c2O0xUBBks7Zc1f8UCtdHC6NvLMV__nTz98p8LI_zDW9zKSukVUp4_LI6abVOvy-mksg3ACzlRYiedcpN72DB8DxLXB-HJzFWegjC_3je9sj8inrPlZ0vZ9YYrxIvV7D-as5W_OIBpIRApbfuH1UUj3wuTHwC7sBpTCDa-vgW7au5rYoWAdwNqy1tTVC5heE2biTAR3e8KrsCmqrAVKy786cXOA4YVVC2KJcwpNnyOFfHwXPD88CRLWj-27byoGJ-iNHJ6XNJH6D4crx-hWiadZS6k59bQaBGxaKm5yk4erwOephkPrij-MZTGtq--SNLzU5Apg-n3PtoT51jiCox-w0zAiQWAdOkVXB9wl8rCYKHNVTYrAR9ktJkwNTdog=w938-h625-no) |
| Make | Canon | Canon |
| Model | EOS Rebel T6 |EOS Rebel T6|
| Date and Time | 2019:02:04 11:52:36 | 2019:02:04 11:52:44|
| Image File Type | JPEG | JPEG|
| Resolution | 5184x3456 | 5184x3456|
| Focal Length | 18.0 mm |18.0 mm |
| Exposure | 1/200 |1/200 |
| ISO | 1600 |1600|
| F-Number | **5.6** | **22**|
| GPS | NO | NO |
| Flash | ON | ON |

**Q6 ISO**  
ISO is a measurement of the light sensitivity of the camera. The higher the ISO, the brighter the image will be. However, high ISO settings may lead to over-saturation in the images. The following table demonstrates the effect of ISO on images.  

|  Metadata  |      Image 1 (IMG_40)      |  Image 2 (IMG_41) |
|----------|:--------------|:------|
| Image | ![](https://lh3.googleusercontent.com/xQtTnP0FsDHbdlxwEyRI0cpAW1t1n6v-sEWWxkhgq0yjWzCYhv_ZY2uy6bZynlk9LGEhxSYICORaNMGp7vFuiSmgZDyc1Vrzwim7vtagzRy8jxbDOjCM_1MNnDiK8WT8otAbKFnBZBy-IOBLNzy0WfH_EgdR1Gz5EkqQffMtHqY0ghSpnZOR8zE38_jKgFR7di0yTJgOt9WtwTDAR0SDUfZFPsGuayoG3Dn4DcwJcLpOuX0QD0GZiyOhDkzY_dmtpJbDQX9XPD9z7XX5W2H5L2mZM5RoE3_eh5gUna3h4u9drT1Mb9bdZ0ySzZkQCThi2pWFdYrI6Viy8oo-N-1tGHMgNr5exT8yqR-ACMlRVDRxfUbkqoALm9GWT6LpP4cbZKNkvAPGs_k4PQENdSftMNC-PqTSZBc9AtdRkYPPPaywFcmCskpWo-26znsI4_gOBn_nQOLuhlCfLtAAVWD2PsslUjmln5pwCg2tpgWvxJMYNzjy7O3HV6BQkV8CxzW7KnDnAV_vvh4occIO2RMImqbA7j-d0OApMTht6E-YGq2WjBZiOBPkaTBeeOgJoqvauX9PFPxrMx-v5dLVO_113DvUojTRKa3fUIuQmXk8geE0d9W9gmIoWYtPWTaTYtoYlluBqN_cMIHd0epRtDkOMUvsFxoBcz_HmqwRXt5QjKTfwYkJIAzYvw=w938-h625-no) | ![](https://lh3.googleusercontent.com/K4n_0hGmFFwBxVqeZsWHjzePJRTinsUyffcHoRa5wGrdfV-H6MpKLS2yL2jFSHZcGaRnEeFqJ7rRCZqEpoFj94nK87mq8Ag_EJp-9hJVXEcAe05LE-6Pe-HFVLEb-kYMBaM1rES1VFxdE27F4Q3waoR73rVKyAZtxTMxEFPjFFamLa2q0P9OGr-BWoZLUojLoq4VOXLH70gjv-xV6lbz8G6-KClYrzcyINokSnjxZW8qvXAeysNIkFWjHpWOcyOVc4g9UjdGjhTMCgWIkbxO-sTs1exqciG4MShOcIGMMlRy5UEkthsNiIZ7NjX5BrZgGXYNiagSVqIIvMSpFuamUtPpWmKq3ANklKIIiM2GMF-ifiZQANkzNfXa5MTyBt_jUznqz0nCnTmLHx4UQQODqmKsWWL1dmFIYmmIV2FDB36X_gizOunFcI_Y5KtT92IRTnV6QDUWPrTP23rNCuOlfgsrNfLzRYL0SUSBwBcZ6AzlY-lj8kORhjHRRTkL1_CrElBrDsmi1keG-4GT7X9oegF3p6zUo0mQbkdA3JIs7cEJGtqQWYi8iiCdIkUU6iYle2ylsm93dlQ1vD3XZ8tYE0QXDFod4ipE0MwN9xYlGrqRmxbVc-G2WHyCoQtr-QeVvTdWc9CehAySLAJ_pYwh3wN3mbgQpYgvvi0ZMYXr5enJYc6dufhPYg=w938-h625-no) |
| Make | Canon | Canon |
| Model | EOS Rebel T6 |EOS Rebel T6|
| Date and Time | 2019:02:04 11:51:20 | 2019:02:04 11:51:35|
| Image File Type | JPEG | JPEG|
| Resolution | 5184x3456 | 5184x3456|
| Focal Length | 55.0 mm |55.0 mm |
| Exposure | 1/160 |1/160 |
| ISO | **800** |**6400**|
| F-Number | 5.6 | 5.6|
| GPS | NO | NO |
| Flash | ON | ON |

**Q7 Flash**
Camera flashes produce an extra source of light which can improve image quality because more light will be going into the camera sensor. The two provided images show the effect of flash and no flash. Because the picture was taken on my phone, ISO was set automatically by my phone software. However, the ISO values are still fairly similar.  

|  Metadata  |      Image 1      |  Image 2  |
|----------|:--------------|:------|
| Image | ![](https://lh3.googleusercontent.com/zIZryr74lMA6aq7NkTOK0cRZ2s21qdDhjNojGGrJFBlRfGCVAryyhxKm0IakOfA11M_mr61RmQx41pw9MfDesikNDbbvkj-Bgt0n4Rmlad-z5AtBWPbeZSy_lCxG5aEjcYT_oW9evhK5IntUVLCTZnsqvJLoIKTW4GeraKjs24IKxLcLmTwO514tHoDoRmihmiZ5tcQciJoOOqqHCbVsYzYGGZHqpuhbpLwolD_kk0IeNp8SkinpO0KDFyddsgZK43ZjUS6lM616pbQf6SNHhCGZaSPuVwSP7K5mnEuVwMm9AFhmSz-hGMMARKs8WxbanKMNAcGApfETC3_b2ppdlxwGcKcjSq3qTsz2OBTuLVpa0MuAysDbcf2nVI4BwalhjvOv0C9X-36c9V1T_ori1zqs7gQ6MKLlJYftUAzuTISCjSHKCqoFZ3MEjKOHaZittarT-Cq_3q_9VP5zu0SEoZzlkLcOu7sFaitPKw2sRDx6y0mIP08ZztYJCuVyY4q5603eVk5A-DAFlHaZm9iVAVplLRD_EEAdp5Ho-WkJdAPSmm6W3D1bZfmtA1it-UhtHOLiFYFrJH7CDNS-A7FUQyYWZNDD0jzuHZfybMqfY3QHqvZeWYJScSskLsu4jLHooG88HuFw54GyiPau0GWkxHb_TRMIETw6_YtqF9SPeOt67wV_pc1K0A=w469-h625-no) | ![](https://lh3.googleusercontent.com/kXvTCr_iZ69h9DGe1jeNi1Ulk0HZaD_I2a8igdn-ss-6zOKLNYn1ZVNV7ZuBSqA3qsdMO0E99yVgIwnm2qaJYkfcr7jB7m0qADPaxgzPLMW09ZPMaKr_nzSjcIoQmRGMr47pxGqvPQ9Arh9AZPa8J8c6YPdOE4MT0M79x5QnpEq9a8uitOtVuo2xhCknGW-9bXmawpBi35FRCKFCWs-FLI2_KvEYudSkbdQj83nVw_8qeO3GO9fF_AVPeI8u5rbwwdF-XDNc3daGy9AWO01SVDYosUZ3jZovaPrmujCF0qS-OgYi9in0CTFBewsRUsy8GupvdDySMM_fQYwF_RPzhQj17pThP4Iov6CTcLBrCUNMuHhuCvsmM9-2nm_lHH8J9JdyBK56oYKlxiLIJXhVTJcsn_ra4c-JcRFCsS9hLqfjMEnRh_YQSbv9WE5UgXhKdJThtzGStGa02YR1t-OhJP5ETeH93PN_g3xCL-Po0hqtH1vl9hU-9kPRhZizeBUQXvHZFTG-PGA__wJumQIc36uYOSasItJyrOHfTP06EKsfzQDDhMOLI7DUWDfYI4jhUv4J4ZhsMZQfSckaQi87-SxhfVyh65AQ-9OlUokXVVDJaoeVgxTbOO6PoTuWzPDOYBIQpIMJKPRnvOLjg7tLscv_3AQsVgD-QIzODIVhVK9vZ_-s2FXiiw=w469-h625-no) |
| Make | Google | Google |
| Model | Pixel 2 XL |Pixel 2 XL|
| Date and Time | 2020:02:22 17:29:47 | 2020:02:22 17:29:53|
| Image File Type | JPEG | JPEG|
| Resolution | 3024x4032 | 3024x4032|
| Focal Length | 4.5 mm |4.5 mm |
| Exposure | 1/125 |1/125 |
| ISO | **146** |**131**|
| F-Number | 1.8 | 1.8|
| GPS | 43.470269 N 80.540864 W| 43.470269 N 80.540864 W |
| Flash | **OFF** | **ON** |

**Q8 Focal length**  
Changing the focal lengths is essentially optical zoom. The greater the focal lengths, the more zoomed in the picture will be. It does not have any effect on image quality. The following table demonstrates the changes in focal length has on the picture.  

|  Metadata  |      Image 1 (IMG_45)      |  Image 2 (IMG_46) |
|----------|:--------------|:------|
| Image | ![](https://lh3.googleusercontent.com/y2OUeUkUZ8gAUDOgJpxvPqcpW6N1oE4lfeIThwHnB3-2Qb44CzhpWd0CI0ld4ge30QrFEPcxeNAFdbY6c4pDeE-1dgbC03D0mF3n8kNVscRAZBBG4nalk5RTephGfI2Js3Vy8YkS7PzHX82y_i81C0cFJ_PZTS2m-A4hbsoRWkiemmPo7R_dBA3BrFNeq5hbglU-RooYyD1kkiDyQBVhEAbV9_mhphIlwxgUuGpGQPYbceqskRW6pu6Yo4IjpR9NYJeq0RKP1CqCyRBRN7WZLU5rLN2hRxzjo1FuSlkO9bQo-WopnWVYHEsJ1EqZrndP3SZJp88m-nIIKX6hRza2i6jbfOZzn0xw24neHmQxZx9KaAr4z1OwuzSMPWsp_1k0qzZOavYzXFZM4vOJ7uQTUAWldwP7HA3kSewSEwTgmbRBKDZK_FR7ppI4-Xv8yKm088I5iX68H16mnGmRiXgwuOKCpmZrHVbbKWRiF5HVWAw0lH6NFYGdFaTBpG1Ec1Pw8VgUeidNdkwSWAMP8PkSo4CPp22A5GrMvhwhEHIbo6TjKLkv7ZvbMuR9z-WHgzM2vhH9lO_f3zL0_4klSpdeM1nCAu2UuoU-6qvWZH24g9Fj_q-Llztg0q_hKJmblIjwAq8SSHNAbsnvITNrCPacwYVeGQGNVN5g-zl8RFtBv4J5PfnjZHyD6Q=w938-h625-no) | ![](https://lh3.googleusercontent.com/1GPD3GgKSDDiiyGRYZ_yHZhEuQrlO83E_HkFSQDRnv2Qd7btJh7pjgmg6i6nDPjU5N17anJU5Pfx0fDNQTS3UIrn-mqOeg6ySWE08hS-WzdYkYkMd0aYL5Me2CRRcHCdCTlNRPG0Ml9rLcGGjyOEDORraycXngDhudBXko9DHLwCnLiTsWs34VIDBGYLNpfB5WNpRS50qw88SUsHL9cGLJoSx5C8P6f9oXr87W3hza-vKWZBczuDEWnD3fRTDAeqdhdkwBeQJA0v9JxtyQj17yl0a9HCt-pQFo3QuHaKcsgPlW9FbexJkg-vpFIdqN1IVxdncp1bRIbxyQituLI1ZlA3UEnAutoAwKru5vsLBNqzsGNc7yExiqXy_YoZVryGgzW1rh3Q6fMySU6bVlQ9TuO0K80crO8GZgasUA57WLzI6KhZVKKg-XISd0mfCy50S7RADzvFpg8bxNwNflJRhvFsuEz-kHQlbGFnmh8wTlNlPBvzPWYx4_27EKMaqhQl9jm6PMT_TOYs5Ns0mmpc6GoLTqMScZiEZF60eT_uHQbA2u1ji6g4g_toTbTvh1w8WbJc4-b5axnvjUAjfScWAcMOLSb13t0LX6Y5VbYRyCrnK-qN4DRAJKSwJ9gaW2C1sFHDhjB2ogetXLU4WynrA1p5GPTEx6Q8hg7YB4weVKxA0XTAAdTUxQ=w938-h625-no) |
| Make | Canon | Canon |
| Model | EOS Rebel T6 |EOS Rebel T6|
| Date and Time | 2019:02:04 11:52:28 | 2019:02:04 11:52:36|
| Image File Type | JPEG | JPEG|
| Resolution | 5184x3456 | 5184x3456|
| Focal Length | **55.0 mm** | **18.0 mm** |
| Exposure | 1/200 |1/200 |
| ISO | 1600 |1600|
| F-Number | 5.6 | 5.6|
| GPS | NO | NO |
| Flash | ON | ON |

**Q9 Field of view**  
The field of view is what the camera is able to see. Adjustments to the field of view can be accomplished by changing the focal length in optical cameras as shown in the following table. In digital camera, the field of view is changed through cropping the digital image and expanding it.  

|  Metadata  |      Image 1 (IMG_45)      |  Image 2 (IMG_46) |
|----------|:--------------|:------|
| Image | ![](https://lh3.googleusercontent.com/y2OUeUkUZ8gAUDOgJpxvPqcpW6N1oE4lfeIThwHnB3-2Qb44CzhpWd0CI0ld4ge30QrFEPcxeNAFdbY6c4pDeE-1dgbC03D0mF3n8kNVscRAZBBG4nalk5RTephGfI2Js3Vy8YkS7PzHX82y_i81C0cFJ_PZTS2m-A4hbsoRWkiemmPo7R_dBA3BrFNeq5hbglU-RooYyD1kkiDyQBVhEAbV9_mhphIlwxgUuGpGQPYbceqskRW6pu6Yo4IjpR9NYJeq0RKP1CqCyRBRN7WZLU5rLN2hRxzjo1FuSlkO9bQo-WopnWVYHEsJ1EqZrndP3SZJp88m-nIIKX6hRza2i6jbfOZzn0xw24neHmQxZx9KaAr4z1OwuzSMPWsp_1k0qzZOavYzXFZM4vOJ7uQTUAWldwP7HA3kSewSEwTgmbRBKDZK_FR7ppI4-Xv8yKm088I5iX68H16mnGmRiXgwuOKCpmZrHVbbKWRiF5HVWAw0lH6NFYGdFaTBpG1Ec1Pw8VgUeidNdkwSWAMP8PkSo4CPp22A5GrMvhwhEHIbo6TjKLkv7ZvbMuR9z-WHgzM2vhH9lO_f3zL0_4klSpdeM1nCAu2UuoU-6qvWZH24g9Fj_q-Llztg0q_hKJmblIjwAq8SSHNAbsnvITNrCPacwYVeGQGNVN5g-zl8RFtBv4J5PfnjZHyD6Q=w938-h625-no) | ![](https://lh3.googleusercontent.com/1GPD3GgKSDDiiyGRYZ_yHZhEuQrlO83E_HkFSQDRnv2Qd7btJh7pjgmg6i6nDPjU5N17anJU5Pfx0fDNQTS3UIrn-mqOeg6ySWE08hS-WzdYkYkMd0aYL5Me2CRRcHCdCTlNRPG0Ml9rLcGGjyOEDORraycXngDhudBXko9DHLwCnLiTsWs34VIDBGYLNpfB5WNpRS50qw88SUsHL9cGLJoSx5C8P6f9oXr87W3hza-vKWZBczuDEWnD3fRTDAeqdhdkwBeQJA0v9JxtyQj17yl0a9HCt-pQFo3QuHaKcsgPlW9FbexJkg-vpFIdqN1IVxdncp1bRIbxyQituLI1ZlA3UEnAutoAwKru5vsLBNqzsGNc7yExiqXy_YoZVryGgzW1rh3Q6fMySU6bVlQ9TuO0K80crO8GZgasUA57WLzI6KhZVKKg-XISd0mfCy50S7RADzvFpg8bxNwNflJRhvFsuEz-kHQlbGFnmh8wTlNlPBvzPWYx4_27EKMaqhQl9jm6PMT_TOYs5Ns0mmpc6GoLTqMScZiEZF60eT_uHQbA2u1ji6g4g_toTbTvh1w8WbJc4-b5axnvjUAjfScWAcMOLSb13t0LX6Y5VbYRyCrnK-qN4DRAJKSwJ9gaW2C1sFHDhjB2ogetXLU4WynrA1p5GPTEx6Q8hg7YB4weVKxA0XTAAdTUxQ=w938-h625-no) |
| Make | Canon | Canon |
| Model | EOS Rebel T6 |EOS Rebel T6|
| Date and Time | 2019:02:04 11:52:28 | 2019:02:04 11:52:36|
| Image File Type | JPEG | JPEG|
| Resolution | 5184x3456 | 5184x3456|
| Focal Length | **55.0 mm** | **18.0 mm** |
| Exposure | 1/200 |1/200 |
| ISO | 1600 |1600|
| F-Number | 5.6 | 5.6|
| GPS | NO | NO |
| Flash | ON | ON |
