# Author:xqkang
# Date:2020/10/8 上午8:38
import json
import pickle
def sayhi():
    print(sayhi)

f = open("a.txt", "w")
b = {"a": "dasda",
     "b": "ada",
     }


# f.write(str(b))
json.dump(b, f)

# pickle 可以存二进制文件，内存文件，json不可以
# f.write(pickle.dumps(b))

f.close()
