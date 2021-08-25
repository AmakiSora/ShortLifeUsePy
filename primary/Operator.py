"""
运算符
"""
# 算数运算符
print(1 + 1)  # 加
print(1 - 1)  # 减
print(2 * 2)  # 乘
print(1 / 2)  # 除
print(5 // 2)  # 整除
print(5 % 2)  # 取余
print(2 ** 3)  # 幂

print(9 // -4)  # 整除,一正一负,向下取整
print(-9 // 4)  # 整除,一正一负,向下取整

print(9 % -4)  # 取余,一正一负,带入公式,余数=被除数-除数*商,9-(-4)*(-3)
print(-9 % 4)  # 取余,一正一负,带入公式,余数=被除数-除数*商,-9-4*(-3)

# 赋值运算符
str = 'hello'
a = b = c = 2  # 支持链式赋值
print(a, b, c)

a, b, c = 10, 20, 30  # 支持系列解包赋值
a, b = b, a  # 交换数值
print(a, b, c)

a += 1
a -= 1
a *= 1
a /= 1
a %= 1
a //= 1
a **= 1
# :=海象运算符,py3.8版本提供的,功能是并行赋值,具体使用百度吧

# 比较运算符
a, b, c = 1, 2, 3
print(a > b)  # 大于
print(a < b)  # 小于
print(a >= b)  # 大于等于
print(a <= b)  # 小于等于
print(a == b)  # 等于(对象值的比较)
print(a != b)  # 不等于(对象值的比较)
print(a is b)  # 对象id的比较
print(a is not b)  # 对象id的比较

print(c > b > a)  # 可使用链式表达式

# 布尔运算符
a = True
b = False
print(a and b)  # 当ab都为True,结果为True
print(a or b)  # 当ab都为False,结果为False
print(not a)  # 结果取反,True变False,False变True

s = 'hello'
print('h' in s)
print('h' not in s)

# 位运算符
print(1 >> 2)  # 1向右移两位
print(1 << 2)  # 1向右移两位
print(1 & 2)  # 按位与
print(1 | 2)  # 按位或
print(1 ^ 2)  # 按位异或
