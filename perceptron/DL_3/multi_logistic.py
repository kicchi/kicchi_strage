#coding* utf-8

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle

M = 2 		#入力データの次元
K = 3 		#クラス数
n = 100 	#クラスごとのデータ数
N = n * K	#全データ数

X1 = np.random.randn(n, M) + np.array([0, 10])
X2 = np.random.randn(n, M) + np.array([5, 5])
X3 = np.random.randn(n, M) + np.array([10, 0])
Y1 = np.array([[1, 0, 0] for i in range(n)])
Y2 = np.array([[0, 1, 0] for i in range(n)])
Y3 = np.array([[0, 0, 1] for i in range(n)])

X = np.concatenate((X1, X2, X3), axis = 0)
Y = np.concatenate((Y1, Y2, Y3), axis = 0)

plt.plot(X1[:,0],X1[:,1],'o')
plt.plot(X2[:,0],X2[:,1],'^')
plt.plot(X3[:,0],X3[:,1],'x')
plt.savefig("sample_date.png")


W = tf.Variable(tf.zeros([M, K]))
b = tf.Variable(tf.zeros([K]))

x = tf.placeholder(tf.float32, shape = [None, M])
t = tf.placeholder(tf.float32, shape = [None, K])
y = tf.nn.softmax(tf.matmul(x, W) + b)

cross_entropy = tf.reduce_mean(-tf.reduce_sum(t * tf.log(y), reduction_indices = [1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(t, 1))

batch_size = 50 #ミニバッチサイズ
n_batches = N // batch_size

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for epoch in range(20):
	X_, Y_ = shuffle(X, Y)

	for i in range (n_batches):
		start = i * batch_size
		end = start + batch_size

		sess.run(train_step, feed_dict={
			x: X_[start:end],
			t: Y_[start:end]
		})

X_, Y_ = shuffle(X, Y)

classified = correct_prediction.eval(session = sess, feed_dict = {
	x: X_[0:10],
	t: Y_[0:10]

})

prob = y.eval(session = sess, feed_dict = {
	x: X_[0:10]
})


#print (sess.run(W))
print ('classified:')
print (classified)
print ()
print ('output probability')
print (prob)


plt.plot(X1[:,0],X1[:,1],'o')
plt.plot(X2[:,0],X2[:,1],'^')
plt.plot(X3[:,0],X3[:,1],'x')

w = sess.run(W).T
b = sess.run(b)
print (w)
x_1 = np.arange(-5,15,1)
#class 1 and 2
x_2 = (w[1][0] - w[0][0]) * x_1 + (b[1] - b[0]) / (w[0][1] - w[1][1])
plt.plot(x_1,x_2)
#class 2 and 3
x_2 = (w[2][0] - w[1][0]) * x_1 + (b[2] - b[1]) / (w[1][1] - w[2][1])
plt.plot(x_1,x_2)
#class 3 and 1
x_2 = (w[0][0] - w[2][0]) * x_1 + (b[0] - b[2]) / (w[2][1] - w[0][1])
plt.plot(x_1,x_2)
plt.savefig("split.png")
