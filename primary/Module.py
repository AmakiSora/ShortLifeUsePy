"""
模块
    如果有同名方法或变量,后面导入的模块会覆盖前面导入的模块
"""
# 模块的导入1  import 模块名 as 自定义模块名
import sys as sys

# 模块的调用1  模块名.方法 或 自定义模块名.方法  导入模块的所有工具
print(sys.version)
print(sys)
print(id(sys))
print(type(sys))

# 模块的导入2  from 模块名 import 工具名(*)  导入部分工具(*导入全部工具)
from sys import version

# 模块的调用2  from..import不用指定模块名
print(version)
