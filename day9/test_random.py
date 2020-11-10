# Author:xqkang
# Date:2020/10/10 下午6:53
import random

# 随机 0-1 之间的值 0.09302718144026756
print(random.random())
# 随机后去浮点数， 可以指定区间
print(random.uniform(-2, 9))

# 随机整数 需要给一个范围 7
print(random.randint(1, 10))

# 整数 顾头不顾尾 1,2
print(random.randrange(1, 3))

# rang 都是顾头不顾尾 1,2
for i in range(1, 3):
    print(i)

# 随机获取字符 o
print(random.choice("hello"))
# 2
print(random.choice([1, 2, 3]))
# org
print(random.choice(["apple", "org", "orange", "pear", "lemon"]))
# 随机获取两个字符 ['l', 'e']
print(random.sample('hello', 2))

# 洗牌功能
items = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(items)
# [7, 8, 5, 1, 2, 4, 3, 6]
print(items)



