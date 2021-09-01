"""
模块
    如果有同名方法或变量,后面导入的模块会覆盖前面导入的模块
    调用其他的模块时,模块文件中没有缩进的语句会自动执行
"""
# 模块的导入1  import 模块名 as 自定义模块名
import ModuleTest as m

# 模块的调用1  模块名.方法 或 自定义模块名.方法  导入模块的所有工具
print(m.name)
print(m)
print(id(m))
print(type(m))

# 模块的导入2  from 模块名 import 工具名(*)  导入部分工具(*导入全部工具)
from ModuleTest import name

# 模块的调用2  from..import不用指定模块名
print(name)

# 包的导入 import
import Package

# 包中模块的调用 包.模块.方法
Package.test1.t1()
Package.test2.t2()
