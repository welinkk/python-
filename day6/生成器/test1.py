# Author:xqkang
# Date:2020/10/7 上午10:38

# 生成器的英文名:generator
# 列表生成式
a = [i*2 for i in range(10)]
print(a)

# 相当于:
b = []
for i in range(10):
    b.append(i*2)

print(b)

# 生成器只有在调用的时候才会调用
c = (i*i for i in range(10))
print(c)
# print(c[1000])不能用
print(c.__next__())
print(c.__next__())
print("----------")

# 生成器只记住当前的位置. 此时for循环会从下一个c.__next__()的下一个开始循环
for i in c:
    print(i)
