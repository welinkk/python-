# Author:xqkang
# Date:2020/9/19 下午6:08

#字典 key:value
# 特性：无序

info = {
    'stu1101': "Xiaoze Maliya",
    'stu1102': "Longze Luola",
    'stu1103': "Tenglan Wu"
}
'''
print(info)

print(info["stu1102"])

# 添加和修改
info["stu1104"] = "Cangjing Kong"
print(info)

info["stu1103"] = "武藤兰"
print(info)

# 删除
#del info["stu1103"]
info.pop("stu1103")
# 随机删除
#info.popitem()
print(info)

# 当不确定是否有查找的key时不要用下面方法，否则报错,可以用get
#print(info["stu110322"])

print(info.get("stu110322"))

# 判断key是否在字典中
print("stu110322" in info)
print("stu1102" in info)
'''
b = {
    "stu1101": "ddd",
    1: 2,
    2: 3
}
'''
# 将b字典添加到info字典，有相同的key则修改，没有则添加
info.update(b)

print(info)

# 把字典转成列表
print(info.items())


#创建新dict
c = b.fromkeys([1, 2, 3])
print(c)

d = info.fromkeys([6, 7, 8], "test")
print(d)
'''
# 修改一个全改
e = dict.fromkeys([6, 7, 8], [1, {"name": "kxq"}, 888])
e[6][1]["name"] = "Jack Chen"
print(e)
'''
# 遍历
for i in info:
    print(i, info[i])

# 慢（字典换成列表再输出）
for k, v in info.items():
    print(k, v)
'''