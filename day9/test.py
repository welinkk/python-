# Author:xqkang
# Date:2020/10/11 上午8:32
import random

check_code = ''
i = random.randrange(0, 4)
for n in range(0, 4):
    if random.randrange(0, 4) == i:
        tmp = chr(random.randint(65, 90))
    else:
        tmp = random.randrange(0, 10)
    check_code += str(tmp)

print(check_code)
