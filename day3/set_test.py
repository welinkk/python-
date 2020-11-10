# Author:xqkang
# Date:2020/9/21 上午11:45
#集合：无序，没有重复元素

list_1 = [1, 2, 3, 4, 5]
list_1 = set(list_1)
print(list_1, type(list_1))

list_2 = [4, 5, 6, 7, 8]
list_2 = set(list_2)
print(list_2)

# 交集{4, 5}
print(list_1.intersection(list_2))
print(list_1 & list_2)

# 并集{1, 2, 3, 4, 5, 6, 7, 8}
print(list_1.union(list_2))
print(list_1 | list_2)
'''
# 差集{1, 2, 3}
print(list_1.difference(list_2))
print(list_1 - list_2)

# 子集（1是2的子集）
print(list_1.issubset(list_2))

# 父集（2是1的父集）
print(list_2.issuperset(list_1))

# 对称差集（除去交集）{1, 2, 3, 6, 7, 8}
print(list_1.symmetric_difference(list_2))
print(list_1 ^ list_2)

print(list_1.isdisjoint(list_2))


print("\n")
list_3 = [1, 2, 3, 4]
list_3 = set(list_3)

# 添加
list_3.add(999)
print(list_3)

# 添加集合、多项
list_3.update([12, 32, 43, 24])
print(list_3)

# 集合长度
list_3_len = len(list_3)
print(list_3_len)

gg = 12 in list_3
print(gg)

gg = "qw" not in list_3
print(gg)

# 删除没有的话报错
list_3.remove(12)
print(list_3)

# 删除没有不报错
print(list_3.discard(12))

# 删除任意
list_3.pop()
print(list_3)
'''