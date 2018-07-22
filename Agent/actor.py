# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-22 15:04:08
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-22 15:09:36
class Actor():
	def __init__(self):
		self.isBusy = False
	def getStatus(self):
		return self.isBusy
	def occupied(self):
		self.isBusy = False
		print('{} is occupied with current movie'.format(type(self).__name__))
	def available(self):
		self.isBusy = True
		print('{} is free for the movie'.format(type(self).__name__))


class Agent():
	def __init__(self):
		self.actor = Actor()

	def work(self):
		if self.actor.getStatus():
			self.actor.occupied()
		else:
			self.actor.available()

if __name__ == '__main__':
	a = Agent()
	a.work()