# Author:xqkang
# Date:2020/10/8 下午4:40
import pickle
def sayhi():
    print(sayhi)

f = open("a.txt", "wb")
b = {"a": "dasda",
     "b": "ada",
     "sh": sayhi
     }

pickle.dump(b, f)
