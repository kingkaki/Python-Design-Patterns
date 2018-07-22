# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-22 16:47:28
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-22 16:53:10

class Subject:
	def __init__(self):
		self.__observers = []

	def register(self, observer):
		self.__observers.append(observer)

	def notifyAll(self, *args, **kwargs):
		for observer in self.__observers:
			observer.notify(self, *args, **kwargs)

class Observer1:
	def __init__(self, subject):
		subject.register(self)

	def notify(self, subject, *args):
		print("{}:: Got {} From {}".format(type(self).__name__, args, type(subject).__name__))

class Observer2:
	def __init__(self, subject):
		subject.register(self)

	def notify(self, subject, *args):
		print("{}:: Got {} From {}".format(type(self).__name__, args, type(subject).__name__))

if __name__ == '__main__':
	sub = Subject()
	ob1 = Observer1(sub)
	ob2 = Observer2(sub)
	sub.notifyAll('notification')


