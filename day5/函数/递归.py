# Author:xqkang
# Date:2020/10/6 上午11:50

def calc(n):
    print(n)
    if int(n/2) > 0:
        return calc(int(n/2))
    print("->", n)
calc(10)