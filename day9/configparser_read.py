# Author:xqkang
# Date:2020/10/12 下午4:00
import configparser
conf = configparser.ConfigParser()
conf.read("example.ini")
# 打印default默认参数
print(conf.defaults())
# 打印节点参数 没有default
print(conf.sections())

print(conf['bitbucket.org']['user'])

sec = conf.remove_section('bitbucket.org')
conf.write(open('example2.ini', 'w'))
