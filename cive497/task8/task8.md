# Task 8: Neural Network

**Name:** Kai Yang  
**ID:** 20640696  
**Degree:** BA  

## Problem 1
For part 1 of this problem, I played around with the tensorflow neural network playgroud. As noted, no results are included in this report.  

For part 2, the following subsections will describe the demos in the tutorial.  

### Gaussian Demo
For this example, two datasets following the gaussian distribution were generated; they are (2,2) and (-2,-2). The goal of this neural network was to identify the boundary between the two datasets. This is a multi-classification task.  

The defaulted testing parameters was 20 epochs with a constant learning rate of 0.03. There are two input nodes and two output nodes (for the x and y values). A single hidden layer consisting of 5 nodes was specified. Activation function on the hidden layer is "sigmoid" and for the output node, "softmax" is used. The loss function is cross-entropy. The final plot is shown below. As this was a relatively simple task, the convergence of the weights and biases is fairly fast.  

![](https://lh3.googleusercontent.com/07zCKpXuAn7u4dhRypEQreF1sEWSzvdY28PopFDUMKTe-MjSyUNiyozLQHZsiWv_gPYtP3ZIKb4fBVX2RaPias7PbXI8-mmbHODDPJLeCDpiMY7Go5b1WV50CwZVkk_iyduVvE2l-uu86iVq3kg77PR43j9mCtx8GdFMmZx4jb1qt3F4dwg1iYEn3X7T4uVmocxKHlqDqtFj4jNdS4AhIC6Ymomm3dxHalUCOLZIWoS48IJY9N_fXwMXkyRKuh4bI2F-HIK4eyMI7tocG5uKmMwb139OdDW_4iG7iPb59G1ft9sEZtY5t0ZGpK-PqRfeQthnHh6Uiqqf3JdhYzt2OT9iU0xSXi9-Aii8sLyRTVj_SFfZuYI_lwY4QflFMStKNeRrP5ZDw5DxghLy_zRuI4NbcVBpvi_yxNwiflj25ZNjmAVV5yZ25hrGZ9armpFQqKBjqdNXcn6s0XnYQosBpWtGBl2KW59F1INcqWyNVqwW-sGUyIgwmRRYnxjBv3gjXo0QO4doG5hviSPt1u6E7194wkcwzeRKm8gchh2CmEOw9OT-J3EDeqNPhDxpZao43rUW0VS0c82ez4de2XP-gSWYa76T779nWUOfRyFH1LQMJMJdTin1wtZ_-nBhkBh9uyLgkMzfbNp_Rrf4G93GlfD_mqyYvF7mK2GlkxMwvBP1_EeOSbFu642iLagt=w1006-h465-no)    

### Circle Demo
For this example, there is a dataset of points clustered together forming a distinguishable circle. There is also an outer ring of points scattered. The purpose of this neural network is to identify the boundary which forms the inner circle. This is a multi-classification task.   

The selected testing parameters was adjusted from the defaulted values. The parameters was selected to be 10 epochs with a constant learning rate of 0.1. There are two input nodes and two output nodes (for the x and y values). A single hidden layer consisting of 15 nodes was specified. Activation function on the hidden layer is "sigmoid" and for the output node, "softmax" is used. The loss function is "cross-entropy". The final plot is shown below. Convergence happens relatively quickly; judging by the accuracy graph, 10 epochs may not be required. 

![](https://lh3.googleusercontent.com/JzxYpV6M8LX7u66eVjhMleeSsbfRXk9RiQr4X3977F1PiUJIY0rHjmcPj0gK2FcUmzzRvtewV_1wU1NiwoDWrUCZUTK2xNaqbVIEVynU9OC4PJaQV4Fp_eyJy963QlDoIoDEpHitIcWM_A1ghNeiX8WUulclcqXMKV_XiQjYvGQxDBIqIvo0MRtcjrzwM9WnOO8jqfcxcMUQsyZVNpZ0rJQECUbb-oPXr-kCoOQzvcEetwIAFpKuW_0m4say2uW1wy16RSHUt8pgcFfJM7L87nMRFpcGaX3gli1NZFt9rmK0O32cEGFq5ajyJKXAedI8RjFYuGlE6e7kGspouOduTU3ztJZQy2iBuNm4Ff4K2g8i2UEtZ38tsKN0ayt9JTTD_utYVt8xaWMNPtJHXZIrP_ZTrmOCUo5y3X0WOQhThWK12sv1aGckhXcDpuNFYGJvi0hRrlukDmIQi9EBvMemLsd8BOYIlUZf4XEIr0ekagfg0VvjCOX-lrhQp7bEEa1-v_8WGUo9ik3YoGEBl-vmRkBEHr7CBuEdtWhLvhgiC9F6fV-p-vWwThkK5XYvCqRtK4TOudKzFW_vDQELnbIqj4MPsTMmaoecqZ0MJpYr7gGZv1en1NDYLRyvU8ID1MpCHg87_1US_OfwP1iJr0ZoiJHB3NEbFijHVpK8168zzXO0erPZk4TDRalTUPox=w1006-h465-no)    

### Poly Demo
For this example, the neural network had to fit a line to a polynomial scatter. The scatter is based from a fourth degree polynomial. This is an regression task.  

The selected testing parameters was 50 epochs with a learning rate of 0.007. A learning rate scheduling of 0.75 was specified as well. There is one input node with one output node (given the x-value, the NN will predict the y value). A single hidden layer consisting of 20 nodes was specified. Activation function on the hidden layer is "sigmoid" and for the output node, "linear" is used. The loss function is "l2-loss". The final plot is shown below.  

![](https://lh3.googleusercontent.com/IXRAFxA_Hzgreua897-YDnpObeGKIc_5lWlUTj6Pek4xiFFTxcPt5FevPnKzl3YVlmde1awaw5kRg2BQvALmxPHLcESUgHXSCTAZ5IuqaQfQTkZ_VLdgnvSOWr7aNDYQVtN-jz2yLfxLhrBD9a9F3UBv6slqP-IqfCx-kzG-LaoJ10YTpFitWQ00DCaaFBT7P9CPmTpUx9mSGoVh3BZt4ijnL_Z7yQvXoi5EGnSttZRex9AQWjwOgAFK6kZTy1oo7lgocBDmBvsdyfc6uWKqCZlYZGT-egk7aiTwBDAPsKzBzmjwESl3B782QhwC8dFyvRUtQmF7l0qWcAyITYySkrda7ahbq6KXSzUb7L8v9KNUdM-zq7oCmvT2EeND75-_AswenxGfINWuslOAcKygoEj_WLJ_JiUyw6UmNR1ZGisIbtRsZpMSqGg55EBLxBpCJUKGUsn8U-P-q8vmU0IYk2oiaawG_BvVoeFMos3XOScza_FH31juXV6r9SqUYwaEqjiqAk9OkPcMRixQ_7iM2FbfAFto2oEi_JZyt-UKolp3ve4jYC7K85NQ2Rz90C-Qnd8uP2O2kP-zA1TKR3_Nhb7Ayq0V_hpea09B8X0u_OGIe4Mcx6OX039GfFbtEVnf_8unwj-pBHOb7RnFUDlrBsBjvFTalCzGKL-Ym2e1nRCtNEjztSkSmew5t_Qe=w1006-h465-no)    

### XOR Demo
In this example, the neural network had to perform a two-class classification.  

The selected parameters were unchanged from the default parameters as they appeared to work efficiently. 50 epochs was specified with a learning rate of 0.1. There are two input nodes with two outputs nodes (the x and y values). A single hidden layer consisting of 15 nodes was specified. Activation function on the hidden layer is "sigmoid" and for the output node, "softmax" is used. The loss function is cross-entropy.  The final plot is shown below. As noted, convergence happens relatively quickly and it may not be necessary to use 50 epochs.  

![](https://lh3.googleusercontent.com/IOFlVx_ZCgjUA8cXDT2Bch_ELj4-RSG8iXNC817uNI8UdeznPoMZNnjIB7mOdN4_KOc6CPCFVKjJbhVZIjeAg16Rh0SbxCSevJRkRc5_5nr-icqr6HNCFkarBlc1fbr1BTbS6xahP7TmWJkMp1Bn1R2ZpUZFoqXvz41-adhoApmuYGW7HSeRaNtRmr-iAiVTa2SczzVxvkjSeEMXmsGCZi2FQeaW2Uhe6x9BwRHpNmAvqKTlMnNL37G5KcScYaGVMp93OrpTSfDA5mJIk1JYviHvq5rA_TekDcYC0jZ_br-9j9bQZb6DYrBSq7egUsQYWe1kSMHnhYTpBsNjvN8vJYAEzPCSZR61tJDSUESQ0UpCLySOmCdn-1xzpVEHnlTJ33ORIl66Edp7R2-ywpOaQrNJ8E109KcNZE77rgik8pjeb0PB9xccKhIZccVqshaO5L1s4yhmsnmu3nDTLwmCrcMQ0cT2WoK__Busz_BpXBTupWApkvI5micsj-_JdnhGkESY7VUfE4OslXN7IEqLRcqKHcZLx4OXcSLyeAQI1er7JVwA2hUuCOcCmdTa8zz49r0yGcPe9Rg5TYevmCwBaHP0w9ZmFVfYGf1V6pgMrH2lbCzfQraukHQgeU9wN0TcWopXNazkfvipndUpM1cYzZbswur11U_SjcSdl7An2naz7ieKhGtUZF3q_DjF=w1006-h465-no)    

### Wine Class Demo
In this example, the neural network had to classify the different wine classes given the various inputs. This is a multi-classification task.  

The neural network parameters were unchanged from the defaults. 60 epochs was specified with a constant learning rate of 0.01. There are 13 input nodes and 3 output nodes (to input the various characteristices of the wine and output the wine type). A single hidden layer consisting of 15 nodes was specified. Activation function on the hidden layer is "sigmoid" and for the output node, "softmax" is used. The loss function is "cross-entropy". The final plot is shown below.  

![](https://lh3.googleusercontent.com/2povyZCoKGSqdRDdg888NzEd932BJt4gzaXoNFpunjWIb5AEXaAkIwd6_a337-1T1CRiKkxS0IyF4d5rxTZ_bHS41JT8NE8C_OrW1H6xnP8LAbn7-Mb4BDNVO1eatu1z7FNW4kGXjIvKYTx2sal0Y-OJDkslDgKsYN_y_110IK63DFSzLyPeBIm-4MDQ11KOOwqAUyZrqmDLqpXKJ3J_zFjmBDtlG5_6-YAz_Xa5iF0chG3aBI0E9Pk0ojTL9IToyey5Jlk6lQyB2N-YgtwNzBUGQ7jBbC5SKvwglZ7iWCzDLwd6zmjT254wBTTgNJuo0Jfo3A-C7ZoGh5sdD52NAcKklY2RocLyYc6HJEX0KaOIO_gW4u1_BOOGWauNSWaPQpFw67t1wHWunZCvPE6bdQ_PxPMVPxWcjuvwutuUQUszjBC8lDVHj9hFVRDB2jDhrJvqYNp-8nHbW2vJHykDFFS2cHasQeBQt8UmsukNvQTAzqWYijzOwHtfVHVNfnee4OgT4vROHIvHzNU3ywovo7_zsOcHHcaYQI2WN51oYgM48pQwGbzHgtVqKKJrQfkUZAgl9Ccb_zXCgWNFpWDgFklDPKBuv2KUwrC_NcEYwCaC0BVZwG0vo4cfb4svGQAwlghrOCpMgXCY-50Zy9Wu2FPRKOqVMstmQhfrZ7FO_Itwf4cxg5cv_U4z2JK8=w1006-h349-no)    

### Red Wine Rating Demo
In this example, the neural network was designed to guess the rating of the red wine given the various inputs. This is a multi-classification task. The rating system ranges from 0-10, so at first glance it may seem like a cross-classification problem. However, the rating is done in intervals (ie. 5.5, 7.5, but not 5.4 or 7.7). The example code models this as a regression problem.  

Nothing was changed from the demo. An activation function of sigmoid was specified for the hidden layers and an output activation function of linear was specified for the output nodes. The loss function is "l2 loss". There are 11 input nodes. one layer of 20 hidden nodes, and one single output node. 100 epochs was used with a learning rate of 0.005.  

![](https://lh3.googleusercontent.com/PvJKOt9e0SEXIJ9eyEj6IKMRB_yz459pA9tNMbbSDFl9lArbrZ6-CXhcO1DyGbngeMEztluPpbib8mToLlK9cjw85WGCWuuFRSoZg-g3cDUdZEDXtTikYsDnsyuz_XNnttVj9P5l7eYHea7ExB7fZTk3L1fkTGKuQ_Fs2zacZD9vF5YyHsY3kFWTdqDHbZPxv4c76d-QxnztFZKtLCcOmjf2ZSDfh-LLuMqm4JMh4Y1JdmMc7jqyq4aKC7D-Hw-P5NbDTiDLo8iGZxqvGYhAtwQitnciHdr47xNqVS1HYFQpHo9s1Kpu2OoIRxAOtEkTY4oghLXZh_tBQg1OOfXRlG_BezF6NC8HRRP0TjOtYqwGqPFwsoMNz148h0Muw4cEbKZlZiJNU8W2PNR5Pn6CP5KXQRV8pbcD_cgosh3zDlWCfYWVvpan6Pa1V3NJKkhQoLJgTA-tOkY268HDp0ezr4nA4xUF9ktRw9E4i1Wds_Zsr-HJXTXvc59u5YJfRH3nkj-D3a8p-KiGvh1Cs3uiBMYHq1wilhwjtqnGSgqAzkrvIkW1HMwtaTmj5LVhtDPv4XDjHqu5-eYjfMlQMTsG7jU4NPDAWQ38kuCeI4zpm93jLOvv69v0CkTsRNkZhbnatC_AWwZaSYNH0pAjCcb04pMfZ7VdQ2IGgDzQhNlaDLs6VWV1TRi9QS1INH0f=w1006-h349-no)    

### Car Demo
In this example, the neural network had to predict the type of the car given the data. Unlike previous examples, the discriptors of the inputs were strings, so they had to be transformed into numberical values. The output, similiarily had to be converted to numberical values. Ultimantely, this is a multi-classification problem.  

The neural network parameters were unchanged from the defaults. 60 epochs was specified with a learning rate of 0.01 and a scheduling rate of 0.9. There are 6 input nodes and 4 output nodes (to input the various characteristices of the car and output the wine type). A single hidden layer consisting of 12 nodes was specified. Activation function on the hidden layer is "sigmoid" and for the output node, "softmax" is used. The loss function is "cross-entropy". The final plot is shown below.  

![](https://lh3.googleusercontent.com/hHMToLegG1RbAZl3nGIiU13H2H8dTyl-m_ULvpq0cweg2uDINmsMSoF1Ecu5alVTSS7aBQpECV48lNoVEIwqMFCq2SDOQ2RbisN2X06To8G9uTFfjmFNlc5byfqyYZL2bQyoybXwCbqs6umzrJFZ8QJt5mKdenkJUwqtOoy-Fp_vLYcm2rPXmCckOgPcZEUdN6gKJGh86T6wDJOFvZbMFLeC1ddrxX_A8d3ELPaIcsFwX4kW6NwfHUHu-MZjHlL7kIVfhv5NKlLnfUBkqqRJD8NW1PLsoQy25NaFfbTdbZ6pu8eSh7T2IDcjujcxZe-iFYyqopUatWiuuTnnpFmo9RSHTD5BaX6OjPtjGgjba5MEaNKSst9z7QnT8EMRcdKT7Ozon0Ugf7iTRn9Zo6BpU-l7GGfJ1qqsxN0SBqeflRUXBGm1wTDHUx2HoW6RB59D0v3BC99bZg71MxOyq_xRxrExecJYG9D1LvSq0xAJwbH6L_Pc4Iy7dKtvpMhZYqfldGn__MP_jLZ6OK0i4bv4lJi8_ifdR-iMqTCxnhHhO5xG4b69DR5dWjQPdes2h7GfBwZeSx_3gXiw-4OuKF_VfDA_G2D6GIyBTC-aUvj1u3inVCm3UkU1eLfAMsjhStodmBbn1BGtpQIdeX1v169VgyBbMYxM6v8ETozvRWpkOCmw6TJhv5vP0zVsC65Q=w1006-h349-no)    

## Problem 2

b) The dataset I used for this question is the [Statlog (German Credit Data) Data Set](https://archive.ics.uci.edu/ml/datasets/Statlog+%28German+Credit+Data%29). The format of this dataset is a mix of categorical ( strings) and qualitaive (numberical). Essentially, there are 20 attributes (such as status of existing checking account, credit history, credit amount, etc.) which is used to evaulate whether or not the person is a good or bad credit risk. Ultimantly, this is a binary classification problem because there is only two possible classifications. A sample of the dataset is shown below; the last column is the evaluation of good or bad (good = 1, bad = 2). For more information on what the categories mean, refer to the link above.  

```
A11 6 A34 A43 1169 A65 A75 4 A93 A101 4 A121 67 A143 A152 2 A173 1 A192 A201 1
A12 48 A32 A43 5951 A61 A73 2 A92 A101 2 A121 22 A143 A152 1 A173 1 A191 A201 2
A14 12 A34 A46 2096 A61 A74 2 A93 A101 3 A121 49 A143 A152 1 A172 2 A191 A201 1
A11 42 A32 A42 7882 A61 A74 2 A93 A103 4 A122 45 A143 A153 1 A173 2 A191 A201 1
A11 24 A33 A40 4870 A61 A73 3 A93 A101 4 A124 53 A143 A153 2 A173 2 A191 A201 2
A14 36 A32 A46 9055 A65 A73 2 A93 A101 4 A124 35 A143 A153 1 A172 2 A192 A201 1
A14 24 A32 A42 2835 A63 A75 3 A93 A101 4 A122 53 A143 A152 1 A173 1 A191 A201 1
A12 36 A32 A41 6948 A61 A73 2 A93 A101 2 A123 35 A143 A151 1 A174 1 A192 A201 1
A14 12 A32 A43 3059 A64 A74 2 A91 A101 4 A121 61 A143 A152 1 A172 1 A191 A201 1
```

A purely numberical dataset has also been derived from the above dataset and provided by the uploader. It is not explained how the numerical dataset was computed, but it was implied to be similar to the categorical dataset. A sample of the dataset is shown below. For completion, both datasets will be ran.  

```
   1   6   4  12   5   5   3   4   1  67   3   2   1   2   1   0   0   1   0   0   1   0   0   1   1 
   2  48   2  60   1   3   2   2   1  22   3   1   1   1   1   0   0   1   0   0   1   0   0   1   2 
   4  12   4  21   1   4   3   3   1  49   3   1   2   1   1   0   0   1   0   0   1   0   1   0   1 
   1  42   2  79   1   4   3   4   2  45   3   1   2   1   1   0   0   0   0   0   0   0   0   1   1 
   1  24   3  49   1   3   3   4   4  53   3   2   2   1   1   1   0   1   0   0   0   0   0   1   2 
   4  36   2  91   5   3   3   4   4  35   3   1   2   2   1   0   0   1   0   0   0   0   1   0   1 
   4  24   2  28   3   5   3   4   2  53   3   1   1   1   1   0   0   1   0   0   1   0   0   1   1 
   2  36   2  69   1   3   3   2   3  35   3   1   1   2   1   0   1   1   0   1   0   0   0   0   1 
   4  12   2  31   4   4   1   4   1  61   3   1   1   1   1   0   0   1   0   0   1   0   1   0   1 
```

My neural network was written in python using keras. The results of the model using categorical data is shown below. The accuracy is approximately 0.7 and the loss is approximately 0.6. Note that the ```RMSProp``` optimizer was used because there were issues with convergence when the stoicastic gradient decent optimizer was used. ```RMSProp``` is fairly similar to SGD, which can justify the change. The code for the model, as well as all its parameters is included after the figures.  

![](https://lh3.googleusercontent.com/UYVk-_kzye1_fSpxEn1RRTaTz_Nx0WFvI5QmSDbLRzK_4Abu7fJTMKmOC0HIaHweXMgP0tS1zIEVsf4voB9JopCrw8wXpWLgMn8oNI1DQr1DoN_klsIWePxdsRTRCPG2LrqvY7GhZLehN0leDgaqzdIJ4Lzw3X0-pfEYSuSUQ_sF7bRTi5FU0pvXbN9Dy84bRXXDYQ8JwAADOw53RgW3_LR-PtHW3DVHVmwED2Zx7brfW3anz-OJCKC-xmHn7oNptPULMWoX7PzuXBeylRVpLw7EOroHi_ZKfApV37-MsvnHfpGR9iNshVcwqIHX5t3M0m0bbFsDZzRC6jyoHB2HBcFzWcF_BiXk06CiCy79tEE_jVpgJRMa4NOCSh2yBB6zUomNCJk5XPk-nQVYXcy396UJR3QDLBfnvew4pGfEtAq24tJjihop90MsIL1b2J1AsyLbdP9gANkB-DTjY0ixrNnuy-Kkh7H8IcF_DuTBbk3eTyW6BB9Ca1kuTkhR-hWMqXTylj1Xnha1Q371W5SvpzwmgerBS-hGEQhHW9uVmcMSCg-biLe7qZ6WPW1lvNEilISrCUd2E5wAl8ecnI_pBmSKYAt3E5e28Q9esfWZTdydtVEqQoKQvST3psWlndUsQGFxX835ewARa4xe24dxmXR-rneVxzcR-JQgQYtDZCkTBBvLQ9aPQMY296rj=w386-h278-no)  

![](https://lh3.googleusercontent.com/qF21hCDKz1_g6xnCOBpfVzMP_KVA6V0-qfMse7Tk9YDqbrXgykMXJ_zBuemdbXa9AGI2UiASofogTiJdA1oWqXedf0SpGGTNGrUVs1H-1W_Sf7WdJ3V5iwfepSHE7C6pKD4r63I-2Bx1tUws5OuX-NZu85QUd8SoJAtGwrs3WzOyz1LDq9nG_SypguORqRHRNvhPbmwWi3Y9foAgcIDNstGsKarfZpWsbc7SSEJvxaMhCLaPfPdsm-4oEmQS3WeJpRJ_nO4alTV1Nc70eeQAOH1eN-PCWBjSxt5Oc07sNWSGBwtvTk9w0W5yDSpCIQd1bTjIUmJWF2pYdg4Rbzyer_P7ZwE1vfTsEVKJOIzsz1tuJcw9CxCCxUQH6fKghnAXHMopeQDRevZGxPVPyjv8HKudbLcL5LZTMXIvW-OZJHpkMaTR4qS8XJL_juNYQQRyoM7lerCW_tMNZs_khkrW1YPQGQBk6c2silUN9uE98rZkqOMogNTDAyTgXq4TqcGislMvJeV15fKlMwZ4sfygGrHEBwkQ2ZvyJ1yDAdUdaYDplGs-Uep5bzNN2OvZfOKLxSYnEgKPwjoK1Yp0IEiy5IpsF020YMadJYlnqvdyqAlhnwBU3UNCAca5WiDue8Y0aLlCcpuxBMLIGu_iH0Q_ocgnU7OdV0hyOAGLTYbtfjZ2-a71EIQUftCbjQnn=w386-h278-no)  

```python
"""
Created on Thu Apr 23 10:58:05 2020

@author: henry
"""

# import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
from numpy import loadtxt
import tensorflow
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD, RMSprop
from sklearn import preprocessing

def cleanData(dataset):
    """
    Function to clean the data from "german.data". The inputted data is a mix 
    of qualitative and numberical

    Returns np.array dependant on the size of the dataset

    """
    # clean the data
    data = pd.DataFrame(dataset)
    
    # Everything was imported as a string, but the following columns should be numberical
    data[1] = data[1].astype(int)
    data[4] = data[4].astype(int)
    data[7] = data[7].astype(int)
    data[10] = data[10].astype(int)
    data[12] = data[12].astype(int)
    data[15] = data[15].astype(int)
    data[17] = data[17].astype(int)
    data_num = data.select_dtypes(include = [int])
    
    data[20] = data[20].astype(int) # final results (ie. Y)
    data_Y = data[20]-1 # either 0 or 1
    
    # Classify the values in the columns
    le = preprocessing.LabelEncoder()
    data_obj = data.select_dtypes(include=[object])
    data_obj_trans = data_obj.apply(le.fit_transform)
    
    # New dataframe with the processed data
    data_out = pd.concat([data_num, data_obj_trans], axis=1)
    return [data_out.to_numpy(), data_Y.to_numpy()]

def createModel():
    """
    Creates a neural network using keras

    """
    # Define the keras model. 2 hidden layers of 15 neurons with activation 
    # functionn of relu. The output layer has one neuron with activation 
    # function of sigmoid
    model = Sequential()
    model.add(Dense(15, kernel_initializer='random_uniform', 
                    input_dim=20, activation = "relu"))
    model.add(Dense(15, kernel_initializer='random_uniform', 
                    activation = "relu"))
    model.add(Dense(1, activation = "sigmoid"))
    
    # compile the keras model. Note that the optimizer = agd is for the
    # stochastic gradient descent
    model.compile(loss='binary_crossentropy', optimizer='RMSProp',
                  metrics=['accuracy'])
    # Note the optimizer is RMSprop, which is similar to gradient descent. 
    # This optimizer was suggested in keras documentation for binary 
    # classification problems. 
    return model

def outputPlots(history):
    # list all data in history
    print(history.history.keys())
    
    # summarize history for accuracy
    print(history.history.keys())
    
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Model Accuracy')
    plt.ylabel('Accuracy')
    plt.ylim(0,1)
    plt.xlabel('Epoch')
    plt.xlim(0, 150)
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    
    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.ylim(0,1)
    plt.xlabel('Epoch')
    plt.xlim(0, 150)
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()

# Extract useable dataset
dataset = loadtxt('german.data', dtype=str)
[X, Y] = cleanData(dataset)

# Setup neural network
model = createModel()
print(X.shape)
history = model.fit(X, Y, epochs=150, batch_size = 1, validation_split = 0.2, 
                    verbose=1)

# Output plots of accuracy and loss
outputPlots(history)
```

The numerical dataset was evaluated as well. No convergence issues were encountered using SGD with this dataset. The accuracy is fairly similar and the loss is slightly lower at 0.7 and 0.5, respectively.  

![](https://lh3.googleusercontent.com/O-RK8GhtkdKp8JjOzuy-rQNWuK4z9zVZ11_hrY_yd5bB7rPphvou3eVHgNzmAIZl8raNsbT8IRaIAl44fCRfc2VV-Ldo8a3hHgVusF0KnYrfOcIXz1dVdQzVnIb0RoEkQXo89BRlEw7DR2GJaD1V_ulNUh-wRI46v9Tquc_TtYNGGyYvqsdGooiwESQmIvl0mRJWLW-BW6K2UJ_YpEWaMsu8tEkb-3MOQBdQKSZF2jk-2U03yHHRuM7Zj2bDS0fp21ZeBFc5MqWeOAdt40cUAx8f7k-A0PS33Jys9kvaZAnN7MLnPYkFFRYeIwPZ7gjCbNBXGX5QAfUCsGZaBslFVnVJy3fikZ1pHpU0LmaAnzkadgl_Gq18QbbLeRjzs3y_MdhxBoHmXAVFn09qGHNoma81SUTWptZaounSWQci54WQ0jLHcv2XO0yL62tIiGVjnoRZi4zqcWaj1HqEWAQyv-XNEaJ5324r9x9PqmNjx4z-ZldjVqos0K_fdnDkqm_WyXgpMBPXgdZcqacWiuRCl0By-8oSCMM_5r0Effe0ohDPWXqQUxwkliMXn4e-u6S_5gcChzNVH4--TZf_yWApN4VIjNtIPVxFJl4hqiya4rhbmM1KOu8rtZxiXpvsiV4prR5FC9Wcd4c0Z_4_yWY86EfJJPMsKGX--NLwSik9YefWcqZRovbKcqP3bpxy=w386-h278-no)  

![](https://lh3.googleusercontent.com/Y6P5FdPMw9tieB9QEbuq3UVXpGiQchwZCWnXoPMRYa7xiWYbmmWzTQgkPbOzWfokO9lLuATyKa26zsnh_Z2CIpTT3uBy4w7tXSGHeHpGLiDhijmhou0KzKScT7JdCocW3YWsUabStqs_V7Fodw5UScjMwYQ5CWb_LUoYHx40AMwXY-pU6EDrlP7e8_iqK6Cfg4RIkDh4aU8y_jBU-QLbbW6EIfZ030COVPkIfzEWcAob6-aqARCq66mgP9GVitmd-z45sjJqnBKP6DIDohcElxt2i_OmmdcuM7pVDhC6s6wQyWP-Sk9FB4gB3muenKn5vSkiJ_X_MS5W0MK3zkMEQgZ0S8BWLgT6zgUIxYymekfiXO-rnJdPtvIM2gMAutdtQYsCUFztgZKwN4dcZGJO2kycILvjGBOSlzcR1cA4WzZxITwZUFQRI6h6DpBRKSKhzEz1wi5471oVMooPIv6EiklBPaLFU7mfV-RrwJ4R0yZkAdysGsOwEVGjfII_cABEhxWA--OliPxW6c-jRg9f1KVTPWHWKJKMPjIfIexIZxHMUgsg5VOZxz6y0NCmXYgpuke1oXT3FJYVDDHjGn9VzZd9VeUJff0DbuddYdZuMwnBGg4S3LFnusaYlGQiIy-TAMF8Q9p29_ge5OxWu-G0jYSIyuTU5ftwJInGnJasJWz2XDh6w40E7602-ahM=w386-h278-no)  

```python 
"""
Created on Fri Apr 24 10:58:02 2020

@author: henry
"""

# import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
from numpy import loadtxt
import tensorflow
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD, RMSprop
from sklearn import preprocessing

def cleanData(dataset):
    """
    Function to return the X and Y parts of the dataset

    Parameters
    ----------
    dataset : np.array
        Extracted datafile

    Returns X and Y components to be used in the NN
    -------
    None.

    """
    X = dataset[:,0:-1]
    Y = dataset[:,-1]-1
    
    return [X, Y]

def createModel():
    """
    Creates a neural network using keras

    """
    # Define the keras model. 2 hidden layers of 15 neurons with activation 
    # functionn of relu. The output layer has one neuron with activation 
    # function of sigmoid
    model = Sequential()
    model.add(Dense(15, kernel_initializer='random_uniform', 
                    input_dim=24, activation = "relu"))
    model.add(Dense(15, kernel_initializer='random_uniform', 
                    activation = "relu"))
    model.add(Dense(1, activation = "sigmoid"))
    
    # compile the keras model. Note that the optimizer = agd is for the
    # stochastic gradient descent
    sgd = SGD(lr = 0.1, momentum = 0.1, nesterov=True)
    rms = RMSprop(lr = 0.1)
    model.compile(loss='binary_crossentropy', optimizer='sgd',
                  metrics=['accuracy'])
    # Note the optimizer is RMSprop, which is similar to gradient descent. 
    # This optimizer was suggested in keras documentation for binary 
    # classification problems. 
    return model

def outputPlots(history):
    # list all data in history
    print(history.history.keys())
    
    # summarize history for accuracy
    print(history.history.keys())
    
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Model Accuracy')
    plt.ylabel('Accuracy')
    plt.ylim(0,1)
    plt.xlabel('Epoch')
    plt.xlim(0, 150)
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    
    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.ylim(0,1)
    plt.xlabel('Epoch')
    plt.xlim(0, 150)
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()


dataset = loadtxt('german.data-numeric')
[X, Y] = cleanData(dataset)

# Setup neural network
model = createModel()
history = model.fit(X, Y, epochs=150, batch_size = 1, validation_split = 0.2, 
                    verbose=1)

# Output plots of accuracy and loss
outputPlots(history)
```
