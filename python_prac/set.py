#coding: utf-8

#セットを生成する
set01 = set([1,2,2,2,3])
print set01
set02 = set({"dog":"inu","cat":"neko","bird":"tori"})
print set02

#要素数を取得
print len(set01)

#要素の追加、削除
set01.add(6)
print set01
set01.remove(2)
print set01
set01.clear()
print set01

#論理演算を使う
s1 = set([1,2,3,4,6])
s2 = set([1,2,3,4,6,8,10])

print s1 | s2
print s1 & s2
print s1 - s2

#部分集合か判定
print s1.issubset(s2)
print s2.issubset(s1)


