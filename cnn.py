# -*- coding: utf-8 -*-
"""CNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_-QzYxq2ljc-8APzOwExrCnAXM-PHPwq
"""

import pandas
import numpy
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers import Flatten

from keras.datasets import mnist

(x_train,y_train),(x_test,y_test) = mnist.load_data()

x_train.shape

import matplotlib.pyplot as plt

plt.imshow(x_train[0]);

x_train = x_train.reshape(x_train.shape[0],28,28,1).astype('float32')
x_test = x_test.reshape(x_test.shape[0],28,28,1).astype('float32')

x_train /= 255
x_test /= 255

from keras.utils.np_utils import to_categorical

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

y_train.shape

classes = y_train.shape[1]

model = Sequential()
model.add(Conv2D(16,(5,5),strides=(1,1),activation="relu",input_shape=(28,28,1)))
model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
model.add(Flatten())
model.add(Dense(100,activation="relu"))
model.add(Dense(classes,activation="softmax"))

model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=['accuracy'])

model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10, batch_size=200, verbose=2)

score = model.evaluate(x_test,y_test,verbose=0)
print("Accurac : {}\n Error : {}".format(score[1],100-score[1]*100))

model = Sequential()
model.add(Conv2D(16,(5,5),strides=(1,1),activation="relu",input_shape=(28,28,1)))
model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))

model.add(Conv2D(8,(2,2),strides=(1,1),activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))

model.add(Flatten())
model.add(Dense(100,activation="relu"))
model.add(Dense(classes,activation="softmax"))

model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=['accuracy'])

model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10, batch_size=200, verbose=2)

score = model.evaluate(x_test,y_test,verbose=0)
print("Accurac : {}\n Error : {}".format(score[1],100-score[1]*100))

