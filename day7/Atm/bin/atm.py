# Author:xqkang
# Date:2020/10/8 下午5:19
import os
import sys
# 因为在pycharm中下面的会是绝对路径
print(__file__)
# 返回绝对路径/home/xqkang/PycharmProjects/pythonProject1/day7/Atm/bin/atm.py
print(os.path.abspath(__file__))
# 返回dir name /home/xqkang/PycharmProjects/pythonProject1/day7/Atm/bin
print(os.path.dirname(os.path.abspath(__file__)))
# 返回到项目路径名 /home/xqkang/PycharmProjects/pythonProject1/day7/Atm/
SE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 系统添加环境变量
sys.path.append(SE_DIR)
import core, conf

from core import main

main.login()
