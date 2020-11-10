# Author:xqkang
# Date:2020/10/7 下午3:43
from collections import Iterable, Iterator

# 可以直接用于for循环的数据类型有以下几种:
# 一类是: list、tuple、dict、set、str
# 一类是 generator， 包括生成器和带yeild的generator function
# 这些可以直接作用于for循环的丢向统称为迭代对象：Iterable
# 可以使用isinstance() 判断一个对象是否是Iterable

a = isinstance([], Iterable) # ture
print(a)
b = isinstance({}, Iterable) # true
print(b)
c = isinstance("abc", Iterable) # True
print(c)
d = isinstance((x for x in range(10)), Iterable) # True
print(d)
e = isinstance(100, Iterable) # False
print(e)

# 可以被next()函数调用并返回一个对象称为迭代器： Iterator

# >>> a=[1,2,3]
# >>> dir(a) 没有next()函数，所以不是迭代器
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# 生成器都是Iterator对象，丹list、dict、str虽然是Iterable,却不是Iterator.
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数

f = isinstance(iter([]), Iterator) # True
print(f)