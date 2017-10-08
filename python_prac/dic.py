#coding: utf-8
#キーの指定と取得
dic = {"JP":"nihon","UK":"igirisu"}
print dic

value = dic["JP"]
print value

list01 = dic.values()
print list01

list01 = dic.items()
print list01

#for
for v in dic.values():
	print "value" , v

