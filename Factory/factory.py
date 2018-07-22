# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-22 12:36:58
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-22 13:06:00
from abc import ABCMeta, abstractclassmethod

class Section(metaclass=ABCMeta):
	@abstractclassmethod
	def describe(self):
		pass

class PersonalSection(Section):
	def describe(self):
		print('Personal Section')

class AlbumSection(Section):
	def describe(self):
		print('Album Section')

class PatentSection(Section):
	def describe(self):
		print('Patent Section')

class PublicationSection(Section):
	def describe(self):
		print('Publication Section')


class Profile(metaclass=ABCMeta):
	def __init__(self):
		self.sections = []
		self.createProfile()

	@abstractclassmethod
	def createProfile(self):
		pass
	def getSections(self):
		return self.sections
	def addSections(self, section):
		self.sections.append(section)

class linkedin(Profile):
	def createProfile(self):
		self.addSections(PersonalSection())
		self.addSections(PatentSection())
		self.addSections(PublicationSection())

class facebook(Profile):
	def createProfile(self):
		self.addSections(PersonalSection())
		self.addSections(AlbumSection())

if __name__ == '__main__':
	profile_type = 'linkedin'
	profile = eval(profile_type)()
	print(type(profile))
	print(profile.getSections())
