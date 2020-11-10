# Author:xqkang
# Date:2020/10/6 下午7:35
import time

def timer(func):
    def tt():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("运行时间为:%s" %(stop_time-start_time))
    return tt

def test1():
    time.sleep(3)
    print("我是test1")

@timer
def test2():
    time.sleep(3)
    print("我是test2")

# test1 = timer(test1)
# test1()#和下面的效果一样

test2()