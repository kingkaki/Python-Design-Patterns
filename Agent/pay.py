# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-22 15:24:23
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-22 16:29:48
'''
DebitCard通过代理Bank为用户付钱
'''

class You:
	def __init__(self):
		print('You:: I want to buy it ')
		self.debitCard = DebitCard()
		self.isPurchased = False

	def make_payment(self):
		self.isPurchased = self.debitCard.do_pay()

	def __del__(self):
		if self.isPurchased:
			print('You:: I bought it :) ')
		else:
			print("You:: I can't but it :( ")

class Bank:
	def __init__(self, cardid):
		self.cardid = cardid
		self.account = self.__getAccount()

	def __getAccount(self):
		if self.cardid == 1:
			return 500
		else:
			return 1000

	def __checkAccount(self):
		print("Bank:: checking if card {} has enough funds".format(self.cardid))
		return self.account

	def do_pay(self, account):
		return self.__checkAccount() >= account


class DebitCard:
	def __init__(self):
		self.id = 1
		self.bank = Bank(self.id)

	def do_pay(self):
		return self.bank.do_pay(500.1)


you = You()
you.make_payment()
