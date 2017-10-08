#coding: utf-8

#タプルの表現の仕方
tuple = (1,2,3,4)
print tuple

tuple = (1,)
print tuple

#要素の取得
tuple = (1,2,3,4)
print tuple[1]

#スライス : 使うやつ
print tuple[1:3]

#サイズ取得
print len(tuple)

#連結と繰り返し
tuple01 = tuple + (5,6)
print tuple01

tuple01 = tuple * 4
print tuple01


