# Author:xqkang
# Date:2020/10/7 上午11:21


# 1,1,2,3,5,8,13...
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

# print(next(f))
# print(f.__next__())
# print("--------")
# print(f.__next__())
# print(f.__next__())
# print("=========")
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())

while True:
    try:
        x = next(f)
        print("f:", x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break
# for i in f:
#     print(i)
