"""
异常处理
    常见的异常:
        ZeroDivisionError 除数为0
        IndexError 序列中无此索引
        KeyError 对象中无此key
        NameError 未声明/初始化对象
        SyntaxError 语法错误
        ValueError 无效参数
"""
import traceback

try:  # 可能抛出异常的代码
    a = 100
    b = int(input())
    c = a / b
except ZeroDivisionError:  # 除数为0异常
    print('除数不能为0!')
    # traceback.print_exc()  # 打印异常信息(其他线程打印的,所以显示位置不确定)
except ValueError:  # 输入异常
    print('输入不是数字!')
except BaseException:  # 所有的异常
    print('总之就是出错啦!')
else:  # 如果没有异常则执行以下代码
    print(c)
finally:  # 无论是否发生异常都执行以下代码
    print('老Java了!')
