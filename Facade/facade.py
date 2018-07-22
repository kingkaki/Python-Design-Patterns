# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-22 14:22:22
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-22 14:38:51


class EventManager:
	'''
	总事务负责人
	'''
	def __init__(self):
		print('EventManager: let me talk to the folks\n')

	def arrange(self):
		self.hotelier = Hotelier()
		self.hotelier.bookHotel()

		self.florist = Florist()
		self.florist.setFlowerRequirements()

		self.caterer = Caterer()
		self.caterer.setCuisine()

		self.musician = Musician()
		self.musician.setMusicType()

'''
各类负责人
'''
class Hotelier():
	def __init__(self):
		print('Arranging the Hotel for Marriage?')

	def _isAvailable(self):
		print('Is the hotel free for the event on given day?')
		return True

	def bookHotel(self):
		if self._isAvailable():
			print('Registered the Boking\n')

class Florist():
	def __init__(self):
		print('Flower for the Event?')

	def setFlowerRequirements(self):
		print('carnations & roses\n')

class Caterer():
	def __init__(self):
		print('Food arrangements for the event?')

	def setCuisine(self):
		print('Chinese & Continental Cuisine to be served\n')

class Musician():
	def __init__(self):
		print('Music arrangements for the marriage?')
	def setMusicType(self):
		print('Jazz and classical\n')

'''
你只需要询问总负责人即可
'''
class You():
	def __init__(self):
		print('You:: Marriage Arrangements?')
	def askEventManager(self):
		print("You:: let's contact the Manager")
		m = EventManager()
		m.arrange()
	def __del__(self):
		print('Wonderful!')

y = You()
y.askEventManager()





