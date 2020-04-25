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
In this example, the neural network was designed to guess the rating of the red wine given the various inputs. This is a multi-classification task. The rating system ranges from 0-10, so at first glance it may seem like a cross-classification problem. However, the rating is done in intervals (ie. 5.5, 7.5, but not 5.4 or 7.7). The example code models this as a regression problem.  

Nothing was changed from the demo. An activation function of sigmoid was specified for the hidden layers and an output activation function of linear was specified for the output nodes. The loss function is "l2 loss". There are 11 input nodes. one layer of 20 hidden nodes, and one single output node. 100 epochs was used with a learning rate of 0.005.  

image original  

### Car Demo
In this example, the neural network had to predict the type of the car given the data. Unlike previous examples, the discriptors of the inputs were strings, so they had to be transformed into numberical values. The output, similiarily had to be converted to numberical values. Ultimantely, this is a multi-classification problem.  

The neural network parameters were unchanged from the defaults. 60 epochs was specified with a learning rate of 0.01 and a scheduling rate of 0.9. There are 6 input nodes and 4 output nodes (to input the various characteristices of the car and output the wine type). A single hidden layer consisting of 12 nodes was specified. Activation function on the hidden layer is "sigmoid" and for the output node, "softmax" is used. The loss function is "cross-entropy". The final plot is shown below.  

image  

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

image  

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

image  

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
