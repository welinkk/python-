# Author:xqkang
# Date:2020/10/6 下午2:52
def add(a, b, f):
    return f(a) + f(b)
res = add(3,-6,abs)
print(res)
