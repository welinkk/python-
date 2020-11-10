# Author:xqkang
# Date:2020/10/8 下午4:11
import json
import pickle

def sayhi():
    print("sayhi")
f = open("a.txt", "rb")
fr = f.read()
#fr = eval(fr)
#data = json.loads(fr)
data = pickle.loads(fr)
print(data["sh"]())
