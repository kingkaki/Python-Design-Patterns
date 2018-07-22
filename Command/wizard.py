# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-22 22:59:17
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-22 23:04:14
class Wizard():
	def __init__(self, src, rootdir):
		self.choices = []
		self.rootdir = rootdir
		self.src = src

	def preferences(self, command):
		self.choices.append(command)

	def execute(self):
		for choice in self.choices:
			if list(choice.values())[0]:
				print('Copying binaries -- {} to {}……'.format(self.src, self.rootdir))
			else:
				print('No Operation')

if __name__ == '__main__':
	wizard = Wizard('Python3.7.zip', '/usr/home/')
	wizard.preferences({'Python': True})
	wizard.preferences({'Java': False})
	wizard.execute()
