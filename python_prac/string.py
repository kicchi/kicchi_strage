#coding: utf-8

#文字列の連結
a = 'python'
b = '2.7'
c = a + b
print c

#文字列配列の結合
strings = ['dog','cat','penguin']
print ','.join(strings)

#文字列の繰り返し
s = 'dog?'
print s * 3

#値の埋め込み
#sprintf
a = "python"
b = "a programming language"
print "%s is %s" % (a,b)
#拡張sprintf
v = dict(first = "Michael", family = "Jackson")
print "He is %(first)s, %(first)s %(family)s." % v
#formatメソッド
print"{0},{1}".format("Hello", "World")


#置換
s = "Today is Monday"
print s
print s.replace("Monday","Sunday")
s2 = "Hello Hello"
print s2.replace("Hello", "Bye")
s3 = "World World"
print s3.replace("World", "Hello", 1)
print s3.replace("World", "Hello", 2)
s4 = "World World World"
print s4.replace("World", "Hello", 1)

import re
s = "Hello World"
print re.sub(r"[a-z]","A",s)

#N文字目の文字の取得
s = "abc"
n = 1
print s[n-1]
s2 = "xyz"
print s2[-1]

#部分文字列の取得(N文字目から、M文字取り出す)
s = "This is a pen."
n = 1
m = 4
print s[n-1:n-1+m]
print s[0:4]
print s[-4:-1] #-4 <= s < -1

#検索
s = "abcabcabc"
index = s.find('b')
print index
index = s.find("b",2)
print index

target = "b"
index = -1
while True:
	index = s.find(target,index + 1)
	if index == -1: #見つからなかったら-1を返す
		break
	print "start = %d" % index

#1文字ずつ処理
for c in "aiueo":
	print c

print list("hoge")

s = "aiueo"
for i in range(len(s)):
	c = s[i]
	print c

#strip
s = " x "
print "A" + s.strip() + "B"
print "A" + s.lstrip() + "B"
print "A" + s.rstrip() + "B"

#改行削除
line = "hoge\n"
msg = line.rstrip() + "moge"
print msg
'''
with open("./test.txt") as fh:
	for line in fh:
		no_line_break_line = line.rstrip()
'''

#全部大文字にする
print "hello".upper()
#全部小文字にする
print "BIG".lower()

#ある文字列が部分文字列として含まれるかどうか調べる
s = "abc"
print "b" in s
print "x" in s

#ある文字列が部分文字列として登場する回数を数える
s = "aaabbc"
print s.count("b")

#intを文字列に変換する
v = 1
print str(v)
print "%d" % v

#floatを文字列に変換する
f = 1.234
print str(f)
print "%f" %f

#listを文字列に変換する、tupleを文字列に変換する
v = [1,2,3]
print str(v)
print "%s" % v

v = (1,2,3)
print str(v)
#print "%s" % v
print "%s" % (v,)

print "<" + ("/".join([str(item) for item in v])) + ">"



