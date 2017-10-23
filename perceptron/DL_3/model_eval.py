#coding: utf-8

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from sklearn import datasets
from sklearn.model_selection import train_test_split


N = 300
X, y = datasets.make_moons(N, noise = 0.3)

'''
print (X[1].shape)
data01 = np.empty((150,2))
data02 = np.empty((150,2))
for i in range(300):
	if y[i] == 0:
		data01 = np.concatenate((data01,X[i]), axis = 0)
	elif y[i] == 1:
		data02 = np.concatenate((data02,X[i]), axis = 0)
'''


Y = y.reshape(N, 1)
X_train, X_test, Y_train, Y_test =\
	train_test_split(X, Y, train_size=0.8)

num_hidden = 3

x = tf.placeholder(tf.float32, shape = [None, 2])
t = tf.placeholder(tf.float32, shape = [None, 1])

#入力層 - 隠れ層
W = tf.Variable(tf.truncated_normal([2, num_hidden]))
b = tf.Variable(tf.zeros([num_hidden]))
h = tf.nn.sigmoid(tf.matmul(x, W) + b)

#隠れ層 - 出力層
V = tf.Variable(tf.truncated_normal([num_hidden, 1]))
c = tf.Variable(tf.zeros([1]))
y = tf.nn.sigmoid(tf.matmul(h, V) + c)

cross_entropy =  - tf.reduce_sum(t * tf.log(y) + (1 - t) * tf.log(1 - y))
train_step = tf.train.GradientDescentOptimizer(0.05).minimize(cross_entropy)
correct_prediction = tf.equal(tf.to_float(tf.greater(y, 0.5)),t)

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

batch_size = 20
n_batches = N // batch_size

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for epoch in range(500): 
	X_, Y_ = shuffle(X_train, Y_train)

	for i in range (n_batches):
		start = i * batch_size
		end = start + batch_size

		sess.run(train_step, feed_dict={
			x: X_[start:end],
			t: Y_[start:end]
		})

accuracy_rate = accuracy.eval(session = sess, feed_dict = {
	x: X_test,
	t: Y_test
})

print ('accuracy: ', float(accuracy_rate))

print ("------data01-------")
print (data01)

X_1 = data01[:,0]
X_2 = data01[:,1]
plt.plot(X_1,X_2,'o')
X_1 = data02[:,0]
X_2 = data02[:,1]
plt.plot(X_1,X_2,'x')
plt.savefig("toy_problem.png")