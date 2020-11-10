# Author:xqkang
# Date:2020/10/7 下午2:30

import time

def consumer(name):
    print("%s 准备吃包子了" % name)
    while True:
        baozi = yield
        print("包子%s来了,被%s吃了" % (baozi, name))

# c = consumer("二傻子")
# c.__next__()
# c.__next__()

def producer(name):
    c = consumer("A")
    c2 = consumer("B")
    c.__next__()
    c2.__next__()
    print("老子开始做包子了")
    for i in range(10):
        time.sleep(1)
        print("做了一个包子,分两半")
        c.send(i+1)
        c2.send(i+1)


producer("二傻子")
