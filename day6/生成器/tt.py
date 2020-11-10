# Author:xqkang
# Date:2020/10/7 下午3:02
import time

def consumer(name):
    print("%s来吃包子了" % name)
    while True:
        baozi = yield
        print("%s开始吃包子%s" % (name, baozi))

def producer(name):
    print("老子开始生产包子了")
    c = consumer(name)
    # __next__()必须的,执行他才能执行yield
    c.__next__()
    for i in range(10):
        time.sleep(1)
        print("生产了包子%s" % (i+1))
        c.send(i+1)

# send发送数据到生成器yield
# next不发送数据

producer("大傻子")