# Author:xqkang
# Date:2020/10/5 下午7:38
def fun1(x, *args):
    print(x, args)



fun1(1, 2, 3, 33)


#参数转换成字典

def fun2(**kwargs):
    print(kwargs)


fun2(name='kk', age=8, sex='f')
