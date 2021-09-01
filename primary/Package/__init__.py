"""
包
    包是一个包含多个模块的特殊目录
    目录下必须要有__init__.py文件
    包名的命名方式和变量名一致
    使用import 包名 可以一次性导入包中所有的模块
    要在其他地方使用包中的模块,需要在__init__.py中指定对外提供模块的列表
"""
# from 目录(.代表当前目录) import 模块
from . import test1
from . import test2
