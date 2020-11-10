# Author:xqkang
# Date:2020/9/22 下午1:35
# 实现类似于Linux中的sed的简单替换功能
import sys

file = sys.argv[1]
str_old = sys.argv[2]
str_new = sys.argv[3]
file_new = ('%s.bak' %file)
print(file, str_old, str_new)

file_r = open(file, "r", encoding="utf-8")

file_w = open(file_new, "w", encoding="utf-8")

for line in file_r:
    if str_old in line:
        line = line.replace(str_old, str_new)
    file_w.write(line)
file_r.close()
file_w.close()
