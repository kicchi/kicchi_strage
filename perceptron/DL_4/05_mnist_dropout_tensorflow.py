#coding: utf-8

import tensorflow as tf
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

np.random.seed(0)
tf.set_random_seed(1234)

#データの生成
mnist = datasets.fetch_mldata('MNIST original', data_home = 'MNIST')

#データをランダムに選ぶ
n = len(mnist.data)
N = 10000
train_size = 0.8
indices = np.random.permutation(range(n))[:N]

X = mnist.data[indices]
y = mnist.target[indices]
Y = np.eye(10)[y.astype(int)] #1-of-K表現に変換
print (X.shape)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size = train_size)

#モデル設定
n_in = len(X[0]) #784
n_hidden = 200
n_out = len(Y[0]) #10

x = tf.placeholder(tf.float32, shape=[None, n_in])
t = tf.placeholder(tf.float32, shape=[None, n_out])
keep_drop = tf.placeholder(tf.float32) #ドロップアウトしない確率

#入力層 - 隠れ層
W0 = tf.Variable(tf.truncated_normal([n_in, n_hidden], stddev=0.01))
b0 = tf.Variable(tf.zeros([n_hidden]))
h0 = tf.nn.relu(tf.matmul(x,W0) + b0)
h0_drop = tf.nn.dropout(h0, keep_drop)

#隠れ層 - 隠れ層
W1 = tf.Variable(tf.truncated_normal([n_hidden, n_hidden], stddev=0.01))
b1 = tf.Variable(tf.zeros([n_hidden]))
h1 = tf.nn.relu(tf.matmul(h0,W1) + b1)
h1_drop = tf.nn.dropout(h1, keep_drop)

W2 = tf.Variable(tf.truncated_normal([n_hidden, n_hidden], stddev=0.01))
b2 = tf.Variable(tf.zeros([n_hidden]))
h2 = tf.nn.relu(tf.matmul(h1,W2) + b2)
h2_drop = tf.nn.dropout(h2, keep_drop)

#隠れ層 - 出力層
W4 = tf.Variable(tf.truncated_normal([n_hidden, n_out], stddev=0.01))
b4 = tf.Variable(tf.zeros([n_out]))
y = tf.nn.softmax(tf.matmul(h2,W4) + b4)

cross_entropy = tf.reduce_mean(-tf.reduce_sum(t * tf.log(y),reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(t, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

#モデル学習
epochs = 50
batch_size = 200

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

n_batches = (int)(N * train_size) // batch_size

for epoch in range(epochs):
	X_, Y_ = shuffle(X_train, Y_train)

	for i in range(n_batches):
		start = i * batch_size
		end = start + batch_size

		sess.run(train_step,feed_dict={
			x: X_[start:end],
			t: Y_[start:end]
		})
	
	# 訓練データに対する学習の進み具合を出力
	loss = cross_entropy.eval(session=sess, feed_dict={
		x: X_,
		t: Y_
	})

	acc = accuracy.eval(session=sess, feed_dict={
		x: X_,
		t: Y_
	})
	print ('epoch: ', epoch, ' loss:', loss, 'accuracy:', acc)

#予測精度の評価
accuracy_rate = accuracy.eval(session=sess, feed_dict={
	x: X_test,
	t: Y_test
})
print ('accuracy: ', accuracy_rate)