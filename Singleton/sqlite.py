# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-20 17:23:04
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-20 17:32:51
'''
单例数据库连接
'''
import sqlite3

class MetaSingleton(type):
	_instance = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instance:
			cls._instance[cls] = super().__call__(*args, **kwargs)
		return cls._instance[cls]

class Database(metaclass=MetaSingleton):
	connection = None
	def connect(self):
		if self.connection is None:
			self.connection = sqlite3.connect('db.sqlite3')
			self.cursorobj = self.connection.cursor()
		return self.cursorobj

db1 = Database().connect()
db2 = Database().connect()

print(db1)
print(db2)
