"""
列表[]
    可变序列
    列表的元素是有序的
    可存储重复数据
    可混合类型存储
    根据需要动态分配内存
"""
# 空列表
l = []
print(l, type(l), id(l))

# 列表初始化1
l = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print(l, type(l), id(l))

# 列表初始化2
l = list([1.0, 2, '3'])
print(l, type(l), id(l))

# 可混合类型存储,可存储重复数据,列表元素是有序的
l = ['A', 1, 2.0, 0xE, True, [2, 1], 2.0]
print(l, type(l), id(l))

# 获取元素  列表名[位置]
print(l[0])  # 取列表中的某个元素
print(l[-2])  # 倒数第n个数

# 切片,返回一个列表(新的对象)  列表名[起始位置:结束位置:间隔数]
print(l[:])  # 不写默认0:-1:1
print(l[::])
print(l[::-1])  # 间隔数为负数,则逆序输出
print(l[0:-2])
print(l[0:-1:2])
print(l[-1::-1])
print(l[-1:0:-1])

# 获取元素位置  列表名.index(元素,起始位置,结束位置)
print(l.index(2))  # 返回元素的位置,如有相同,只返回第一个
print(l.index('A', 0, -1))  # 在第0个位置到-1个位置查找元素

# 判断列表中某元素是否存在  元素 (not) in 列表名
print(1 in l)
print(1 not in l)

# 列表元素的遍历  for 变量 in 列表名
for i in l:
    print(i)

# 列表的增删改
# 增
print(id(l))  # 增删改后,id不会改变
l.append([1, 2, 3])  # 在列表末尾添加元素
print(l)
l.extend([1, 2, 3])  # 在列表末尾添加多个元素
print(l)
l.insert(1, '666')  # 在列表的某一个位置添加元素
print(l)

# 改
l[2:9] = [44, 55, 66]  # 在列表的某个位置覆盖列表
print(l)
l[2:] = [11, 22, 33]  # 在列表的某个位置覆盖列表
print(l)
l[2] = 111
print(l)

# 删
l.remove('666')  # 删除某个元素,重复只删第一个
print(l)
l.pop(1)  # 删除某个位置的元素
print(l)
l.pop()  # 不写,默认删最后一个
print(l)
l[1:] = []  # 可以用空列表覆盖达到删除效果
print(l)
l.clear()  # 清空所有元素(变成空列表)
print(l)
print(id(l))  # 增删改后,id不会改变

del l  # 删除对象(不是空列表)

# 生成列表  [列表元素 for 变量 range(起始范围,结束范围)]
lst = [i for i in range(1, 10)]
print(lst)
lst = [i * 2 for i in range(1, 10)]
print(lst)

# 列表排序
lst = [3, 4, 2, 2, 1, 5, 9]
print(lst, id(lst))
lst.reverse()  # 列表反转
print(lst)
lst.sort()  # 默认是升序
print(lst)
lst.sort(reverse=True)  # 变为降序
print(lst)
print(lst, id(lst))  # 以上操作不产生新对象
print(l := sorted(lst), id(l))  # 产生新对象的排序方法
print(l := sorted(lst, reverse=True), id(l))  # 降序

# 统计某元素在列表中的个数
print(lst.count(2))
