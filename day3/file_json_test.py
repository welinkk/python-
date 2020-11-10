# Author:xqkang
# Date:2020/9/21 下午3:05
#读
#f = open("test.txt", "a", encoding="utf-8")#f内存对象：文件句柄
# data = f.read()
#data2 = f.read()#X
# print(data)
# print("---------------data2---------")
#print(data2)#不会打印

#读行 一行一行读
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

# for i in range(10):
#     print(f.readline())
'''
#以列表的形式呈现,
print(f.readlines())
#['我爱这土地\n', '近现代 ：艾青\n', '假如我是一只鸟，\n', '我也应该用嘶哑的喉咙歌唱：\n'......]


for line in f.readlines():
    print(line)
'''

#不打印第十行
'''
#只适合小文件，因为将文本数据存到内存中
for index, line in enumerate(f.readlines()):
    if index == 9:
        print("-----------我是第十行--------")
        continue
    print(line)
'''
'''
#f变成迭代器，读一行删一行，占用内存小
count = 0
for line in f:
    if count == 9:
        print("--------10 lines--------")
        count += 1
    else:
        print(line)
        count += 1
'''
'''
#tell打印当前位置的字节数
print(f.tell())
#读取字符数
print(f.read(10))
print(f.tell())
#光标回到n字节，例如从0开始读，如果是汉字不能拆分字符会报错
f.seek(12)
print(f.tell())
print(f.read(10))
print(f.tell())

#打印字符编码
print(f.encoding)

#操作系统中文件的io接口
print(f.fileno())

print(f.name)

#判断是否可移动光标 tty、终端设备文件不能移动光标
print(f.seekable())

#强制将内存中的数据刷进入磁盘中
print(f.buffer)

#判断是否关闭
print(f.closed)
'''
#截断文件中的内容，open（“”，“a”）不写：清空（并没有） 数字n：截取n字节 发现必须写字节位点 但是已经seek到相应字节位点
#跳转到相对应的字节
##f.truncate()
#写
'''
f_w = open("test.txt", "w")
f_w.write("我爱北京天安门....\n")
f_w.write("天安门上太阳升....")

f_w.close()
'''
'''
#append 追加
f_a = open("test.txt", "a")
f_a.write("\n面朝大海，春暖花开")
f_a.close()
'''

#可读写"r+"
# 读写 写只能在最后面写
#f = open("poem.txt", "r+", encoding="utf-8")
# 写读 清空文件 写只能在最后面写
#f = open("poem.txt", "w+", encoding="utf-8")
#追加读写
#f = open("poem.txt", "a+", encoding="utf-8")
#二进制文件 不用加字符编码
'''
f = open("poem.txt", "rb")

print(f.tell())
f.seek(0)
#f.readline()
print(f.readline())
'''
#print("亢学强".encode())
f = open("poem.txt", "wb")
f.write("你好，世界".encode())
