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

image  

### Circle Demo
For this example, there is a dataset of points clustered together forming a distinguishable circle. There is also an outer ring of points scattered. The purpose of this neural network is to identify the boundary which forms the inner circle. This is a multi-classification task.   

The selected testing parameters was adjusted from the defaulted values. The parameters was selected to be 10 epochs with a constant learning rate of 0.1. There are two input nodes and two output nodes (for the x and y values). A single hidden layer consisting of 15 nodes was specified. Activation function on the hidden layer is "sigmoid" and for the output node, "softmax" is used. The loss function is "cross-entropy". The final plot is shown below. Convergence happens relatively quickly; judging by the accuracy graph, 10 epochs may not be required. 

image  

### Poly Demo
For this example, the neural network had to fit a line to a polynomial scatter. The scatter is based from a fourth degree polynomial. This is an regression task.  

The selected testing parameters was 50 epochs with a learning rate of 0.007. A learning rate scheduling of 0.75 was specified as well. There is one input node with one output node (given the x-value, the NN will predict the y value). A single hidden layer consisting of 20 nodes was specified. Activation function on the hidden layer is "sigmoid" and for the output node, "linear" is used. The loss function is "l2-loss". The final plot is shown below.  

image  

### XOR Demo
In this example, the neural network had to perform a two-class classification.  

The selected parameters were unchanged from the default parameters as they appeared to work efficiently. 50 epochs was specified with a learning rate of 0.1. There are two input nodes with two outputs nodes (the x and y values). A single hidden layer consisting of 15 nodes was specified. Activation function on the hidden layer is "sigmoid" and for the output node, "softmax" is used. The loss function is cross-entropy.  The final plot is shown below. As noted, convergence happens relatively quickly and it may not be necessary to use 50 epochs.  

image  

### Wine Class Demo
In this example, the neural network had to classify the different wine classes given the various inputs. This is a multi-classification task.  

The neural network parameters were unchanged from the defaults. 60 epochs was specified with a constant learning rate of 0.01. There are 13 input nodes and 3 output nodes (to input the various characteristices of the wine and output the wine type). A single hidden layer consisting of 15 nodes was specified. Activation function on the hidden layer is "sigmoid" and for the output node, "softmax" is used. The loss function is "cross-entropy". The final plot is shown below.  

image  

### Red Wine Rating Demo
In this example, the neural network was designed to guess the rating of the red wine given the various inputs. This is a multi-classification task. The rating system ranges from 0-10, so at first glance it may seem like a cross-classification problem. However, the rating is done in intervals (ie. 5.5, 7.5, but not 5.4 or 7.7). The example code models this as a regression problem, but I attempted to redo it as a cross-classification problem with 20 output nodes (for intervals of 0.5).  

explaination

image original  

image new  

### Car Demo
In this example, the neural network had to predict the type of the car given the data. Unlike previous examples, the discriptors of the inputs were strings, so they had to be transformed into numberical values. The output, similiarily had to be converted to numberical values. Ultimantely, this is a multi-classification problem.  

The neural network parameters were unchanged from the defaults. 60 epochs was specified with a learning rate of 0.01 and a scheduling rate of 0.9. There are 6 input nodes and 4 output nodes (to input the various characteristices of the car and output the wine type). A single hidden layer consisting of 12 nodes was specified. Activation function on the hidden layer is "sigmoid" and for the output node, "softmax" is used. The loss function is "cross-entropy". The final plot is shown below.  

image
