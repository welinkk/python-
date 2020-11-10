# Author:xqkang
# Date:2020/10/7 下午4:29
'''
# all 列表全真则为真 0是false
print(all([1, 0, -2])) # false
print(all([1, 2, -2])) # True

# any 列表有一个真则为真
print(any([1, 0, -2])) # True
print(any([1, 2, -2])) # True
print(any([])) # False

# ascii
print(ascii([1, 2, "考试大家卡洛斯"])) # [1, 2, '\u8003\u8bd5\u5927\u5bb6\u5361\u6d1b\u65af']
a = ascii([1, 2, "考试大家卡洛斯"])
print(type(a)) # <class 'str'>

# bin 十进制转二进制
print(bin(255)) # 0b11111111

# bool
print(bool([])) # []空为假，有为真,
print(bool([1]))
print(bool(0)) # 0为假，其余为真
print(bool(2))

# bytes
a = bytes("abcde", encoding="utf-8")
print(a) # b'abcde'
print(a.capitalize(), a) # b'Abcde' b'abcde',字节、字符串不能修改，字典列表能修改

# bytearray
b = bytearray("abcde", encoding="utf-8")
print(b) # bytearray(b'abcde')
print(b[0]) # 97
b[1] = 120 # 只能赋值数字，assii码值
print(b) # bytearray(b'axcde')

# callable 判断是否可以带哦用
print(callable([])) # 列表不可以调用 False
def sayhi():
    print("hi")
print(callable(sayhi)) # 函数可以调用 True

# chr 将数字转换成对应的asii码值
print(chr(97)) # a

# ord 将字符转换成asii码对应的值
print(ord("a")) # 97

# compile

code = """
def febo(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        # yeild 可以让函数停下来 有yeild就叫生成器
        yield b
        a, b = b, a+b
        n = n + 1
    return "done"

f = febo(4)

while True:
    try:
        x = next(f)
        print("f:", x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break
"""
py_obj = compile(code, "error.log", "exec")
exec(py_obj)

# dir 查看都有什么方法
print(dir("[]"))

# divmod(a,b) 返回伤和余数
print(divmod(5, 3)) # (1, 2)
print(divmod(10, 6)) # (1, 4)

# 匿名函数 lambda 只使用一次，不可以计算复杂的逻辑结构 但能写三元运算
ss = lambda n: print(n)
ss(5)

ss = lambda n:3 if n>4 else n
print(ss(2))

# filter过滤，一般和lambda合用
res = filter(lambda n: n > 5, range(10))
print(res) # 打印的是迭代器
for i in res:
    print(i)

re = map(lambda n: n*n, range(10))
for i in re:
    print(i)

print("-------")
# 不对
rr = [lambda n: n*2 for n in range(10)]
print(rr)
for i in rr:
    print(i)
'''
import functools
r2 = functools.reduce(lambda x, y: x+y, range(5))
print(r2)


# frozenset 冻结不可变
ss = [12, 1231, 123]
a = frozenset(ss)

# 打印此文件的所有内容
print(globals())

# hex
print(hex(15)) # 0xf

# oct
print(oct(10)) # 0o12

# pow（a,b）  计算a的b次方
print(pow(3, 3)) # 27

# round 保留几位小数
print(round(3.123, 2))

# sorted
b = {1: 2,
     3: 23,
     213: 32,
     -12: 21
     }
print(b)
print(sorted(b.items()))
print(sorted(b.items(), key=lambda x: x[1])) # 按key排序

# zip
a1 = [1, 2, 3, 4]
a2 = ["a", "b", "c", "d"]

for i in zip(a1, a2):
    print(i)

# 结果：
# (1, 'a')
# (2, 'b')
# (3, 'c')
# (4, 'd')
