#coding: utf-8
print "for文にrange関数を使用した繰り返し文"
for i in range(5):
	print(i)
for i in range(1,6):
	print(i)

print "for文とif文を使った条件分岐"
for i in range(1,11):
	if i % 3 == 0:
		print(i)

print "break-continue文"
strings = ["ruby","perl","java","c","python"]
for string in strings:
	if string == "python":
		print "OK"
		break
	print string

for string in strings:
	if string != "python":
		print string
		continue
	print "OK"
	break

print "for-else文"
scores = [100, 71, 80 , 99, 74]
for score in scores:
	if score <= 70:
		break
else:
	print "合格"

print "for文のスコープ"

for i in range(5):	
	ans = 1
print ans
