# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-22 23:07:40
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-22 23:16:00
from abc import ABCMeta, abstractclassmethod

class Command(metaclass=ABCMeta):
	def __init__(self, recv):
		self.recv = recv
	def execute(self):
		pass

class ConcreteCommand(Command):
	def __init__(self, recv):
		self.recv = recv
	def execute(self):
		self.recv.action()

class Receiver:
	def action(self):
		print('Receiver Action')

class Invoker:
	def command(self, cmd):
		self.cmd = cmd

	def execute(self):
		self.cmd.execute()

if __name__ == '__main__':
	recv = Receiver() # recv 接受传入的参数
	cmd = ConcreteCommand(recv) # cmd声明执行的接口
	invoker = Invoker() # invoker调用cmd执行命令
	invoker.command(cmd)
	invoker.execute()