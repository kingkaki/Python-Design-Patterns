# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-20 17:08:18
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-20 17:12:54
'''
创建元类单例
'''
class MetaSingleton(type):
	_instance = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instance:
			cls._instance[cls] = super().__call__(*args, **kwargs)
		return cls._instance[cls]

class Logger(metaclass=MetaSingleton):
	pass

l1 = Logger()
l2 = Logger()
print(l1)
print(l2)