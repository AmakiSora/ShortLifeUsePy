"""
函数
    支持像java一样的重载
"""


# 函数的定义
def 加法(数字1, 数字2=3):  # def 函数名 (形参):
    结果 = 数字1 + 数字2  # 函数体
    return 结果  # 返回值,返回多个值时,类型为元组


# 函数的调用
print(加法(1, 1))
print(加法(数字1=2, 数字2=2))
print(加法(3))  # 当定义中有默认值,可以不填有默认值的参数
lst = [6, 6]
print(加法(*lst))  # 加*号可将列表转换为对应位置的参数
dic = {'数字1': 11, '数字2': 11}
print(加法(**dic))  # 加**号可将字典转换为对应位置的参数


def 加法(*A):  # *符号代表参数个数可变(元组)
    sum1 = 0
    print(type(A))  # A为元组
    for i in A:
        sum1 += i
    return sum1


print(加法(1, 2, 3, 4, 5))


def 加法(**A):  # **符号代表参数个数可变(字典)
    sum1 = 0
    print(type(A))  # A为字典
    for i in A.values():
        sum1 += i
    return sum1


print(加法(a=1, b=2, c=3))


def 加法(*A, **B):  # **符号代表参数个数可变(元组,字典),*可以在**之前,**不能在*之前
    sum1 = 0
    print(type(A))  # A为元组
    for i in A:
        sum1 += i
    print(type(B))  # B为字典
    for i in B.values():
        sum1 += i
    return sum1


print(加法(1, 2, 3, a=4, b=5, c=6))


def 加法(a, b, *, c, d):  # 在*号后面的参数必须指定
    return a + b + c + d


print(加法(8, 8, c=8, d=8))  # 后两个参数需要按形参名指定
