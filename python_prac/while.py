#coding: utf-8

num = 0

print "start"
while num < 5:
	print "num = " + str(num)
	num += 1
else: #else が使える
	print "end"

num = 5
while(num > 0):
	print(num)
	num -= 1
	if (num == 0):
		break
