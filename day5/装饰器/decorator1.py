# Author:xqkang
# Date:2020/10/6 下午6:59
import time

def funtest(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print("运行时间%s" %(start_time-stop_time))

def test1():
    time.sleep(3)
    print("我是test1")

def test2():
    time.sleep(3)
    print("我是test2")

funtest(test1)
funtest(test2)