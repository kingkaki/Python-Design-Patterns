# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-20 16:11:57
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-20 16:59:45
"""
懒汉式实例化确保在需要调用时创建对象
__init__方法并不创建对象
创建单例实例的任务交了了getInstance类方法
"""
class Singleton:
	__instance = None
	def __init__(self):
		if not Singleton.__instance:
			print("__init__ method called..")
		else:
			print("Instance already created :", self.getInstance())

	@classmethod
	def getInstance(cls):
		if not cls.__instance:
			cls.__instance = Singleton()
		return cls.__instance

print('1:')
s = Singleton()
print('2:')
print(Singleton.getInstance())
print('3:')
s1 = Singleton()
