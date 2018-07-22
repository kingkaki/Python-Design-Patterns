# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-22 18:22:21
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-22 22:29:21
from abc import ABCMeta, abstractclassmethod

class NewsPublisher:
	def __init__(self):
		self.__subscribers = []
		self.__latestNews = None

	def attach(self, subscriber):
		self.__subscribers.append(subscriber)

	def detach(self):
		return self.__subscribers.pop()

	def subsribers(self):
		return [ type(x).__name__ for x in self.__subscribers ]

	def notifySubscribers(self):
		for sub in self.__subscribers:
			sub.update()

	def addNews(self, news):
		self.__latestNews = news

	def getNews(self):
		return 'Got news: {}'.format(self.__latestNews)


class Subscriber(metaclass=ABCMeta):
	@abstractclassmethod
	def update(self):
		pass

class SMSSubscriber(Subscriber):
	def __init__(self, publisher):
		self.publisher = publisher
		self.publisher.attach(self)

	def update(self):
		print(type(self).__name__, self.publisher.getNews())

class EmailSubscriber(Subscriber):
	def __init__(self, publisher):
		self.publisher = publisher
		self.publisher.attach(self)

	def update(self):
		print(type(self).__name__, self.publisher.getNews())

class AnyOtherSubscriber(Subscriber):
	def __init__(self, publisher):
		self.publisher = publisher
		self.publisher.attach(self)

	def update(self):
		print(type(self).__name__, self.publisher.getNews())

if __name__ == '__main__':
	news_publisher = NewsPublisher() # 定义一个发布者
	for subsriber in [ SMSSubscriber, EmailSubscriber, AnyOtherSubscriber ]:
		subsriber(news_publisher) # 在每个订阅者中注册一个发布者
	print('Subscribers: ', news_publisher.subsribers() )
	print()
	news_publisher.addNews('hello world!') # 添加消息
	news_publisher.notifySubscribers() # 发布消息
	print()
	news_publisher.addNews('second news!')
	news_publisher.notifySubscribers()









