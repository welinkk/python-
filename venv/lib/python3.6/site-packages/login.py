# Author:xqkang
# Date:2020/9/15 下午6:50
import getpass

user = "kxq"
pwd = "123456"
count = 0
while count < 3:
    input_name = input("your name:")
    input_pwd = input("your pwd:")
    if input_name == user and input_pwd == pwd:
        print("welcome {0} login...".format(user))
        break
    else:
        print("wrong username and password!!!")
    count += 1
else:
    print("you have tried too many times")
