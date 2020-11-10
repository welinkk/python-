# Author:xqkang
# Date:2020/9/18 下午4:14
import copy
# 列表
names = ["zhangsan","lisi","wangwu","zhaoliu","3haoliu","WWWW"]

#
# print(names)
# print(names[0:2])#切片：顾头不顾尾0,1
# print(names[-1])
# print(names[-3:-1])
# print(names[-3:])
# print(names[:3])

# names.append("kxq")
# print(names)


# 取代1原来的位置：['zhangsan', 'kxq', 'lisi', 'wangwu', 'zhaoliu', '3haoliu', 'WWWW']
# names.insert(1, "kxq")
# print(names)
# print(names.index("kxq"))
# names[2]="www"
# print(names)

# 删除
# names.remove("kxq")
# print(names)

# del names[1]
# print(names)
# 删除最后一个 带索引删除索引对应项
# names.pop()
# names.pop(1)
# print(names)

# del可以使切片模式
del names[1]
del names[2:3]
print(names)
# 位置
# print(names.index("www"))
# print(names[names.index("www")])
#
# #count
# print(names.count("kxq"))
#
# #翻转
# names.reverse()
# print(names)

# 清零
# names.clear()
# print(names)


# names.sort()
# print(names)
#
# names2 = [1,2,3]
# names.extend(names2)
# print(names)
#
# del names2

# print(names)
# names = ["zhangsan", "lisi", ["wangwu", "awk"], "zhaoliu", "3haoliu", "WWWW"]

# names2 = names.copy()

# print(names)
# print(names2)

# names[2][0] = "ffff"
# names[1] = "kxq"

# 深copy
# names2 = copy.deepcopy(names)
# names[2][0] = "ffff"
# names[1] = "kxq"
# print(names)
# print(names2)

'''
for i in names:
    print(i)

hhh = names[0:-1:2]
sss = names[::2]
ddd = names[:]
print(hhh)
'''