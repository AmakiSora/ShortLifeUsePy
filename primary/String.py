"""
字符串
    不可变序列
"""
# 字符串初始化
s = 'Amaki Sora'
print(s, type(s), id(s))
s = "Amaki Sora"
print(s, type(s), id(s))
s = '''Amaki Sora'''
print(s, type(s), id(s))  # 和java常量池类似(不完全相同),相同内容id一样

# 字符串大小写转换
print(s.upper())  # 所有字母转成大写
print(s.lower())  # 所有字母转成小写
print(s.swapcase())  # 大写的转成小写,小写的转成大写
print(s.capitalize())  # 第一个字符转大写,其他转小写
print(s.title())  # 每个单词的第一个字符转大写,其他转小写(字母只要分隔了,就当是一个单词)

# 字符串对齐
print(s.center(20, '.'))  # 居中对齐  center(宽度,填充符(默认空格))  如果设置宽度小于实际宽度则返回原字符串
print(s.ljust(20, '.'))  # 左对齐    ljust(宽度,填充符(默认空格))  如果设置宽度小于实际宽度则返回原字符串
print(s.rjust(20, '.'))  # 右对齐    rjust(宽度,填充符(默认空格))  如果设置宽度小于实际宽度则返回原字符串
print(s.zfill(20))  # 右对齐  zfill(宽度) 左边用0填充  如果设置宽度小于实际宽度则返回原字符串
print('-1234'.zfill(10))  # 遇到'+'或'-'符号会在符号后填充0

# 字符串的截取(和列表切片类似)
print(s[0])
print(s[:])
print(s[3:5])
print(s[::2])

# 字符串的分割  split(分割符,最大分割次数)
print(s.split())  # 从左边开始分割,默认分割符是空格,返回值是列表
print(s.rsplit())  # 从右边边开始分割,默认分割符是空格,返回值是列表
print(s.split('a'))  # 指定分割符
print(s.split('a', 1))  # 限制分割次数

# 字符串的判断
print('张三'.isidentifier())  # 判断字符串是否是合法的标识符(标识符支持中文了!)
print('    \t  '.isspace())  # 判断字符串是否全部由空白字符组成(回车,换行,水平制表符)
print('AmakiSora'.isalpha())  # 判断字符串是否全部由字母组成
print('中文也是字母'.isalpha())  # 判断字符串是否全部由字母组成(全中文也算,混搭不算)
print('2333333'.isdecimal())  # 判断字符串是否全部由十进制数字组成
print('0233330'.isnumeric())  # 判断字符串是否全部由数字组成
print('一1壹Ⅰ'.isnumeric())  # 判断字符串是否全部由数字组成(中文数字,罗马数字也算,离谱)
print('张三buy233'.isalnum())  # 判断字符串是否全部由字母和数字组成(中文算字母)

# 字符串的查询
print(s.index('a'))  # 查找第一次出现元素的位置,没有则抛出异常
print(s.rindex('a'))  # 查找最后一次出现元素的位置,没有则抛出异常
print(s.find('a'))  # 查找第一次出现元素的位置,没有则返回-1
print(s.rfind('a'))  # 查找最后一次出现元素的位置,没有则返回-1

# 字符串的替换  replace(被替换的字符串,替换的字符串,最大替换次数)
print(s.replace('Sora', 'cosmos'))

# 字符串的合并  分隔符.join(对象)
print('.'.join(['Amaki', 'Sora', 'COSMOS']))
print('|'.join('AmakiSora'))

# 字符串的比较
print('Amaki' > 'Amaka')  # 逐个字符进行比较,比较字符的ASCII码
print('Amaki' > 'amaki')  # 逐个字符进行比较,比较字符的ASCII码(第一个比较出结果后,后续不再比较)

# 字符串的格式化
name, id = 'amaki', 233
print('name = {0}, id = {1}'.format(name, id))  # {位置}
print(f'name = {name}, id = {id}')  # 前面记得加f
print('name = %s, id = %d' % (name, id))  # C语言既视感
print('%10d' % 666)  # %宽度d,默认填充空格
print('%10.3f' % 3.14159)  # %宽度.精度f
print('{0:.3f}'.format(3.1415926))  # {位置:宽度.精度f}

# 字符串的编码与解码
print(e1 := '牛的'.encode('GBK'))  # 编码,GBK一个中文占两个字节
print(e2 := '牛的'.encode('UTF-8'))  # 编码,UTF-8一个中文占三个字节
print(e1.decode('GBK'))  # 解码,用不同的编码格式会抛出异常
print(e2.decode('UTF-8'))  # 解码,用不同的编码格式会抛出异常

# 字符串判空
s = ''
if not s:
    print("s为空")
