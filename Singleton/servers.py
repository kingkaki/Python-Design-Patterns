# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-20 17:35:11
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-20 17:46:56
'''
两个实例Server.display()
对同一类进行的增删操作

server1
server2
server3

server1
server2
server3
server4

server1
server2
'''

class Server:
	_instance = None
	servers = ['server1','server2','server3']	

	def __new__(cls, *args, **kwargs):
		if cls._instance is None:
			cls._instance = super().__new__(cls, *args, **kwargs)
		return cls._instance

	def add(self):
		self.servers.append('server{}'.format(len(self.servers)+1))

	def pop(self):
		self.servers.pop()

	@classmethod
	def display(self):
		for server in self.servers:
			print(server)
		print()

s1 = Server()
s2 = Server()
Server.display()

s1.add()
Server.display()

s2.pop()
s2.pop()
Server.display()
