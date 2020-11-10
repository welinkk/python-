# Author:xqkang
# Date:2020/10/12 下午4:11

import hashlib
'''
m = hashlib.md5(b'hello')
print(m.hexdigest())
m.update(b"It's me")
print(m.hexdigest())
m.update(b"It's been a long time since we spoken...")
print(m.hexdigest())

# sha1,sha256,sha512
s2 = hashlib.sha1()
s2.update(b'helloTts me')
print(s2.hexdigest())

hh = hashlib.md5("口吐芬芳".encode(encoding="utf-8"))
print(hh.hexdigest())
import hmac
# 
h = hmac.new(b"12345", b"you are 250")
print(h.digest())
'''
import hmac
hhh = hmac.new("天王盖地虎，你是250".encode(encoding="utf-8"))
print(hhh.hexdigest())
