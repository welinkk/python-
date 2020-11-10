# Author:xqkang
# Date:2020/9/22 上午11:32

f = open("yesterday.txt", "r", encoding="utf-8")
# print(f.read())
f1 = open("yesterday2.txt", "w", encoding="utf-8")

for line in f:
    if "赤裸的阳光" in line:
       line = line.replace("赤裸的阳光", "赤裸的美女")
    f1.write(line)

f.close()
f1.close()
