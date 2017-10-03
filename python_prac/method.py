#coding: utf-8

class MyClass(object):
	pass

me = MyClass()
print(me)

class EmptyClass(object):
	pass

holder = EmptyClass()
holder.name = "Sato"
holder.age = 20
print holder.name, holder.age

class MyClass(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age
	
	def introduce(self):
		print "My name is " + self.name + ", " + str(self.age) + " years old"

me = MyClass("Suzuki",30)
me.introduce()

me.name = "Taro"
me.age = 25
me.introduce()

class MyClass(object):
	primary_key = "id"

	@classmethod
	def show_primary_key(cls):
		print "Primary is  %s" % cls.primary_key

print MyClass.primary_key
MyClass.show_primary_key()

class MyClass(object):
	primary_key = "id"

	@classmethod
	def show1(cls):
		print(cls.primary_key)
	
	@staticmethod
	def show2():
		print(MyClass.primary_key)
	
MyClass.show1()
MyClass.show2()
