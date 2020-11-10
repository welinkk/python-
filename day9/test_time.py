# Author:xqkang
# Date:2020/10/10 下午3:44
import time

'''
# localtime
print(time.localtime())
# time.struct_time(tm_year=2020, tm_mon=10, tm_mday=10, tm_hour=16, tm_min=0, tm_sec=20, tm_wday=5, tm_yday=284, tm_isdst=0)

# time.time 时间戳 从1970-1-1 0:00开始算起
print(time.time())
# 1602316910.8096082

# timezone 时区 东八区 单位秒
print(time.timezone/3600)

# 夏令时 和utc的差值
print(time.altzone)

# 是否使用夏令时
print(time.daylight)

# sleep
#time.sleep(1)

# gmttime 不加参数本地当前时间 转换成元祖的模式
print(time.gmtime(time.time()))
# time.struct_time(tm_year=2020, tm_mon=10, tm_mday=10, tm_hour=9, tm_min=26, tm_sec=43, tm_wday=5, tm_yday=284, tm_isdst=0)
print(time.gmtime())
x = time.gmtime(time.time())
print(x.tm_year)

# time.strftime按照一定的格式输出 1919-03-24 14:24:00
print(time.strftime("%Y-%m-%d %H:%M:%S", x))

# time.mktime(x) 将元祖的时间转化为时间戳
print(time.mktime(x))


# strftime (“格式”，time.localtime()) --> "格式化的字符串"
# strptime ("格式化的字符串"，"格式") --> struct_time
print(time.strptime("2020-10-10 09:42:17", "%Y-%m-%d %H:%M:%S"))

# 加入变量秒 Sat Oct 10 18:15:46 2020
print(time.ctime())

# 加入变量元祖 Sat Oct 10 18:17:01 2020
print(time.asctime())

import datetime
print(time.time())
print(time.localtime())
print(datetime.datetime.now())
x = time.localtime()
print(time.ctime())
print(time.mktime(x))
y = time.time()
'''
print(time.asctime(time.strptime("2020-10-10 09:42:17", "%Y-%m-%d %H:%M:%S")))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.asctime(time.localtime()))
