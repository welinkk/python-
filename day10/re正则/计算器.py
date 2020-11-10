# Author:xqkang
# Date:2020/10/13 下午2:31

import re
a = "1-2*((60-30)+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2)"

def kuohao(a):
    # ['60-30', '-40/5', '9-2*5/3+7/3*99/4*2998+10*568/14', '-4*3', '16-3*2']
    b = re.compile(r'[(]{1,2}(.*?)[)]{1,2}', re.S)
    c = re.findall(b, a)
    print(c)
    return c
# kuohao(a)
def jisuan(a):

    for i in a:
        b = re.split(r'\+|\-')
        print(b)
jisuan(kuohao(a))
def chengchu(cc):

    for i in cc:
        print(i)
        if '*' in i:
            s = re.split('\*', i)
            # print(s)
            # print(s[0].strip())
            # print(float(s[1].strip()))
            # print(float(s[0].strip()) * float(s[1].strip()))
            return float(s[0].strip())*float(s[1].strip())
        if '/' in i:
            s = re.split('\/', i)
            return float(s[0].strip())/float(s[1].strip())
def jiajian(cc):
    for i in cc:
        print(i)
        if '*' in i:
            s = re.split('\+', i)
            return float(s[0].strip())+float(s[1].strip())
        if '/' in i:
            s = re.split('\-', i)
            return float(s[0].strip())-float(s[1].strip())


