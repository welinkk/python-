# Author:xqkang
# Date:2020/10/6 下午8:03
import time

def timer(func):
    def tt(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print("运行时间为:%s" %(stop_time-start_time))
    return tt

def test1():
    time.sleep(3)
    print("我是test1")

@timer#test2=timer(test2) = tt  test2(name) = tt(name)
def test2(name):
    time.sleep(3)
    print("我是test2")
    print("我是%s" %name)


test2("kk")