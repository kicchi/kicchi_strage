#coding: utf-8
class MyClass:
	"""A sample class"""
	PI = 3.14
	def __init__(self):
		self.name = ""
	
	def getName(self):
		return self.name

	def setName(self,name):
		self.name = name

a = MyClass()
a.setName("Tanaka")
print a.getName()
print MyClass.PI

class MyClass:
	def __init__(self):	
		self.name = ""

a1 = MyClass()
a1.name = "Sato"

a2 = MyClass()
a2.name = "Suzuki"

print a1.name
print a2.name

class MyClass:	
	count = 0
	
	def __init__(self):
		MyClass.count += 1

a1 = MyClass()
a2 = MyClass()
print MyClass.count

class MyClass:
	pass

a1 = MyClass()
a1.name2 = "Takahashi"
MyClass.PI2 = 3.141
print a1.name2
print MyClass.PI2

class MyClass:
	PI = 3.14

a1 = MyClass()
a2 = MyClass()
print a1.PI
a1.PI = 3.141593
print a1.PI
print a2.PI

class MyClass:
	name = "Yamada"
	def setName(self,name):
		self.name = name

a = MyClass()
b = MyClass()
a.setName("Ito")
print a.name
print b.name

class MyClass:
	def __init__(self):
		self.name = "tanaka"
		self._name = "yamada"
		self.__name = "suzuki"
	
	def hello(self):
		print "hello"
	def _hello(self):
		print "hello"
	def __hello(self):
		print "hello"

a = MyClass()

print a.name
print a._name
# print a.__name 参照できない

a.hello()
a._hello()
#a.__hello()

print a._MyClass__name
a._MyClass__hello()

class MyClass:
	def __init__(self):
		print "INIT!"
	def __del__(self):
		print "DEL!"

a = MyClass()
del a

class MyClass:
	def __init__(self,name):
		self.name = name
	
	def __str__(self):	
		return "My name is " + self.name

a = MyClass("Yamada")
print a

class MyClass:
	def hello(self):
		print "Hello"

class MyClass2(MyClass):
	def world(self):
		print "World"

a = MyClass2()
a.hello()
a.world()
class MyClass3(MyClass):
	def hello(self):
		print "HELLO"

a = MyClass3()
a.hello()

class MyClass1(object):
	def __init__(self):
		self.val1 = 123

class MyClass2(MyClass1):
	def __init__(self):
		super(MyClass2,self).__init__()
		self.val2 = 456

a = MyClass2()
print a.val1
print a.val2

class MyClassA:
	def funcA(self):
		print "MyClassA:funcA"

class MyClassB:
	def funcB(self):
		print "MyClassB:funcB"

class MyClassC(MyClassA,MyClassB):
	def funcC(self):
		print "MyClassC:funcC"

a = MyClassC()
a.funcA()
a.funcB()
a.funcC()
