# Task 6: Image filter and edge detection

**Name:** Kai Yang  
**Degree:** BA  
**ID:** 20640696  

## Problem 1: 2D Convolution (10 points)

a) The selected image is shown along with the results of the 2D convolution. The image was colour, so it needed to be split into individual RGB bands to be convoluded.  

![](https://lh3.googleusercontent.com/-Zm-Rz-N1tX3h4XMpb0hTfqIvHT3FpCnUXoMtg6sVQyyAZHDIvh_OdaK8aS7ab2y4HcQ5ZWytdpZEqu5YZcUDNF0dhWWpslBiYxgoJRjcVi1RT9UjAxQVypv54pQZ3g_OmJgN2A7hb68NIo8HUZ8CerJeWSf__ESkHVOlnq25wkG2m0oGcgQqR1jDJl-oBlAvMCcLmS4ffLQYseEFNb3lzvaUxdBGz0VkKs5WpFFmzltrxJ3uCegYvg7RPqzo7D485KUT1uxLvFWfSGu4CUjpFtlZxubl9l70sZMbfMoZqeULEJE8cqBHW-QRqYYYpdK7_25qRoe-JrwzbLu0KRDY6c258MZK6vfXoNDh8Ih3wlq68kMGDYTS9WfvDymNeWb-zJ9AWFiXISz7BlZDt57ILCUuM5OlIgRQ1ZOaAfs99i8EdtZb7sanVG0s51V6QFBqXxS-7vNmId46dApg6Zwff8LZpUj9WtrpVlL0Z5co1BHBWLVVQ-ArFgsF2vgPsSpsmIdO7vSdDsxzwzfB_6_RQWyPW3Z7PGhwOVjLtBMTzApUV_uY4fVQMgj1MVGw7nT6OVT9Y8EONjiIzQjRAwtKVCPJ3iDUIuw_IJ45p15zDHr76ZP-Z-tIL9XKsqvPMALMqFyVRnPJeR7m60Eu_UHILKdqiWmYP3GUuZqn3PU8zyVviIIuBW6Vg=w790-h477-no)  

```matlab
% Load image and resize to 250x200
temp_image = imread('problem1.jpg');
imSize = [250 200];
I = imresize(temp_image, imSize);

figure(1);
imshow(I);

% Define kernel
H = [0 -1 0;
    -1 4 -1;
    0 -1 0];

% Since baseImg is a colour image, split into RGB channels. Perform
% convolution on each individual channel, then combine back into image
IR = I(:,:,1);
IG = I(:,:,2);
IB = I(:,:,3);

IR_conv = conv2(IR,H,'same');
IG_conv = conv2(IG,H,'same');
IB_conv = conv2(IB,H,'same');

IR_conv = cat(3,IR_conv, zeros(imSize, 'uint8'), zeros(imSize, 'uint8')); 
IG_conv = cat(3, zeros(imSize, 'uint8'), IG_conv, zeros(imSize, 'uint8'));
IB_conv = cat(3, zeros(imSize, 'uint8'), zeros(imSize, 'uint8'), IB_conv);

I_new = IR_conv + IG_conv + IB_conv;

% display new image
figure();
imshow(I_new)
```

b) Convolution of the image using the same kernel but with a user defined convolution function results in the same image.  

