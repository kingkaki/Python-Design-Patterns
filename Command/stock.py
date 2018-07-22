# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-22 23:19:58
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-22 23:43:43
from abc import ABCMeta, abstractclassmethod

class Order(metaclass=ABCMeta):
	@abstractclassmethod
	def execute(self):
		pass

class BuyStockOrder(Order):
	def __init__(self, stock):
		self.stock = stock
	def execute(self):
		self.stock.buy()

class SellStockOrder(Order):
	def __init__(self, stock):
		self.stock = stock
	def execute(self):
		self.stock.sell()

class StockTrade:
	def buy(self):
		print('Buying stocks……')
	def sell(self):
		print('Selling stocks……')

class Agent:
	def __init__(self):
		self.__orderQueue = []
	def placeOrder(self, order):
		self.__orderQueue.append(order)
		order.execute()

if __name__ == '__main__':
	stock = StockTrade()
	buyStock = BuyStockOrder(stock)
	sellStock = SellStockOrder(stock)

	agent = Agent()
	agent.placeOrder(buyStock)
	agent.placeOrder(sellStock)