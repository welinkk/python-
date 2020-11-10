# Author:xqkang
# Date:2020/10/5 下午6:16
def func1():
    print("我是func1")


def func2():
    print("我是func2")
    return 0
def func3():
    print("我是func3")
    return "1", ["1", "sda"], {'name': "kk"}
x = func1()
y = func2()
z = func3()
# 返回0
print("%s" %x)

# 返回none
print("%s" %y)
print("%s %s %s" %z)

