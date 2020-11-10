# Author:xqkang
# Date:2020/10/5 上午11:24
import sys

print(111)
print(sys.getdefaultencoding())
with open("log1", "r") as f:
    print(f.read())

with open("log1", "r") as f, open("log2", "r") as f2:
    print(f.read(), f2.read())
