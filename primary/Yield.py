"""
yield关键字
    yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行。
    yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始。
    带有yield的函数不仅仅只用于for循环中，而且可用于某个函数的参数，只要这个函数的参数允许迭代参数。比如array.extend函数，它的原型是array.extend(iterable)。
"""


# 示例1
def fun1():
    yield 1
    yield from fun2()
    yield 2


def fun2():
    yield 3
    yield 4


f1 = fun1()
for i in f1:
    print(i)

print('-----------------------------------------')


# 示例2
def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=", i)
        # 做一些其它的事情
    print("do something.")
    print("end.")


def call(i):
    return i * 2


# 使用for循环
for i in yield_test(5):
    print(i, ",")
