#encoding=utf8

from abc import ABCMeta, abstractclassmethod

class Animal(metaclass=ABCMeta):
	@abstractclassmethod
	def do_say():
		pass

class Dog(Animal):
	def do_say(self):
		print('wang wang')
class Cat(Animal):
	def do_say(self):
		print("miao miao")

class ForestFactory():
	def make_sound(self, object_type):
		return eval(object_type)().do_say()

if __name__ == '__main__':
	f = ForestFactory()
	animal = 'Cat'
	f.make_sound(animal)