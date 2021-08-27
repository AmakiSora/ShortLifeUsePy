"""
继承
"""


# 新式类:以object为基类的类(python3默认)
# 经典类:不以object为基类的类(不推荐使用)
class Person:  # 父类 python3默认继承Object类
    def __init__(self, id):
        self.id = id

    def 编号(self):
        print(self.id)

    def 自我介绍(self):
        print("我是一个人")


class Student(Person):  # class 类名(父类名,...) 可继承多个父类 多个父类有重名方法时会按继承顺序调用重名方法(这里不进行展开细说)
    def 自我介绍(self):  # 重写父类方法
        super().自我介绍()  # 可用super()来调用父类方法
        # Person.自我介绍(self)  # 也可以用 父类名.方法名 来调用父类方法(不推荐)
        print("职业是学生")


stu = Student(233)
stu.编号()  # 子类可以使用父类方法
stu.自我介绍()  # 重写后,调用重写的方法
