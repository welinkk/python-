# Author:xqkang
# Date:2020/10/12 上午10:28

import shutil
'''
a = open("sss/aaa", encoding="utf-8")
b = open("bbb", "w", encoding="utf-8")

# 复制文件
# shutil.copyfileobj(a, b)

# 直接拷贝文件
# shutil.copyfile("aaa", "ccc")

# 拷贝目录 统计目录下使用
# shutil.copytree("sss", "sss1.bak")

# shutil.rmtree("sss1.bak")

# 打包（文件，格式，路径）
shutil.make_archive("sss", "gztar", "/home/xqkang/PycharmProjects/pythonProject1/day9/")
'''

# zipfile 可以添加
import zipfile
z = zipfile.ZipFile("sss.tar.gz", "w")
z.write("test.py")
print("-----")
z.write("test_os.py")
z.close()
