# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-20 15:46:33
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-20 16:59:45
'''
首先检测该类是否有instance属性
没有就创建一个示例，有则直接返回

输出结果：
<__main__.Singleton object at 0x03A302D0>
<__main__.Singleton object at 0x03A302D0>
'''
class Singleton():
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super().__new__(cls)
		return cls.instance

s1 = Singleton()
s2 = Singleton()

print(s1)
print(s2)
