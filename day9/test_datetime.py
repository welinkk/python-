# Author:xqkang
# Date:2020/10/10 下午6:18
import datetime
import time
# 获取当时间 2020-10-10 18:19:43.753342
#print(datetime.datetime.now())

# 2020-10-10
print(datetime.date.fromtimestamp(time.time()))

# 时间加减
# 获取 三天后 时间 2020-10-13 18:46:28.959719
print(datetime.datetime.now() + datetime.timedelta(3))

# 获取 三天前 时间 2020-10-07 18:47:15.647399
print(datetime.datetime.now() + datetime.timedelta(-3))

# 获取 3小时后 时间 2020-10-10 21:48:57.853997
print(datetime.datetime.now() + datetime.timedelta(hours=3))

# 获取 3小时前 时间 2020-10-10 15:49:28.330983
print(datetime.datetime.now() + datetime.timedelta(hours=-3))

# 获取 30min 后时间 2020-10-10 19:21:26.806662
print(datetime.datetime.now() + datetime.timedelta(minutes=30))

