import keyword

'''
数据类型
'''
print('关键字', keyword.kwlist)  # python的关键字,不能作为变量名或函数名使用
a = 'hello'
print('标识', id(a))
print('类型', type(a))
print('值', a)

# 整数类型
b = 1  # 十进制
print(b, type(b))
b = 0b10  # 二进制
print(b, type(b))
b = 0o10  # 八进制
print(b, type(b))
b = 0xE  # 十六进制
print(b, type(b))

b = 3.14  # 浮点数类型
print(b, type(b))
b = 1.1 + 2.2  # 计算会不精确
print(b, type(b))
from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))  # 精确计算

# 布尔类型
b = True
print(b, type(b))
b = True + 0  # 布尔类型可以转成整数类型计算,True为1
print(b, type(b))
b = False + 0  # 布尔类型可以转成整数类型计算,False为0
print(b, type(b))

# 对象的布尔值,以下列举为False的情况
print(bool(0))        # 整数
print(bool(0.0))      # 浮点数
print(bool(None))     # 空
print(bool(''))       # 字符串
print(bool([]))       # 列表
print(bool(list()))   # 列表
print(bool(()))       # 元组
print(bool(tuple()))  # 元组
print(bool({}))       # 字典
print(bool(dict()))   # 字典
print(bool(set()))    # 集合

# 字符串类型
c = '人生苦短,我用python'
print(c, type(c))
c = "人生苦短,我用python"
print(c, type(c))
c = '''
人生苦短,我用python
'''
print(c, type(c))
c = """
人生苦短,我用python
"""
print(c, type(c))

# 强制类型转换
print(int(True))
print(str(233))
print(float("321"))
