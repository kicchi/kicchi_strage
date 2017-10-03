#coding: utf-8
#関数

def add(x,y):
	print x + y

add (3,5)

def add(x,y):
	ans = x + y
	return ans

n = add(9,5)
print n

def repeat_msg(msg,repeat = 3):
	for i in range(repeat):
		print msg

repeat_msg("Hello")
repeat_msg("Yahoo",repeat = 5)

def func(a1,a2,*args,**params):
	print a1
	print a2
	print args
	print params

func("A","B","C","D",k1 = "K2",k2 = "K2")

def func():
	return 3,"ABC"

n,s = func()
print n,s

count = 0

def func():
	print count
	global count
	count += 1

func()
print count

'''
def func():
	for k in globals().key():
		print "GLOBAL:%s = %s" % (k,globals()[k])
	for k in locals().key():
		print "LOCAL: %s = %s" % (k,locals()[k])

func()
'''

myfunc = lambda x,y:x+y
print myfunc(3,5)

a = [1,2,3]
print map(lambda x:x ** 2, a)

'''
class MyClass:
	def __init__(self):
		self.data = (1,2,3,4,5)
		self.index = 0
	def __iter__(self):
		return self
	def next(self):
		if self.index < len(self.data):
			self.index += 1
			return self.data[self.index - 1]
		else:
			raise StopIteration

for n in MyClass():
	print n

it = MyClass().__iter__()
while 1:
	n = it.next()
	try:
		print n
	except StopIteration:
		break
'''

def mydecolater(func):
	def rapper():
		print "start"
		func()
		print "end"
	return rapper

@mydecolater
def hello():
	print "hello"

hello()

