"""
元组()
    不可变序列
    元组的元素不能修改
    没有增删改操作
"""
# 空元组
t = ()
print(t, type(t), id(t))

# 元组初始化1
t = (1, 'A', True)
print(t, type(t), id(t))
t = (1,)  # 如果元组只包含一个元素需要使用逗号和小括号
print(t, type(t), id(t))

# 元组初始化2
t = tuple(('B', 0, [1, 2, 3], False))
print(t, type(t), id(t))

# 获取元组中的元素(和列表类似)
print(t[0])
print(t[1:-1])

# 计算元组中某元素的个数
print(t.count(0))  # 注意False的值也为0,所以有两个0

# 元组内元素id不可变,但是元组内的字典和列表都可以改变
t[2].extend([4, 5, 6])
print(t)

# 判断某元素是否在元组中
print(0 in t)
print(0 not in t)

# 元组的遍历
for i in t:
    print(i)

# 删除元组
del t

# 元组判空
t = ()
if not t:
    print('t为空')

if t == ():
    print('t为空')
