# Author:xqkang
# Date:2020/9/21 下午5:11
import sys,time

for i in range(50):
    #屏幕输出
    sys.stdout.write("#")
    #如果不加下面这句话会缓存到内存中一块输出
    sys.stdout.flush()
    time.sleep(0.2)