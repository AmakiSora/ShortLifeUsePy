"""
re模块的使用
    re模块是python独有的匹配字符串的模块
"""
import re

'''
    findall(string[, pos[, endpos]])
    匹配字符串中所有的符合正则表达式的内容,返回一个列表
    string : 待匹配的字符串
    pos : 可选参数,指定字符串的起始位置,默认为 0
    endpos : 可选参数,指定字符串的结束位置,默认为字符串的长度
'''
lst = re.findall(r"\d+", "111nmb222")
print(lst)
print('--------------------分割线--------------------')

'''
    re.finditer(pattern, string, flags=0)
    匹配字符串中所有的符合正则表达式的内容,返回一个迭代器
    pattern : 正则表达式
    string : 要匹配的字符串
    flags : 标志位,用于控制正则表达式的匹配方式,如：是否区分大小写,多行匹配等等
'''
lst = re.finditer(r"\d+", "333nmb444")
for i in lst:
    # 从迭代器中拿到内容需要.group()
    print(i.group())
print('--------------------分割线--------------------')

'''
    re.search(pattern, string, flags=0)
    匹配字符串中所有的符合正则表达式的内容,找到一个就返回,返回一个match对象
    pattern : 正则表达式
    string : 要匹配的字符串
    flags : 标志位,用于控制正则表达式的匹配方式,如：是否区分大小写,多行匹配等等
'''
lst = re.search(r"\d+", "555nmb666")
print(lst.group())
print('--------------------分割线--------------------')

'''
    re.match(pattern, string, flags=0)
    从头开始匹配,相当于正则表达式^
    pattern : 正则表达式
    string : 要匹配的字符串
    flags : 标志位,,用于控制正则表达式的匹配方式, 如：是否区分大小写, 多行匹配等等
'''
lst = re.match(r"\d+", "777nmb888")
print(lst.group())
print('--------------------分割线--------------------')

'''
    re.compile(pattern[, flags])
    预加载正则表达式,可通过此对象调用其他方法
    pattern : 一个字符串形式的正则表达式
    flags : 可选,表示匹配模式,比如忽略大小写,多行模式等,具体参数为：
        re.I 忽略大小写
        re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
        re.M 多行模式
        re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
        re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
        re.X 为了增加可读性,忽略空格和 # 后面的注释
'''
z = re.compile(r"\d+")
print(z.findall('999nmb000'))
print('--------------------分割线--------------------')

# 按组匹配获取数据
s = '''
<div class='A'><span id='1'>java</span></div>
<div class='B'><span id='2'>python</span></div>
<div class='C'><span id='3'>go</span></div>
<div class='D'><span id='4'>C</span></div>
<div class='E'><span id='5'>C++</span></div>
'''
# (?P<分组名>正则表达式)
z = re.compile(r"<div class='(?P<class>.*?)'><span id='(?P<id>\d+)'>(?P<data>.*?)</span></div>", re.S)  # re.S可以让其匹配换行符
result = z.finditer(s)
for i in result:
    print(i.group())
    print(i.group('class'))
    print(i.group('id'))
    print(i.group('data'))
    print('--------------------分割线--------------------')

'''
    re.sub(pattern, repl, string, count=0, flags=0)
    用于替换字符串中的匹配项
    pattern : 正则表达式
    repl : 替换的字符串,也可为一个函数
    string : 要被查找替换的原始字符串
    count : 模式匹配后替换的最大次数,默认 0 表示替换所有的匹配
    flags : 标志位,用于控制正则表达式的匹配方式,如：是否区分大小写,多行匹配等等
'''
phone = "2004-959-559 # 这是一个电话号码"

num = re.sub(r'0', "1", phone)  # 替换字符串中的数字0
print(num)

num = re.sub(r'#.*$', "", phone)  # 删除字符串中的 Python注释
print(num)

num = re.sub(r'\D', "", phone)  # 删除非数字(-)的字符串
print(num)
print('--------------------分割线--------------------')


# repl为函数的使用
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)  # 将匹配的数字乘以 2


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
print('--------------------分割线--------------------')

'''
    re.split(pattern, string[, maxsplit=0, flags=0])
    把匹配的子串将字符串分割后返回列表
    pattern : 匹配的正则表达式
    string : 要匹配的字符串
    maxsplit : 分隔次数,maxsplit=1 分隔一次,默认为 0,不限制次数
    flags : 标志位,用于控制正则表达式的匹配方式,如：是否区分大小写,多行匹配等等
'''
l = re.split('(\W+)', ' runoob, runoob, runoob.')
print(l)
print('--------------------分割线--------------------')

l = re.split('a', 'hello world')  # 对于一个找不到匹配的字符串而言,split不会对其作出分割
print(l)
print('--------------------分割线--------------------')
