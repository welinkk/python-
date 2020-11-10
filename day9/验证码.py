# Author:xqkang
# Date:2020/10/10 下午7:23

# 验证码具有数字和字母
import random

checkcode = ''

for i in range(0, 4):
    j = random.randrange(0, 4)
    if i == j:
        # 将数字转化成字母
        tmp = chr(random.randrange(65, 90))
    else:
        tmp = str(random.randint(1, 9))

    checkcode += str(tmp)

print(checkcode)

