# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-22 13:09:34
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-22 13:36:19
from abc import ABCMeta, abstractclassmethod

class PizzaFactory(metaclass=ABCMeta):
	@abstractclassmethod
	def createVegPizza(self):
		pass
	@abstractclassmethod
	def createNonVegPizza(self):
		pass

class IndianPizzaFactory(PizzaFactory):
	def createVegPizza(self):
		return DeluxVeggiePizza()
	def createNonVegPizza(self):
		return ChickenPizza()

class USPizzaFactory(PizzaFactory):
	def createVegPizza(self):
		return MexicanVegPizza()
	def createNonVegPizza(self):
		return HamPizza()


class VegPizza(metaclass=ABCMeta):
	@abstractclassmethod
	def prepare(self, VegPizza):
		pass

class NonVegPizza(metaclass=ABCMeta):
	@abstractclassmethod
	def server(self, VegPizza):
		pass

class DeluxVeggiePizza(VegPizza):
	def prepare(self):
		print('preparing ', type(self).__name__)

class ChickenPizza(NonVegPizza):
	def server(self, VegPizza):
		print('{} is served with chicken on {}'.format(type(self).__name__, type(VegPizza).__name__ ))

class MexicanVegPizza(VegPizza):
	def prepare(self):
		print('preparing ', type(self).__name__)

class HamPizza(NonVegPizza):
	def server(self, VegPizza):
		print('{} is served with ham on {}'.format(type(self).__name__, type(VegPizza).__name__))


class PizzaStore:
	def __init__(self):
		pass
	def makePizzas(self):
		for factory in [IndianPizzaFactory(), USPizzaFactory()]:
			self.factory = factory
			self.NonVegPizza = self.factory.createNonVegPizza()
			self.VegPizza = self.factory.createVegPizza()
			self.VegPizza.prepare()
			self.NonVegPizza.server(self.VegPizza)

pizza = PizzaStore()
pizza.makePizzas()