![](https://lh3.googleusercontent.com/gsoF35vQEiQmRJYj8XiGzNgSLlhca44fhOMUcIz95-6Y55w1NqwFg09DMPuOz912Pm_FgNlvQLGXA-r1W5j7DCSdlGh6Aq0XLFdUZhzk1jqYM6tbBfj5cRBLVEjfFFxVcNssAn59gNdvO9gyX0LSqR2mIdsB75qBjHBjQcTSgzsHR_tcNSjJoltCMQ3BMaLmUkcATe8d1MMpmt-G81Dbi-ILWOcHMsq03IjDieILXuX-iEEVRBE3oR8JrlyyIT9EsvfNggSpuniYm8Q-tdhSc0RutJ1DpS0iGsuGy1O91huBZo3ACKEjEZbRX0f99ZiS4R-DM_kCsTNKaWS6bW5w6Q53-WBcc_s1p0nPMS8ysTS1J91UiVoX0qx0yTznsnOBlzJ7FXOrprrWGJpnGQJ75rJCVQTyPPtoc1NPLqyPwbWR_QW1v3Mub-z34HAtLx5YOwZmHkphyv12ZEtqW9D77eOE0AUk02ry-3QQPE6xFuv7-sBhY0rfRQjKgpUMItEDwqRx-IgbuVP8Ba1ulDgB5ptwealRF9eHoxTbbiBm0Cqq6UuKBbN9-Bc1iiG55UOYttwalBMnlli91vfu6uzcQz4mT2h39zRxYpFiTcGopdx5xkdDPNpoxhRZhzlFqvuSLZBlWai_qnDBdezowUbzrosrKvOMZssePIca3Kws9U1-_J5cZnfXiQ=w790-h477-no)  

```matlab
% Load image and resize to 250x200
temp_image = imread('problem1.jpg');
imSize = [250 200];
I = imresize(temp_image, imSize);

figure(1);
imshow(I);

% Define kernel
H = [0 -1 0;
    -1 4 -1;
    0 -1 0];

% Since baseImg is a colour image, split into RGB channels. Perform
% convolution on each individual channel, then combine back into image
IR = I(:,:,1);
IG = I(:,:,2);
IB = I(:,:,3);

IR_conv = conv2_forLoop(IR,H);
IG_conv = conv2_forLoop(IG,H);
IB_conv = conv2_forLoop(IB,H);

IR_conv = cat(3, IR_conv, zeros(imSize, 'uint8'), zeros(imSize, 'uint8')); 
IG_conv = cat(3, zeros(imSize, 'uint8'), IG_conv, zeros(imSize, 'uint8'));
IB_conv = cat(3, zeros(imSize, 'uint8'), zeros(imSize, 'uint8'), IB_conv);

I_new = IR_conv + IG_conv + IB_conv;

% display new image
figure();
imshow(I_new)

function conv_matrix = conv2_forLoop(matrix, kernel)
% Performs 2D convolution using for loops.
matrix = im2double(matrix);
matrixSize = [size(matrix,1) size(matrix,2)]; % rows, cols
conv_matrix = zeros(matrixSize);

kernelSize = [size(kernel,1) size(kernel,2)]; % rows, cols
kernel_centre_x = ceil(kernelSize(1)/2);
kernel_centre_y = ceil(kernelSize(2)/2);

for m_row = 1:matrixSize(1)
   for m_col = 1:matrixSize(2)
       for k_row = 1:kernelSize(1)
           k_row_flip = kernelSize(1) - (k_row - 1);
           for k_col = 1:kernelSize(2)
               k_col_flip = kernelSize(2) - (k_col - 1);
               
               ii = m_row + (kernel_centre_x - k_row_flip);
               jj = m_col + (kernel_centre_y - k_col_flip);
               
               if ii > 0 && jj > 0 && ii <= matrixSize(1) && jj <= matrixSize(2)
                   conv_matrix(m_row, m_col) = conv_matrix(m_row,m_col) + ...
                                    matrix(ii, jj) * kernel(k_row_flip, k_col_flip);
               end
           end
       end
   end
end
conv_matrix = im2uint8(conv_matrix);
end
```

## Problem 2: Different Kernels

The convolution with kernel H1 is shown below. This filter will produce a blurring effect.  

![](https://lh3.googleusercontent.com/sSBCi-wuKAjFr7cnmx9M9rEjElI674VVpEXeIPEcx6nrwkOyYUyfXNJltXhhHtaB6eLbgipJ5oeJfZW7xMZRMEavLkQVYnujlCBoa8y4njHXfA_kR19kA0ged3PH7jqZGRvo3ob2SIeQD9ELOSY76eTpX-jDv4xNHc-ZT998VUCY-phVeG9Dp8znjZ8C11OjVVhJlTwZ96Yxt2BgFNkXI18eCs-768sfk9JznOjNnESbirn0zPmW35dnjzFwRZ7Oth2viC4sKa8FjAGjAsCrm4mdhNkH9GYjhbbOXmRNtcNBW_LAtoR8gvmt1OR2qo3l6T0FxbSudAZekDswSOrxdgIRuPf23JF5S0-6MHX6fkAMepwwueAIbrWmTlcCaeUzEQwrYfU-9XpO8aYjzeLgqqeFVcQoHjz23rE0GOQVmTSTcVMDL02xhnoqMmM-BEcjvCcMPA6EcRCz8mNdPmPog1_VpWJCmn90BBOlOgoWnS-x9xV6geIbMtQ_iF_msBgCdggn4f35QkR1wPpktkn3StYCDhUjanqMIwaly4c-Jw217Seq5crqJGyGqkcfLu8_5jwF4MzplJg9HUwpQhW5ZwfiLGDQoq0PuYc-my23zv3W6cdhU-qgz_lRG5XZLK0oSBqjj6XF82t2JnWdkhH9AHn5qml3ZNzvnKocBx-nhT6NmCV4W5kPlA=w790-h477-no)  

The convolution with kernel H2 is shown below. This is the LoG filter and is the second derivative of the Gaussian. It will detect edges of the image.  

![](https://lh3.googleusercontent.com/bfSmZmPDlH2grqWuFhTO21V7wBXaxhKRmUIICDvXF_84XfbwqJGjjyvtL_nu8diG71xmGcUlrditDie-75cFAepvGpXfsT2DWDnSZ3Njkkjd2ZcGE0qrbVQkGzwVCJSJA5iZcFXd3jBxpoNv3nElEP7KzwE21XRSGsNaIwb6FLROVyUOsM3jn0G520EttRXl3tTfhPF442byDMSggzJz2s8ofgS4BFDZr-QcHKeRmQOiyKUa1WeuT_EQBkn-_0inWgpjQfuOKLJt9tkyOjiUBWBiM4d6nhGgli5apIQEvqnxjmnayKPKmxXjI1fzBgzUj78GeZ3hsEzfhKHBcewDte8shE7RUmhso3gYegRk4G0JS_UYNm_aOkcOYZoNdxbYh7A7j_aETJ1FeR32hGI1Tdz4bQi8hCZWXLoKN0QHzNrDKHP6Pf4LiT-HLKkGNYaqlNCuccYyUtHyVDehidLgBF05BBGZ4iJnj_k6bRXRiNtnRSVB8cELowYb8v6r8oP4sTGjWhtty6Rc_zDVShDtofrAecd34UAnXJhGkfzXs3F2xro7XZtaoGe5nihDR4T_7a8HdVusBhHOeM9MjbYj8VVLN2p5DcI3oVmGRvaDnKfz1gzKAY8vdAMGsMF0YYYYcMWRBzvs2YsuGJ6jK10GO4WvnRfegNK3Iw8ughk0hVjhrqH-fAigBg=w790-h477-no)  

The convolution with kernel H3 is shown below. This filter will sharpen the image. However, it may oversaturate the images, creating spots of white where the pixel values are greater than 255.  

![](https://lh3.googleusercontent.com/iMx0Qz2kZEh6BX3sJ_1-F-bqtEgCTP6A4lGbQzausrqQlmtA30QORsVB8CWepRdTf1cdvAOEFFMPzKsGLdDEQ8JIuamhcxtAtk4aSzWS8VXdNCF6rgDIMzV64eSXqT1GXv9gG4OA1XZyGLHEAx6-6k4TVfemlASjybx7kKwAjr2zCAJMT6kemvZZgCcKGQzGac6LZLqUf1SuPZceOybo5u2dPiJb3DEIkQMlfxSYL8e14k-Lr1uG21JQ30Gl68If-MYdfulaXcvMEFu0o91wyH6DYOkVKavh-1hLUynp2fH9OlfI36NDhjtVWjUbEcgWbTob_YAqs3TSr6xKvZhbxL7OHDt6rEYsLPtoIK6P4PoCekaEzOa7JoTjXL7c1Ub9ETk1QDz4bFkJRoH6ul5SwxXG9j6U5aarF7VFpiRuhoblscWoTTXffgx7ZVnCI2PaNz023BepPMkUBTcNuWs4PiAY9lAamBfT3HfScsp2fMrPc2J_r4Qcnq9NGPdhFZD3qhYrP_Swag_Igbv72ghygMSi4qksZp-ANaIw4-Qsw5gwRQ55acsy9Ll-1pscd4vcaee6c0Q4Sy086J4knlXXLpCs7eBYPHh3EW7HoreiusqXl8eiKqNkNjLy6J0i-5xM8qobKtkJLD-TCZhgyy9YyVP6z7rSLiofkpt-nh0dpdcRtnOyMH7usg=w790-h477-no)  

The convolution with kernel H4 is shown below. This filter will blur the image. Additionally, this filter will also increase the brighness of the image because the matrix sums to greater than 1.  

![](https://lh3.googleusercontent.com/Qf6GhZJFQ-wNaO8hqBTm7h0eL_OOHdNtCeZUhdKwKcByWAQ9Bcnhh_0rMOejObfxz-6PYnYR88GQHdppIHR3agKiLg4DDIGAjLA4Ml18Cp5sTC6Gs6sQcec7kfum1jClkUawTIfclBZ3fId3-tl545YEPL5iscb9NZhQhrA5FilrIOSO5zgdbud_AacjLMu0SgpuUg7UJteUZK4ctimIxEOEUlD3DKhD6TTekpfM4wk738IOsDHyNdyCBkYMrfd5d-F2F-VQJeHywwDVhSil6m-XIRXQFpZEWwKQROlSpk0z59gXh_e7wROiEW03AWucln7U_2EH3ZcNXnLiPNFiC4LDBoqjQu9cip9kRd1fM9b_fb7E4RZU4IQ2jlylBBHWCWiD7IQMTQRnwSggkzs4YJEx9Yq7tbddwyaHX3AX0cRcoptUenTPCFGttPILWXixPO-S1RhKAFaOcU6RF4IkptN025PRpURnt8rs3sYUa9JCkTeUWVTiGrZvsGHjgfFvXZbMHwtDmCDe7NBAvHQrAWXWeS-Hiwr4MmahdGad2u6Ujc1RLzB7QBTggEiYyf5qJPoRYWFxHJOxlof2wLFybRhqpk7emNioHIuPmFy9UCUI4lUVPSSF9j97vqDebyBTE46iXreaVcbS6MUML39ngysgrJKuCXBWdNvoIab1Z9jOxS5kJCZoLQ=w790-h477-no)  

```matlab
% Load image and resize to 250x200
temp_image = imread('problem1.jpg');
imSize = [250 200];
I = imresize(temp_image, imSize);

figure(1);
imshow(I);

% Define kernels
H2 = [0 -1 0;
    -1 4 -1;
    0 -1 0];

H1 = 1/9* [1 1 1;
    1 1 1;
    1 1 1];

H3 = [-0.55 -0.55 -0.55;
    -0.55 5.4 -0.55;
    -0.55 -0.55 -0.55];

H4 = [0.003 0.0133 0.0219 0.0133 0.003;
    0.0133 0.0596 0.0983 0.0596 0.0133;
    0.0219 0.0983 0.1621 0.983 0.0219;
    0.0133 0.0596 0.0983 0.0596 0.0133;
    0.003 0.0133 0.0219 0.0133 0.003];

% Since baseImg is a colour image, split into RGB channels. Perform
% convolution on each individual channel, then combine back into image
% Kernel H1
IR = I(:,:,1);
IG = I(:,:,2);
IB = I(:,:,3);

IR_H1 = conv2(IR,H1,'same');
IG_H1 = conv2(IG,H1,'same');
IB_H1 = conv2(IB,H1,'same');

IR_H1 = cat(3,IR_H1, zeros(imSize, 'uint8'), zeros(imSize, 'uint8')); 
IG_H1 = cat(3, zeros(imSize, 'uint8'), IG_H1, zeros(imSize, 'uint8'));
IB_H1 = cat(3, zeros(imSize, 'uint8'), zeros(imSize, 'uint8'), IB_H1);

I_H1 = IR_H1 + IG_H1 + IB_H1;

% Kernel H2
IR_H2 = conv2(IR,H2,'same');
IG_H2 = conv2(IG,H2,'same');
IB_H2 = conv2(IB,H2,'same');

IR_H2 = cat(3,IR_H2, zeros(imSize, 'uint8'), zeros(imSize, 'uint8')); 
IG_H2 = cat(3, zeros(imSize, 'uint8'), IG_H2, zeros(imSize, 'uint8'));
IB_H2 = cat(3, zeros(imSize, 'uint8'), zeros(imSize, 'uint8'), IB_H2);

I_H2 = IR_H2 + IG_H2 + IB_H2;

% Kernel H3
IR_H3 = conv2(IR,H3,'same');
IG_H3 = conv2(IG,H3,'same');
IB_H3 = conv2(IB,H3,'same');

IR_H3 = cat(3,IR_H3, zeros(imSize, 'uint8'), zeros(imSize, 'uint8')); 
IG_H3 = cat(3, zeros(imSize, 'uint8'), IG_H3, zeros(imSize, 'uint8'));
IB_H3 = cat(3, zeros(imSize, 'uint8'), zeros(imSize, 'uint8'), IB_H3);

I_H3 = IR_H3 + IG_H3 + IB_H3;

% Kernel H4
IR_H4 = conv2(IR,H4,'same');
IG_H4 = conv2(IG,H4,'same');
IB_H4 = conv2(IB,H4,'same');

IR_H4 = cat(3,IR_H4, zeros(imSize, 'uint8'), zeros(imSize, 'uint8')); 
IG_H4 = cat(3, zeros(imSize, 'uint8'), IG_H4, zeros(imSize, 'uint8'));
IB_H4 = cat(3, zeros(imSize, 'uint8'), zeros(imSize, 'uint8'), IB_H4);

I_H4 = IR_H4 + IG_H4 + IB_H4;

% display new image
figure();
montage({I, I_H1})
title('Convolution with kernel H1')

figure();
montage({I, I_H2})
title('Convolution with kernel H2')

figure();
montage({I, I_H3})
title('Convolution with kernel H3')

figure();
montage({I, I_H4})
title('Convolution with kernel H4')
```

## Problem 3: Gaussian Kernel

a) Code to create a gaussian kernel is as follows.  

```matlab
function k = gauss_kernel(m,sigma)
% Computes the guassian kernal of m x m size with specified sigma 
% The computation is capped at 2 standard devations from the 0

% create two meshes to represent the x and y coordinates
[x,y] = meshgrid(-floor(m/2):floor(m/2), -floor(m/2):floor(m/2));

% compute gauss 2D
k = exp(-(x.^2 + y.^2)/2/sigma^2);
k = k./sum(k(:));

end
```

b) Both kernels will blur the image. The difference between the kernels are the sigmas. The larger the sigma, the blurrier the image becomes.  

![](https://lh3.googleusercontent.com/FDVZCRx_82yhMToazV-tOZEx1A9W8Iu0DeM3FblULVDM-NGwQ_hmxiqhW_h4wEzHGAS_xUvSaoQgautFr-1VJHv4ixycXhRt_Gstc0OL2ycBvgTEIPWssnyeTNvpVz9NSR3K4-Cra-6WkpsRm2MXtvk31G89nCQD4YbwmHORweOnW-2x3bZ2eIf58NpL8CuPBqJ3Ah0cTrKPj-UrPbs1EoPNh2SfxPrqJtqsbiq8gXJC6QI3ixek7W7my1pmoJXMRsGSfMpa-j6uvorpkUqW62drXXGXh3Wgtcb-aVUBZkahiXe4d8z_waZYa-CrnAPnOWJd_RXLk0iupZaTiKEVHpi_wOHxPsO0gg2cwS5e3Mb9Pzr0fO1uRLYn5W8MjRv1iPrKq_xtBpoVcy7-gPEHYpK6IJWy8vgo4y5Z4bkWZNKWf4oblb0YxnGfdSQWvQPz6kgHqfIuf8qjOlkWf0pRQXbI_z4SXdMUWEOICxB58ArS8Kvzfa7nGxONmtQMtTuKekFk-zbk2aSLZVQhfNRgNAYorLHAnWRV43VOf45l1qWbagUZh2XzkUytiZ0yJkBSCjHRshWvAXffQHe2MT3Eiq2IVtiv3HZVAWBKd2ftSb1M4dugLHLkhPveTs7AqZgkjZHwD_9uzRDzC1172SLNdmA3K8a1uVlZOw9Ix7N6GNS6DUuA96OaCA=w942-h477-no)  

![](https://lh3.googleusercontent.com/bOTUImY4goB6WUEa1xc03DupSkuD48oKE0zFEpKGjpgxLjgkl9aFKmuKSyT5JG541dWWF_zuVq-5cE0BQ5NmZT9yIPuXkTwygneaYOXeMBDG6RD7nSI7qKOMQdv9E0lmvIZg-yX8k28smBIgNRyAkWStCWqYKzIGqeM2HYZJ4dYWgmxg0FFqSF9vZmzBA4cvP0mUS2OVbTglMpj0D8otm4bqQx_VkBpMX8ZlwvF-NMzeH76esE3wD26LUimd2hqE16RFrNHjSjSAuHMq5C9kR3C-fOM0Ane3uBTgkJGBGXkQn0mM0aofTE-8qxnW_fihOYT9VPYGb0QRNoukzwH3z_NH2ZIKCR4RVyI5lT3OcP_qo14SF8FoyV4KRNae4XJ95DlY0IGqHSu5P0qb5NDTx2UOu5o5F3K8rnDWfB8op3hElXVmxjbvDtNyeOLqFzpgY1BpfrgJjMesZWwTL57PkQEvH96W-mKtMNUm7sGZWzF28-7D4Udx6u32LHOZiyTAGoroR3YPmFrcM7bHtndEjjEuMO4dBj0b8lXplvquhh-cJySmxNGXs_h4UoeI-bOYeywiLG8Q1ZCc81R6VxE8UQKMDA1jo5L6OvHXRz0qK9Urg5ebFkKavA6HRS-mFOVyOjXTrDy9qZgfmC0MDDjCguYYJJBOKSel6u70QupJ9gdmLCOaiEqGXQ=w942-h477-no)  

c) The sigmas of the kernels are the same, meaning they will blur the image to the same degree. The difference lies with the kernel size, H3 is larger than H2 by 30. The bigger the kernel, the better resolution the blur of the image will have.  

![](https://lh3.googleusercontent.com/bOTUImY4goB6WUEa1xc03DupSkuD48oKE0zFEpKGjpgxLjgkl9aFKmuKSyT5JG541dWWF_zuVq-5cE0BQ5NmZT9yIPuXkTwygneaYOXeMBDG6RD7nSI7qKOMQdv9E0lmvIZg-yX8k28smBIgNRyAkWStCWqYKzIGqeM2HYZJ4dYWgmxg0FFqSF9vZmzBA4cvP0mUS2OVbTglMpj0D8otm4bqQx_VkBpMX8ZlwvF-NMzeH76esE3wD26LUimd2hqE16RFrNHjSjSAuHMq5C9kR3C-fOM0Ane3uBTgkJGBGXkQn0mM0aofTE-8qxnW_fihOYT9VPYGb0QRNoukzwH3z_NH2ZIKCR4RVyI5lT3OcP_qo14SF8FoyV4KRNae4XJ95DlY0IGqHSu5P0qb5NDTx2UOu5o5F3K8rnDWfB8op3hElXVmxjbvDtNyeOLqFzpgY1BpfrgJjMesZWwTL57PkQEvH96W-mKtMNUm7sGZWzF28-7D4Udx6u32LHOZiyTAGoroR3YPmFrcM7bHtndEjjEuMO4dBj0b8lXplvquhh-cJySmxNGXs_h4UoeI-bOYeywiLG8Q1ZCc81R6VxE8UQKMDA1jo5L6OvHXRz0qK9Urg5ebFkKavA6HRS-mFOVyOjXTrDy9qZgfmC0MDDjCguYYJJBOKSel6u70QupJ9gdmLCOaiEqGXQ=w942-h477-no)  
![](https://lh3.googleusercontent.com/xnGPi6Q2IdM9R3HGcj6Mh8TVFpAemCRnTyqhSmzJuiYHrP__d4KrH1yfFly2WvTFGSYWN6ybKmIgY2WY1tKsoTO-2_1NGFcn_kO3dqniRZSh2Xl9rdsUtsPFABLxKHdmM7cDpIQIQlAFUX6Mr1IGxDfi8gJx7hF9vJW02T5_9dCUrA_GRNno0FsGZrNcxi_zF5ZyefdMIKKUb0pO0RZ2Dazys3eE63Xuzudj-gAjA77zBslvMeGe1PUZ_LBA8sEXSLXmvy_HW90j1eXDzvtRcYRWpRmRQxOPHxYxczspz6j3WWG1v8QglBHDMwzHg-CZpA3t9qahymmqB5WyAapw8qar1JLL6c98OkZjYf71BhDcvn-oq7BWsUmMSKq8afDE4vwPJ9ev-w8SqBMdVvl9L1zufm3sslRzyvWX6YTjuoNkCX-7ChdvglDLNz6TmzNB9eGeS9HYpw4fiqZ0m6fVyp80-Mc2OOoQg9mK42N4Lr6diZAH6PzrFPE9rwoOlZB0sXZBbBv6cGg2VLmCOz_0YO-bE8KnLmQqQN_FqqGiutSPXXEaJ1VRVuKAIfmYJ_FJK1Wv9qzFEGKrMKZQHPxmQxmcLWsdpwe8KMoibXjCaY3ZdYoWtPW1eD9lYNEOCOHCYXkUh7zHeBWjeRNPj_tmM0cclGuWTlOTk1hXMevVI3DcKDJCI7k8cg=w942-h477-no)  

d) Again, the sigmas are different and the larger the sigma, the greater the blur in the image.  

![](https://lh3.googleusercontent.com/Zacwzr7zg75M76b3t6EW7k_CNRmMkL9MA-T_ycSziPbFwgjTxtgVQSV__VMDmRoDV0otoejRATL2neTDNBIFGMkA_uhKBGuQSXSzoIGzQk7u4fZbq_FDfgAUqt9kySRjWyRxBJ4-sasIuAF8H-sJvzzB01ukG_a7B-Q6a8TJqS5gf-Q8eLOHi1oZ9wUOQKFO3ajZmm0zF7bH3wKGo6aau14PL_g4hZAb-yz_mygbdahWvZ6Gz6kdCotE9brxURujlFwECPlMZgOKxkFVSML4Ej70UP5fKyR62itZyv6Gzo53pLrCzkJQ8wOqU15Jpa1Fv4a33z-tay_DiMv7tJPgIMpHYtnohwXvaJnTZujANRlWWjFAwpnt7np02O43Fb7TTIpVh93OjDOTVjG4xjqQpHFoLWqTjDAfkRwEFxfF2jPCS47M7H3AI2eQMo9_eySm_3opadvIl0zo0o4__EJgsSMNMgqFXmhyrAZdUfAjfi0YsPW6rHQXVsr3Oj1iOEH0x7XCYCGrFqOl3xo_rkrjx3eSZmq8YESxOX6k7WQ6neZSi-KRVcJiQV0zs8WbMMWNU5Zn11tPOV5w3ZvQP7X0TEs2xUOkRAIla19_ze7npeFNEOUTys4OFc4XeiAFjM40Oi03GADcInWVhkbUCQoFjQngz5GvC7EozbiVLeefHS09PVxrEL6EAw=w942-h477-no)  

![](https://lh3.googleusercontent.com/TYeSBWGptMIS2l0_377BSaw8zFstpCp1BRxlDNipJBOho7UJO2A6EGpCYu9dNNNnwF7Ft4JpztV3MALKVKpNSoeKle2QCoT-dbBND5KGerFvrbhprbnSv4NmkAd6FhCKLQuINdcN15LL7A3ApU__ez_uy8JFV_4eOV_ktVjpeCN7fn0yy1znOMqHjB-PWAKLk6Iq6N8j3vnhlW4CcuXNjPfHtGkd5oeAYn9-O98M_cecj_tBO9YLjxa-setjQEpAMUoRl-hHiddCrZdbZ4s3h8byPWBbmN6stkihF8hILZZrGPV3PfIZt-aMkfIKcQNxAx8fKZf2iTJITqr8W617LizB_Ss7SP0dNrKRp_IqhDLTyHjLH67cXfbEMe87YTRcW3GsiHO1tNgPIjdewb3TJGPgFxM8yiqcBM2Ba7T73thWORk15_i1B3TUskHQNJWMYBhpDOZL2E5hoiwYZcaS2CGcvL3MEgW2GKZUj8ft4zRZPgkSZIxIcW0edyYD-3Nkm0pzCWrdlXSqWRzOFwyhIRsaxnBFU-JH3AEIGJeTe3MxnhZeJvsbgDM8jJ7DnYPDx8NRizTUiMnI94blPcvoFw_DuH0ZsI5jnijfPtDhJsnhvXzDsQKV9USsPTD7Xo6DcY-0JCUZy_1M5KIY1k_XxfganE9CPQhRxIBLKpM4qDFyeYYWpwGVDQ=w942-h477-no)  

```matlab
% the code to apply the filters is trival so a sample of it is shown here
% Load image
I = imread('problem3.jpg');
I = rgb2gray(I);

figure();
imshow(I)

% Define kernel
h1 = fspecial('gaussian', 20, 2);
h2 = fspecial('gaussian', 20, 3);

% Convolution
I_h1 = imfilter(I, h1);
I_h2 = imfilter(I, h2);

figure();
montage({I, I_h1})
title('Convolution with kernel H1')

figure();
montage({I, I_h2})
title('Convolution with kernel H2')
```

## Problem 4: Hough Transform

Code to compute the Hough transform is below. Note that I could not find a way to automatically extract only the edges corresponding to the cover without also extracting false edges in the process. I hard coded in the extraction parameters for each picture. Additionally, I was not able to determine an efficient method to sort the corners of the cover (as top-left, bottom-left, etc.), so that aspect was hard coded in as well.  

```matlab
% Hough Transformation
% Author: Chul Min Yeum (cmyeum@uwaterloo.ca)
% Adjusted by: Kai Yang 20640696
% Last update:: 03/08/20
clear; close all; clc; format shortG;

%% Parameter
bookletSize = [24 31.5]; % cm
bookletImgSize = bookletSize*50; % output image size
dirImg = 'img'; % image folder
dirOut = 'out'; % output image folder
imgList = dir('img/*.JPG'); 
nImg = numel(imgList);

%% Processing
gauss_sigma = [8.5, 11, 8.5, 8.5, 10]; 
c_seq = [4 3 1 2;
    4 3 1 2; 
    1 3 4 2;
    1 2 4 3;
    1 3 4 2];
for ii=1:nImg
    img = imread(fullfile(dirImg, imgList(ii).name));
    corner = FindCorner(img, gauss_sigma(ii)); % find ordered four corners
   
    H = ComputeH(corner, bookletImgSize, c_seq(ii,:)); % compute a homography
    
    [imgTran, RA] = imwarp(img, projective2d(inv(H)));
    bookletImg = imcrop(imgTran, [-RA.XWorldLimits(1), -RA.YWorldLimits(1) bookletImgSize]);
    imwrite(bookletImg, fullfile(dirOut,imgList(ii).name));
    
function corner = FindCorner(img, sigma)
% Computes the corners of the book cover
% NOTE: can only compute 4 unique lines. This does not work if there are
% false edges in the image. Adjust the sigma until only 4 lines result.
% Will require trial and error through changing the parameters of the hough
% transform.

%% Parameter
I = rgb2gray(img);

I = imgaussfilt(I,sigma);

%% extract edges
BW = edge(I,'canny');

%% Compute hough transform
[H,T,R] = hough(BW); %, 'RhoResolution',2,'Theta',linspace(-90,89));

P  = houghpeaks(H,6, 'threshold',ceil(0.4*max(H(:))), 'NHoodSize', [111 3]);

%% Extract the lines 
lines = houghlines(BW,T,R,P, 'MinLength', 250);

%% Plot the lines (for testing purposes only)
figure, imshow(I), hold on
for k = 1:length(lines)
   xy = [lines(k).point1; lines(k).point2];
   plot(xy(:,1),xy(:,2),'LineWidth',2,'Color','green');

   % Plot beginnings and ends of lines
   plot(xy(1,1),xy(1,2),'x','LineWidth',2,'Color','yellow');
   plot(xy(2,1),xy(2,2),'x','LineWidth',2,'Color','red');
end

%% Deterime the equations of the all the lines in the form y = m*x+b
line_sz = size(lines);
mb = zeros(line_sz(2), 2); % y = mx+b

for k = 1:length(lines)
    mb(k,1) = line_coeff(1);
    mb(k,2) = line_coeff(2);
end

%% Go through all the equations of the line and remove similar lines
mb_unique = zeros(4,2);
mb_temp = mb;

% loop to remove similar lines. Every row in the mb matrix is divided by the
% first row of the matrix. After division all similar lines should be very
% close to 1. A threshold value is specified such that all values within
% the range of the threshold is assumed to be the same line.
for n = 1:4
    mb_unique(n,:) = mb_temp(1,:);
    mask_m = mb_temp(:,1)./mb_temp(1,1);
    mask_b = mb_temp(:,2)./mb_temp(1,2);
    mask = cat(2, mask_m, mask_b);
    
    threshold = 0.05;
    mask(mask <= 1 + threshold & mask >= 1-threshold) = 0;
    mask(mask ~= 0) = 1;
    
    mb_temp = mb_temp(logical(mask));
    mb_temp = reshape(mb_temp,[length(mb_temp)/2,2]);
end

if size(mb_unique,1) ~= 4
    error('Cannot identify 4 unique edges');
end

%% Compute corners
corner = corners4(mb_unique);

figure();
imshow(img); hold on;
plot(corner(:,1), corner(:,2), 'g^')
end

function c = corners4(mb_unique)
% computes the intersections of the quadralateral bounded by 4 non-parallel
% lines using homogenous coordinates
lines = [mb_unique(1,1), -1, mb_unique(1,2);
    mb_unique(2,1),-1, mb_unique(2,2);
    mb_unique(3,1),-1, mb_unique(3,2);
    mb_unique(4,1),-1, mb_unique(4,2)];

% every line will have 3 intersections
intersection_x = zeros(4,3);
intersection_y = zeros(4,3);

% find all intersects
line_index = [1,2,3,4];
for n = 1:4
    compare = line_index(line_index ~= n);
    line1 = lines(n,:);
    for m = 1:3
        line2 = lines(compare(m),:);
        x = cross(transpose(line1), transpose(line2));
        intersection_x(n, m) = x(1)/x(3);
        intersection_y(n, m) = x(2)/x(3);
    end
end
% For any two lines, there will be 4 unique intersection and 1 common
% intersection. The quadrilateral will be the 4 unique intersections which
% has the minimum area.

% Compare lines. Compute area of unique intersection.
quad_area = 10^15; % start with an arbitrarily large number
quad_points_x = [];
quad_points_y = [];
area_compare = [1,2,3,4];
for n = 1:3
    area_compare = area_compare(area_compare ~= n);
    line1_int_x = intersection_x(n,:);
    line1_int_y = intersection_y(n,:);

    for m = 1:length(area_compare)
       line2_int_x = intersection_x(area_compare(m),:); 
       line2_int_y = intersection_y(area_compare(m),:); 
       
       x_common = intersect(line1_int_x, line2_int_x);
       line1_x_unique = line1_int_x(line1_int_x ~= x_common);
       line2_x_unique = line2_int_x(line2_int_x ~= x_common);
       
       y_common = intersect(line1_int_y, line2_int_y);
       line1_y_unique = line1_int_y(line1_int_y ~= y_common);
       line2_y_unique = line2_int_y(line2_int_y ~= y_common);
       
       area_temp = polyarea([line1_x_unique, line2_x_unique], [line1_y_unique, line2_y_unique]);
       
       if area_temp < quad_area
           quad_area = area_temp;
           quad_points_x = [line1_x_unique, line2_x_unique];
           quad_points_y = [line1_y_unique, line2_y_unique];
       end
    end
end
c = cat(2,quad_points_x', quad_points_y');
end

function H = ComputeH(corner, sizePic, c_seq);
% Computes homography matrix

% define corners for original image
x1 = corner(c_seq(1),1); y1 = corner(c_seq(1),2);
x2 = corner(c_seq(2),1); y2 = corner(c_seq(2),2);
x3 = corner(c_seq(3),1); y3 = corner(c_seq(3),2);
x4 = corner(c_seq(4),1); y4 = corner(c_seq(4),2);

% define coordinates for original image
x1_ = 1; y1_ = 1; % top left
x2_ = 1; y2_ = sizePic(2); % bottom left
x3_ = sizePic(1); y3_ = sizePic(2); % bottom right
x4_ = sizePic(1); y4_ = 1; % top right

% define homography matrix
A = [
    -x1  -y1  -1   0    0    0   x1*x1_   y1*x1_   x1_;
     0    0    0 -x1   -y1  -1   x1*y1_   y1*y1_   y1_;
    -x2  -y2  -1   0    0    0   x2*x2_   y2*x2_   x2_;
     0    0    0 -x2   -y2  -1   x2*y2_   y2*y2_   y2_;
    -x3  -y3  -1   0    0    0   x3*x3_   y3*x3_   x3_;
     0    0    0 -x3   -y3  -1   x3*y3_   y3*y3_   y3_;
    -x4  -y4   -1  0    0    0   x4*x4_   y4*x4_   x4_;
     0    0    0  -x4  -y4  -1   x4*y4_   y4*y4_   y4_];
 
% solve H matrix
[U,S,V] = svd(A);
H = V(:,end)./V(end,end);
H = reshape(H,3,3);
end

end
```

The extracted book covers are shown below.  

![](https://lh3.googleusercontent.com/TQHpHoiaHFoBIuJC27kNulnYZfoiViHcj3UX8PQYBo7Hxy2A3fe3RQ8POR6d2VU2120Eyb3yYbRcWwWe2mHlIWzcRZuJu0P5r9aG_mXENBmmd_htKydzqXpC5QH9G9pYzdeov_jr9MRZCsr6fOwCDAKGCOhh90lsSCXq7J7Ho0fQKy_TLXkGh-AnU3H9zdjYx47RsOvOWa85JDwCH_1Mmyih6QzlU67HDT2XDJs1-y70BLEKfUqzw4IZozn3JQgFebeXFBU0abyFO2qZh5jd0XtmhRnCwyCqxYQNLkQl1PAqU-2yDgUCR7iqV0DAOqplBb8geoBvdcYp3BZNvuMmXyqqixR-g8FYoODeXPexIiyHDSV1R_Q4AlfAFXZYTPomZQFn4w3l-d2lU6jCHEtDfFE67JX1Jqv6o8o7Luzadg106m-vxpw07n-IYPoMCvaLHC_1RYwHXGNqAXKXVW-SxS-XAbJ4bNomkE17v_LCZ-Yp1CMOJY4gGRmkj6npDV06nI2WwonpSdMmFVSh4G8snpB8XkoXhnaAaYjASu0A9Lc33HEKbpMax1EH9p0Mm3PIrtI2qMFDoC8IOEW-neukF1N0L4guFQS90XQRwWEayH0VH5W_1qGZiJzt19hr3xUmMwf1C2fS-IrLz_PwKCwk3LXbo0QZulNiphqjJDDI3qNZwPOvJUJq6A=w477-h625-no)  

![](https://lh3.googleusercontent.com/KKy02Yb9i_jo0cfOjHG55T2pq3MdCRQKSja-I0SmLGC_LQpXu9he1F6JS-WDiEdle1zGKqO7SYDo1HqAOpXs8U0hRFu1o7mjgnNVrXLW_nd2kPjybD7dmoo1KbNTQyQkPjV1yFtZrBpVe9jCcq0OFaX4lTw4ULwzat0Fh8AEmP04fvdAbquiJSCUTMN4YwqWQnQWU7rmGqLeEf2g6XAH-m7Dv6s14fNmMljZGljJqCOtAlrD0aoqC2r2BvBKhaekYV79d1slcaz3_6GaFAz9k4IZo9UMKjjRfEZQLRvSGwfvmjAgA-IETUKOWspkS8_gv0g_m-rljL7-yum1kUUFFz5F1SK8bhaGZu7qgAY3EI6lONQHWZ1FTfLvvQdaGVNWXJ9cEISlHshC3VxpbOzjeahOc2qC2sLSM3e4Patek5MoX8SttkzurR03B6h0_hAaTAHm5HCsXmCEf7pyScOKWVbKvbc6iCxQx0wqslc3YxZOjJfuTYvjAhUScrfU-qmX43g2WRufe2E6iKJtJP81aUZVhZLSHlwi4cmAaLt7-BTWv-GsLkmFW_r8XXEu9ib2Z3zxXV39vhkmSXcxKGOwDo9aGfpXVAUorLo2GwEvOdICpKXdilnq39l5mvuqiMvD32VhBF4I6MjrNBoWQKLgGdSJBLBmQMA3shFX1RY3lqb9zRFdtXeeQw=w477-h625-no)  

![](https://lh3.googleusercontent.com/UR9gRyE8JpybR3Mbh45jlA449-JDP4lNzLS6w8Fz7aU8ZDw1JEAu4cjgnQfPK2imhjpXVap80zRiu4Ecaq1T25HbVo7J82evq8b4QuUu5ALlJNsQxsAi82QQ4pXrx9oCpfD1NjATHg0TwZBEtRBfi7vnHn1NzJ5rYdxS57GEELjQ_XLCA67v3SJqCEt1c1NoI1RIVwqumjFZPyJO8By0g5M4dzU9_ngn1SVIqGBZCrrwWZxHsTeaGAJ11IBSuqBaDqJJsBTxFf95jXB6Vpg4ObUklceHMTp5SyeG6SUkt78EUg83qG-WdnPU8dKInI3d5cEOtoZUlzprutCHCwkTRVEFhcMchWg8X7lp_0_YSSWPaOCJtMPZZh0XRb05U3xsT5wAw7N_mndt8UrkxJNDxuPgXn9mCbGEPnB69OhG6dcW8NiorZ9L2GiRHbrzTTP4azPfVuS8Yvnm7yRxj2InC_N7VyIQjDW8f79k9-cGqNOWNKekvAa5smwtDhZz0vKpZ8vypkpgoSqdilOwjHhoAcIrwCBHuhUg5qWsOmVkGNbw04EsGxIIS1pGH_1_sBkjpGAVHCwomDW1VCPRI-_nmG-B4ONsVa5ooY9zcRSbow7XIp68NI2m8HoNGB6fL3cuC6Vs7qZXPyuVg7416fsAipnMKzGkyz-6KrxDgsuHwF39XiwqBgmFSA=w477-h625-no)  

![](https://lh3.googleusercontent.com/pusXQyQM78MRe9MZfS1cNrL2oys9GvqP1r4tD-Nry8HftO5wZ9Xj16ELGtUrcixHEIIySWa1own4LuL7tOpJhRjGiS1NNAkFyeeBUc26hjlNJup9adOiQE0fclAMA_QrgmAHKTP6ys9JrL08Q1-18AljBUJt1CMSVeyzWzR2p4_8We91QNLI7-OGkjbBWwQg0pG2wCqTNpwOB10RZw5ZgVRcBtL1xKldFGiozzSw4Zty8XWTSJbWuoHcY1femwppkgpVIK83fBRDqdC90mBH2_cqzR1z_vNKtMVVkIk-s_KxkO5ZtxPExkNpAfE_b6Uy3PRXiu0F_Eoa-wMYdDQ7m5rxIfmnz2V6746h3kEnIEXhswXLNHrkf_9aR6JMYnui1_J7iGIlp1AXZ_E-n2Bt5i0I3zByodMmtD5w3tfOqRd1uNRpccf-jKIk3_2ZfWJtCouKM93P-9iTzFDAEmJ8djFWSrTIFT-rYqhHFJ6PGnDyeAUnrMpi4tctIJYtn__m2jcEKEd-3sRrKMisc73i-YILLdtUvlYsHJoSnejjzYqRSf6iJB774bs-1-FEXlSTM94GwIBuQDVESaYJrSY4En2JiW8rGBuJcpY55AqMXKFChAdMUpnKUU41pvqLFtFGWINtfS7GWhVnJml0d-d2_ldCX8fViwuIVSuIFmK-Z3zEnzzVa3Tjyg=w477-h625-no)  

![](https://lh3.googleusercontent.com/f81Nvrl8fvab_Q9UAs9huvv4bdYdjeoVcJnbQYo9nLi8S5s3voWIXBBMarFsk8YW4qiHkpKij4wOqbXq-jLXPqPRlI7bUeCvaspxbsZrpXjxchXwWb7_0aGlA4dckFFO8FS1qKLdM740k0w2NTf9ZHjGftEJFoiYEm0YAk24FftcDrwYRs_CH7X6Bvc6kRih3FaGI_hVyWn5NgwXKWhpH46sxwIWuTv1-nMmPrINbMNsdoXABxjmw2nBIATP6Yi7hXpgHwmkzDDrBFfTMHSQIJrTJ2ZMJKo55G8PdOENt9yuA-rvu4S0xIPAJ6utN2CBFJbvEk5-iFwhTWvgxp8JNcZJz6U_VepFByrXSbo0Y7hYLwbviEUg0wzKFBAMyWYq8fu6kcBlxaM0mJfIm2QC8aK0opk2UHo4axVaFonwfFJptDa1UkkG9iWeLq9JLJNAtypHkq-VkdgpxYsr0b8YZmDMLfirakiqyYAnAxShPqOD0G_zbg1As5l4HeGF_U2NTJxzSDEgyFkoF1dx_eBsYLvOhY0c8x8Wo0sluo9X7NaDH5lG9j4WoQa3Ax-YlglXU7QdMcbxWXcJjWZwQxvRnZtL49Ma_L53LMG-Ci1MDidVk6LsM4rxWfak5LHNCs7oB9M6ksOeK2Yzgz3ZNxWNtyFJWi66KIklRa9_eoW7hv0i4I777EzT1g=w477-h625-no)  

## Problem 5 (Challenging): Hough Transform & Image Overlay

This question could **not** be completed successfully. During the image overlay process, something went wrong with my code and I have no idea how to fix it.  

![](https://lh3.googleusercontent.com/M8kBrr5YOK5NfUTlXwBJSVKtyDYo5JQegWV_kUah34f0CYhOWSbMwnEZEJE4iA-sRhSmmSquv-l8OWgNkQ57jtiB279HohOqSdwlcPD7W47iSWsYgt8KB8mi9xlz_HE7-lX6EalKojn9f_OLgh8ptTkEXFfEOS5wTfYkRI-wGO05Sa2z7ffk9Q55yMmzycAlsoyRf0WOZ9nOa4B4Ma7fWpQF4m71-XVzd4XLbZGaLAImiyGOVIEB9FApq3ZByX40mxcrOI9qFDl5hykEP9z1ySDNOw59Ou0GlDSZE5ab9EyIQO4KTgx8TkrIni9VhGp-se4aOCURou81PR4pAjM7ZBNv27LANRnrTbMrAxbHZUou-K92Kc4V3exLCBC9nFCtUzxJKmIDi7zsO3mWmITpPaGWY74GBB7mhPNe9pL8Hrm9stPWHGhx4Uz8znoJzB0y4gBrFmHHzVg9oRiMa9JDe_vDYSoM2JqNaYOlvjZI4ieSWcmNCOZHciGwLZ6E2sO5nbnoWxFbsWJkraJQe325WhfarlRiqWa-4lGQ79NL684eiiFnnBPJQ_XVghgqUXwzhovcRcjL8B_TopcdjV8KpdkoVPzzHAkzS-KxPMbK5bgkl19drpl7cdMIa0HYnLlHmozSTRFPoKzPJ1HyeG3FujOtWRzj5EHN0XgtDdPte0h2lvL2HavcZQ=w1006-h616-no)  

Due to the complexity of the task, I decided not to package everything into a single function, fun_prob5. Instead, i opted to use several different function and do most of the coding in the main program for ease of troubleshooting.  

```matlab
% Hough Transformation
% Author: Chul Min Yeum (cmyeum@uwaterloo.ca)
% Adustments made by Kai Yang 20640696
% Last update:: 03/08/20
clear; close all; clc; format shortG;

%% Parameter
file_img1 = '20200227_104101.jpg';
file_img2 = 'IMG_0080.JPG';

%% Processing
imgBoard = imread(fullfile(file_img1));
imgPic = imread(fullfile(file_img2));

% Select the quad on the image. Go from top left and ccw. VERY IMPORTANT
figure(1); imshow(imgBoard);
p = drawpolygon('LineWidth',5,'Color','black');
corner_board = p.Position;

corner_pic = FindCorner(imgPic, 11) % find unordered four corners

H = ComputeH(corner_pic, corner_board, [4 3 1 2]) % compute a homography

%% Image overlay
[imgPicTran, RB] = imwarp(imgPic, projective2d(H));
BWPic = roipoly(imgPicTran, corner_board(:,1)-RB.XWorldLimits(1), corner_board(:,2)-RB.YWorldLimits(1));


BWBoard = ~roipoly(imgBoard, corner_board(:,1), corner_board(:,2));
RA = imref2d(size(BWBoard));

imgBoardMask = bsxfun(@times, imgBoard, cast(BWBoard, 'like', imgBoard));
imgPicTranMask = bsxfun(@times, imgPicTran, cast(BWPic, 'like', imgPicTran));

imgFinal(:,:,1) = imfuse(imgBoardMask(:,:,1),RA, imgPicTranMask(:,:,1),RB,'diff');
imgFinal(:,:,2) = imfuse(imgBoardMask(:,:,2),RA, imgPicTranMask(:,:,2),RB,'diff');
imgFinal(:,:,3) = imfuse(imgBoardMask(:,:,3),RA, imgPicTranMask(:,:,3),RB,'diff');

imshow(imgFinal); imwrite(imgFinal, 'result.jpg');

function corner = FindCorner(img, sigma)
% Computes the corners of the book cover
% NOTE: can only compute 4 unique lines. This does not work if there are
% false edges in the image. Adjust the sigma until only 4 lines result.
% Will require trial and error through changing the parameters of the hough
% transform.

%% Parameter
I = rgb2gray(img);

I = imgaussfilt(I,sigma);

%% extract edges
BW = edge(I,'canny');

%% Compute hough transform
[H,T,R] = hough(BW); %, 'RhoResolution',2,'Theta',linspace(-90,89));

P  = houghpeaks(H,6, 'threshold',ceil(0.4*max(H(:))), 'NHoodSize', [111 3]);

%% Extract the lines 
lines = houghlines(BW,T,R,P, 'MinLength', 250);

%% Plot the lines (for testing purposes only)
figure, imshow(I), hold on
for k = 1:length(lines)
   xy = [lines(k).point1; lines(k).point2];
   plot(xy(:,1),xy(:,2),'LineWidth',2,'Color','green');

   % Plot beginnings and ends of lines
   plot(xy(1,1),xy(1,2),'x','LineWidth',2,'Color','yellow');
   plot(xy(2,1),xy(2,2),'x','LineWidth',2,'Color','red');
end

%% Deterime the equations of the all the lines in the form y = m*x+b
line_sz = size(lines);
mb = zeros(line_sz(2), 2); % y = mx+b

for k = 1:length(lines)
    line_coeff = polyfit([lines(k).point1(1) lines(k).point2(1)], ...
        [lines(k).point1(2) lines(k).point2(2)], 1);
    
    mb(k,1) = line_coeff(1);
    mb(k,2) = line_coeff(2);
end

%% Go through all the equations of the line and remove similar lines
mb_unique = zeros(4,2);
mb_temp = mb;

% loop to remove similar lines. Every row in the mb matrix is divided by the
% first row of the matrix. After division all similar lines should be very
% close to 1. A threshold value is specified such that all values within
% the range of the threshold is assumed to be the same line.
for n = 1:4
    mb_unique(n,:) = mb_temp(1,:);
    mask_m = mb_temp(:,1)./mb_temp(1,1);
    mask_b = mb_temp(:,2)./mb_temp(1,2);
    mask = cat(2, mask_m, mask_b);
    
    threshold = 0.05;
    mask(mask <= 1 + threshold & mask >= 1-threshold) = 0;
    mask(mask ~= 0) = 1;
    
    mb_temp = mb_temp(logical(mask));
    mb_temp = reshape(mb_temp,[length(mb_temp)/2,2]);
end

if size(mb_unique,1) ~= 4
    error('Cannot identify 4 unique edges');
end

%% Compute corners
corner = corners4(mb_unique);

figure();
imshow(img); hold on;
plot(corner(:,1), corner(:,2), 'g^')
hold off
end

function c = corners4(mb_unique)
% computes the intersections of the quadralateral bounded by 4 non-parallel
% lines using homogenous coordinates
lines = [mb_unique(1,1), -1, mb_unique(1,2);
    mb_unique(2,1),-1, mb_unique(2,2);
    mb_unique(3,1),-1, mb_unique(3,2);
    mb_unique(4,1),-1, mb_unique(4,2)];

% every line will have 3 intersections
intersection_x = zeros(4,3);
intersection_y = zeros(4,3);

% find all intersects
line_index = [1,2,3,4];
for n = 1:4
    compare = line_index(line_index ~= n);
    line1 = lines(n,:);
    for m = 1:3
        line2 = lines(compare(m),:);
        x = cross(transpose(line1), transpose(line2));
        intersection_x(n, m) = x(1)/x(3);
        intersection_y(n, m) = x(2)/x(3);
    end
end
% For any two lines, there will be 4 unique intersection and 1 common
% intersection. The quadrilateral will be the 4 unique intersections which
% has the minimum area.

% Compare lines. Compute area of unique intersection.
quad_area = 10^15; % start with an arbitrarily large number
quad_points_x = [];
quad_points_y = [];
area_compare = [1,2,3,4];
for n = 1:3
    area_compare = area_compare(area_compare ~= n);
    line1_int_x = intersection_x(n,:);
    line1_int_y = intersection_y(n,:);

    for m = 1:length(area_compare)
       line2_int_x = intersection_x(area_compare(m),:); 
       line2_int_y = intersection_y(area_compare(m),:); 
       
       x_common = intersect(line1_int_x, line2_int_x);
       line1_x_unique = line1_int_x(line1_int_x ~= x_common);
       line2_x_unique = line2_int_x(line2_int_x ~= x_common);
       
       y_common = intersect(line1_int_y, line2_int_y);
       line1_y_unique = line1_int_y(line1_int_y ~= y_common);
       line2_y_unique = line2_int_y(line2_int_y ~= y_common);
       
       area_temp = polyarea([line1_x_unique, line2_x_unique], [line1_y_unique, line2_y_unique]);
       
       if area_temp < quad_area
           quad_area = area_temp;
           quad_points_x = [line1_x_unique, line2_x_unique];
           quad_points_y = [line1_y_unique, line2_y_unique];
       end
    end
end
c = cat(2,quad_points_x', quad_points_y');
end

function H = ComputeH(corner_pic, corner_board, c_seq)
% Computes homography matrix

% define corners for original image
x1 = corner_pic(c_seq(1),1); y1 = corner_pic(c_seq(1),2);
x2 = corner_pic(c_seq(2),1); y2 = corner_pic(c_seq(2),2);
x3 = corner_pic(c_seq(3),1); y3 = corner_pic(c_seq(3),2);
x4 = corner_pic(c_seq(4),1); y4 = corner_pic(c_seq(4),2);

% define coordinates for destination image
x1_ = corner_board(1,1); y1_ = corner_board(1,2);
x2_ = corner_board(2,1); y2_ = corner_board(2,2);
x3_ = corner_board(3,1); y3_ = corner_board(3,2);
x4_ = corner_board(4,1); y4_ = corner_board(4,2);

% define homography matrix
A = [
    -x1  -y1  -1   0    0    0   x1*x1_   y1*x1_   x1_;
     0    0    0 -x1   -y1  -1   x1*y1_   y1*y1_   y1_;
    -x2  -y2  -1   0    0    0   x2*x2_   y2*x2_   x2_;
     0    0    0 -x2   -y2  -1   x2*y2_   y2*y2_   y2_;
    -x3  -y3  -1   0    0    0   x3*x3_   y3*x3_   x3_;
     0    0    0 -x3   -y3  -1   x3*y3_   y3*y3_   y3_;
    -x4  -y4   -1  0    0    0   x4*x4_   y4*x4_   x4_;
     0    0    0  -x4  -y4  -1   x4*y4_   y4*y4_   y4_];
 
% solve H matrix
[U,S,V] = svd(A);
H = V(:,end)./V(end,end);
H = reshape(H,3,3);
end
```
