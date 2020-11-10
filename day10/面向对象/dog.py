# Author:xqkang
# Date:2020/10/16 上午10:08
class Dog:
    def __init__(self, name):
        self.name = name

    def bulk(self):
        print("%s:wang wang wang!" % self.name)

d1 = Dog("shaizi")
d2 = Dog("aaaa")
d3 = Dog("zzzz")
d1.bulk()
d2.bulk()
d3.bulk()
