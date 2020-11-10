# Author:xqkang
# Date:2020/9/19 下午3:34

name = "my name is kxq"
name1 = "my \tname  is {name} age:{age}"
name2 = "my \tname  is {0} age:{1}"
aa = "kxq"
bb = 20
'''
# 句首首字母大写：My name is kxq
print(name.capitalize())

print(name.count("a"))

print(name.center(50, "-"))

# 是否以什么结尾
print(name.endswith("ang"))

# 扩展n个\t str中有"\t"才能扩展
print(name.expandtabs(tabsize=30))

# 查找索引 第一个字母的索引
print(name.find("name"))
print(name.index("name"))
print(name[name.find("name"):8])


# 带入参数
print(name1.format(name="kxq", age=23))
print(name2.format(aa, bb))
print(name1.format_map({'name': 'kxq', 'age': 12}))


# 是否是数字
print(name.isdigit())
print('23'.isdigit())

# 是否是阿拉伯数字
print(name.isalnum())
print('323'.isalnum())

# 是否是大写数字
print(name.isalpha())
print('Askd'.isalpha())

# 是否是十进制
print(name.isdecimal())
print('1231'.isdecimal())

# 是否是合法变量名
print('121a'.isidentifier())

# 字符串是否只有数字组成
print(name.isnumeric())
print('121.1'.isnumeric())

# 是否全是大写
print('MY NAME IS'.isupper())

# 是否全是小写
print('my name is kxq'.islower())

print('my name is'.join(['1', '2', '3']))
print('my name is'.join('==='))
print('+'.join('==='))
'''
print(name.ljust(50, "*"))
print(name.rjust(50, "*"))
'''
print('NAME'.lower())

print(name.upper())

# 去除空行和空格
print('\n      Xqkang'.lstrip())
print('name    \n'.rstrip())
print('  name  '.strip())

# 转密
p = str.maketrans("abcdefghm", "!@#$%^&*/")
print('my name is xqkang'.translate(p))

# 替换
print(name.replace("m", "L"))
print(name.replace("m", "L", 1))
'''
'''
# 右边找到的第一个
print(name.rfind("m"))

print(name.find("m"))

# 分割成列表
print("my name is kxq".split())
print("myjasdlkakasas".split("a"))

# 通过换行形成列表
print("nak\nsdkj".splitlines())

# 大小写替换
print("KXQ kxq".swapcase())
'''
#每个单词首字母大写：My Name Is Kxq
print(name.title())
