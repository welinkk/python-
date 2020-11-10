# Author:xqkang
# Date:2020/10/12 下午4:51
import re
""""
# <_sre.SRE_Match object; span=(0, 4), match='kang'>
print(re.match("^kang", "kangxueqiang"))

# 匹配一个数字 \d <_sre.SRE_Match object; span=(0, 5), match='kang1'>
print(re.match("^kang\d", "kang12132xue32qiang"))
res = re.match("^kang\d", "kang12132xue32qiang")
# group 只打印匹配到的字符
print(res.group())

# 匹配多个数字 \d+ <_sre.SRE_Match object; span=(0, 9), match='kang12132'>
print(re.match("^kang\d+", "kang12132xue32qiang"))

# . 匹配除 \n 之外的任意一个字符，若制定 flag DOTALL， 则匹配任意字符，包括换行
# <_sre.SRE_Match object; span=(0, 19), match='kang12132xue32qiang'>
print(re.match("^.+", "kang12132xue32qiang"))

# $ 匹配结尾
print(re.match("^.+g$", "kang12132xue32qiang"))
print(re.search("x.+e", "kang12132xue32qiang"))

# xue32qiang
print(re.search("x.+g", "kang12132xue32qiang"))
# ang12132xue32qiang
print(re.search("a.+g", "kang12132xue32qiang"))
# ang        只匹配第一个，匹配到就返回
print(re.search("i[a-z]+g", "kaiasng12132xue32qiaddng"))

print(re.search("#.+#", "asd#skfn#dfs"))

# ? 匹配前一个字符0次或1次
# [0-9]{m} 匹配前一个字符m次    <_sre.SRE_Match object; span=(13, 16), match='321'>
print(re.search("[0-9]{3}", "asd1#sk22fn#d321fs"))

# findall 查找所有  ['1', '22', '321']
print(re.findall("[0-9]{1,3}", "asd1#sk22fn#d321fs"))

#  ['ABC', 'abc']
print(re.search("abc|ABC", "ABCabcaddsf").group())
print(re.findall("abc|ABC", "ABCabcaddsf"))

# \A 同 ^ ,\Z 同 $
print(re.findall("\Aa.+d\Z", "asdasd"))

# \d 匹配数字 0-9
# \D 匹配非数字
# \w 匹配数字字母 [A-Za-z0-9] das234asd32
print(re.search("\w+", "das234asd32*)_%$"))
# \W匹配非数字字母

# \s 匹配空白字符、\t、\n、\r，
print(re.findall("\s", "ab\ts\n123"))

# (?P<id>[0-9]+) 分组 返回结果：{'id': '213'}
print(re.search("(?P<id>[0-9]+)", "dsh213j239812as").groupdict())
# {'id': '213', 'name': 'j'}
print(re.search("(?P<id>[0-9]+)(?P<name>[a-z]+)", "dsh213j239812as").groupdict())
# [('213', 'j'), ('239812', 'as')]
print(re.findall("(?P<id>[0-9]+)(?P<name>[a-z]+)", "dsh213j239812as"))
# {'addr': '130221', 'birthday': '19930206'}
print(re.search("(?P<addr>[0-9]{6})(?P<birthday>[\d]{8})", "130221199388888888").groupdict())

# 分割 split ['as', 'ad', 'f', 'xvc', 'sa']
print(re.split("[0-9]+", "as23ad32f4xvc45sa"))

# 替换 ads|ad|
print(re.sub("[0-9]+", "|", "ads123ad23", count=2))

# 忽略大小写 <_sre.SRE_Match object; span=(0, 11), match='adaasdfasdA'>
print(re.search("[a-z]+", "adaasdfasdA", flags=re.I))
print(re.search("[a-z]+", "adaasdfasdA", re.I))

# re.M 换行也可以用 <_sre.SRE_Match object; span=(5, 9), match='adaa'>
print(re.search("^[a-z]+", "1231\nadaa\nsdfasdA", re.M))
"""
# X没起作用
print(re.search(".+", "1231\nadaa\nsdfasdA", re.S))

print(re.search("(?P<addr>[\d]{6})(?P<birthday>[\d]{8})", "130221199800000000").groupdict())