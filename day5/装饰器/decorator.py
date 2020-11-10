# Author:xqkang
# Date:2020/10/6 下午4:07

# 装饰器:
# 定义:本质是函数,(装饰其他函数)就是为其他函数添加附加功能
# 原则:1.不能修改被装饰的函数的源代码
#     2.不能修改被装饰的函数的调用方式
import time

def timer(func):
    def warpper(*args, **kwargs):
        starttime = time.time()
        func()
        stoptime = time.time()
        print("运行时间为:%s" %(int(stoptime-starttime)))
    return warpper

@timer
def timeq():
    time.sleep(3)
    print("我是welin")

timeq()

# 高阶函数
# bar就是门牌号
def bar():
    print("i'm bar")

def fun1(fun):
    print(fun)# (打印内存地址)
    fun()# (函数即是变量)

fun1(bar)
