"""
列表[]
    可变序列
    列表元素是有序的
    可存储重复数据
    可混合类型存储
    根据需要动态分配内存
"""
# 列表初始化1
list1 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print(list1, type(list1), id(list1))

# 列表初始化2
list1 = list([1.0, 2, '3'])
print(list1, type(list1), id(list1))

# 可混合类型存储,可存储重复数据,列表元素是有序的
list1 = ['A', 1, 2.0, 0xE, True, [2, 1], 2.0]
print(list1, type(list1), id(list1))

# 获取元素  列表名[位置]
print(list1[0])  # 取列表中的某个元素
print(list1[-2])  # 倒数第n个数

# 切片,返回一个列表(新的对象)  列表名[起始位置:结束位置:间隔数]
print(list1[:])  # 不写默认0:-1:1
print(list1[::])
print(list1[::-1])  # 间隔数为负数,则逆序输出
print(list1[0:-2])
print(list1[0:-1:2])
print(list1[-1::-1])
print(list1[-1:0:-1])

# 获取元素位置  列表名.index(元素,起始位置,结束位置)
print(list1.index(2))  # 返回元素的位置,如有相同,只返回第一个
print(list1.index('A', 0, -1))  # 在第0个位置到-1个位置查找元素

# 判断列表中某元素是否存在  元素 (not) in 列表名
print(1 in list1)
print(1 not in list1)

# 列表元素的遍历  for 变量 in 列表名
for i in list1:
    print(i)

# 列表的增删改
# 增
print(id(list1))  # 增删改后,id不会改变
list1.append([1, 2, 3])  # 在列表末尾添加元素
print(list1)
list1.extend([1, 2, 3])  # 在列表末尾添加多个元素
print(list1)
list1.insert(1, '666')  # 在列表的某一个位置添加元素
print(list1)

# 改
list1[2:9] = [44, 55, 66]  # 在列表的某个位置覆盖列表
print(list1)
list1[2:] = [11, 22, 33]  # 在列表的某个位置覆盖列表
print(list1)
list1[2] = 111
print(list1)

# 删
list1.remove('666')  # 删除某个元素,重复只删第一个
print(list1)
list1.pop(1)  # 删除某个位置的元素
print(list1)
list1.pop()  # 不写,默认删最后一个
print(list1)
list1[1:] = []  # 可以用空列表覆盖达到删除效果
print(list1)
list1.clear()  # 清空所有元素(变成空列表)
print(list1)
print(id(list1))  # 增删改后,id不会改变

del list1  # 删除对象(不是空列表)

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
