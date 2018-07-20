# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-20 16:56:39
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-20 17:02:42
'''
不同示例共用同一变量
将变量赋值给__dict__特殊变量

<__main__.Borg object at 0x02C90850>
<__main__.Borg object at 0x02C904F0>
{'_shared_state': {1, 2, 3}}
{'_shared_state': {1, 2, 3}}
'''
class Borg:
	_shared_state  = {}

	def __new__(cls, *args, **kwargs):
		obj = super().__new__(cls, *args, **kwargs)
		obj.__dict__ = cls._shared_state
		return obj

b1 = Borg()
b2 = Borg()
print(b1)
print(b2)
b1._shared_state = {1,2,3}
print(b1.__dict__)
print(b2.__dict__)