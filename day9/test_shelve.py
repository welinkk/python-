# Author:xqkang
# Date:2020/10/12 下午1:36
# shelve模块是一个简单的k,v将内存数据通过文件持久化模块，可以持久化任何pickle可支持的Python数据格式

import shelve
import datetime
d = shelve.open("shelve_test")
name = {"a": "qwe",
        "b": "asd",
        "c": "zxc"
        }
info = ["asddsa", "asdqw", "asda"]
# D = datetime.datetime.now()
# d["name"] = name
# d["info"] = info
# d["D"] = D
# d.close()
print(d.get("name"))
print(d.get("info"))
print(d.get("D"))
for i in d.items():
        print(i)

