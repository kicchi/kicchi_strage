#coding: utf-8
##########リストを生成する##########
#空のリストを作る
list01 = list()
list01 = []
print list01

#初期値を指定する
list01 = ["a","b","c"]
print list01

#タプルからリストを作る
aTapple = (1,2)
list01 = list(aTapple)
print list01

#セットからリストを作る
aSet = set([1,2,3,3,4,5])
list01 = list(aSet)
print list01

#文字列から作る
list01 = list("abcd")
print list01

#文字列から作る
list01 = "1,2,3,4,5".split(",")
print list01

#レンジから作る
list01 = range(0,10)
print list01

#レンジで数値小さくなるように作る
list01 = range(10,0,-1)
print list01
##########値を追加する##########
#後ろに追加
list01.append("a")
print list01
#前に追加
list01.insert(0,"b")
print list01
#任意の場所に追加
list01.insert(3,"c")
print list01
#配列に配列を追加
list02 = [10,20,30,40]
list01 += list02
print list01
##########値を削除する##########
#要素の削除
list01.remove("c")
print list01
#h複数存在するものを全て削除する
list01 = [item for item in list01 if item is not 10]
print list01
list01 = filter(lambda a: a != "a",list01)
print list01
#位置を指定して削除
del list01[2]
print list01
#位置を指定して削除（複数）
del list01[0:2]
print list01
#位置を指定して削除（全部）
del list01[:]
print list01
##########値の取得、出現回数、サイズ##########
list01 = range(5,20)
#範囲指定で取り出す
#要素0~1
print list01[0:2]
#要素1から後ろから二つまで
print list01[0:-1]
#要素0~3まで
print list01[:3]
#要素3〜最後まで
print list01[3:]
#要素を二つおきに取得
print list01[::3]
#逆順に取得
print list01[::-1]
#逆順に２つ取得
print list01[::-2]
#指定した要素の位置を取得する
index = list01.index(19)
print index
#最後の要素を取得して同時に削除する
item = list01.pop()
print item
item = list01.pop(2)
print item
print list01
#指定した要素の出現回数を取得する
count = list01.count(10)
print count
#サイズを確認する
print len(list01)
#要素の存在確認
print 12 in list01
print 22 in list01

##########値を変更する##########
list01[3] = 100
print list01
list01[0:5] = ["A","B","C","D","E","F"]
print list01
list01[-1:] = ["X","Y"]
print list01

#########ソートする#########
#ソートする（元のリストはソートしない）
list02 = sorted(list01)
print list02
#ソートする（元のリスト自体をソートする）
list01.sort()
print list01
#逆順ソート
list01.sort(reverse=True)
print list01

##########リストをスタックとして使う#############
stuck = [3,4,5]
stuck.append(6)
print stuck
print stuck.pop()
print stuck

##########リストをキューとして使う#############
from collections import deque
queue = deque([3,4,5])
queue.append(6)
print queue
print queue.popleft()
print queue.pop()

########関数プログラミング########
list01 = range(0,10)
#filter(条件に一致する要素に絞り込む)
list02 = filter(lambda x: x % 2 == 0,list01)
print list02
#関数型の場合
def isEven(x) : return x % 3 is 0
list03 = filter(isEven,list01)
print list03
#map(各要素に処理を行う)
#ラムダ型の場合
list04 = map(lambda x:x*x, list01)
print list04
#関数型の場合
def func(x) : return x*x*x
list05 = map(func,list01)
print list05

#reduce(各要素を組み合わせて１つの結果を作る)
#ラムダ型の場合
list06 = reduce(lambda x,y:x+y,list01)
print list06
#関数型の場合
def summention(x,y) : return x+y
list07 = reduce(summention,list01)
print list07

#########リスト内包表記########3
print [i * 2 for i in list01]
print [i * 2 for i in list01 if i % 2 is 1]
print [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]

#######ループ処理#######
list01 = list("neuralnetwork")
#一件ずつ処理
for item in list01:
	print item
#ループ処理(indexも一緒に取得したい)
for i,v in enumerate(list01):
	print i,v
#ループ処理(２つの配列を同時に処理する)
firstname = ["sato","suzuki","takahshi"]
secondname = ["taro","hanako","satoshi"]
for f,s in zip(firstname,secondname):
	print f,s
for f in firstname:
	for s in secondname:
		print (f,s)
#ループ中に、ループ対象のリストを処理する
list01 = range(0,10)
for i in list01[:]:
	if i  % 3 is 0:	
		list01.append(i)
print list01

