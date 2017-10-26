#coding: utf-8

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from sklearn import datasets
from sklearn.model_selection import train_test_split


X, y = datasets.make_moons(N, noise = 0.3)

data01 = X
data02 = X
for i in reversed(xrange(300)):
	if y[i] == 0:
		np.delete(data01,i)
	elif y[i] == 1:
		np.delete(data02,i)


print (data01)
