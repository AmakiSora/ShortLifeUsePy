"""
类
"""


class Person:
    id = 233  # 类属性,全体实例共用(可有可无)
    count = 0  # 统计Person类的实例个数

    def __new__(cls, *args, **kwargs):  # 创建对象的方法(创建对象时自动调用)
        print('创建对象,分配空间')
        i = super().__new__(cls)
        return i  # 该方法必须返回对象,之后调用__init__方法,__init__方法中的self就是这里返回的对象

    def __init__(self, name):  # 初始化方法(类似java的构造方法)
        self.name = name
        self.gender = None  # (相当于public)
        self.__age = None  # 加上__即为私有属性,只能在类内部调用(相当于java的private)
        # self.count += 1  # 这样加是不会加到类属性里的,只会加到实例对象的count上
        Person.count += 1

    def showName(self):  # 实例方法,只能由实例对象调用
        return self.name

    def __secret(self):  # 加上__即为私有方法,只能在类内部调用(相当于java的private)
        print('私有方法')  # 其实在python中,并没有真正意义的私有,加__其实是对名称进行特殊处理(_类名__私有方法)

    @staticmethod  # 静态方法,参数随意,没有“self”和“cls”参数,但是方法体中不能使用类或实例的任何属性和方法,类和实例对象都可以调用
    def getMsg():  # (和java的静态方法不一样,别弄混)
        return '这是一个Person类'

    @classmethod  # 类方法,第一个参数必须是当前类对象,该参数名一般约定为“cls”,通过它来传递类的属性和方法,类和实例对象都可以调用
    def getPersonNum(cls):
        return cls.count

    def __str__(self):  # 返回对象的描述信息,即print(实例)时输出的内容(必须返回字符串)
        return 'name = ' + self.name

    def __del__(self):  # 对象被销毁前,会被自动调用
        print(self.name + '对象被销毁!')


# 类对象
print(id(Person))
print(type(Person))
print(Person)
print(Person.id)  # 类.属性
Person.id = 111  # 修改类属性
print(Person.getPersonNum())  # 类.类方法(不需要实例)
print(Person.getMsg())  # 类.静态方法(不需要实例)

# 类的实例化对象
p = Person('amakisora')  # 调用构造函数
print(id(p))
print(type(p))
print(p)  # 如果没有定义__str__方法,会输出<__main__.Person object at 某个地址>
print(p.name)  # 实例.属性
print(p.showName())  # 实例.方法
print(Person.showName(p))  # 类.方法(实例)
p.gender = '女'  # 给属性赋值
print(p.gender)
print(p._Person__secret())  # 私有方法其实也可以调用,但是不推荐使用

# 动态绑定(只绑定到实例上)(不推荐使用)
p.abc = 666  # 类中没有的属性也可以赋值(动态绑定值)
print(p.abc)


def method():
    print('类之外的方法!')


p.m = method  # 类中没有的方法也能加上(动态绑定方法)
p.m()
