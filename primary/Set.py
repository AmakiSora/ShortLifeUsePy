"""
集合{}
    可变序列
    集合的元素是无序的
    元素不能重复
    集合是没有value的字典
"""
# 空集合
s = set()
print(s, type(s), id(s))

# 集合初始化1
s = {True, 'A', 233, 233, 1}
print(s, type(s), id(s))  # 有重复的元素会自动删掉(True本质为1,所以没有1)

# 集合初始化2
s = set(range(5))  # 生成0到4的数字集合
print(s, type(s), id(s))
s = set('hello')  # 将字符串拆成字符,然后存进集合
print(s, type(s), id(s))

# 判断某元素是否在集合中
print('h' in s)
print('h' not in s)

# 集合的增删
# 增
s.add(233)  # 只能添加一个元素
s.add(233)  # 不会重复添加
print(s)
s.update([1, 2, 3])  # 批量增加
s.update({4, 5, 6})
print(s)

# 删
s.remove(1)  # 不存在会抛异常
print(s)
s.discard(132)  # 不存在不会抛异常
print(s)
s.pop()  # 删除任意元素
print(s)
s.clear()  # 删除所有的元素
print(s)

# 集合的关系运算
s = {1, 3, 2, 4}
s1 = {1, 2, 3, 4}
print(id(s), id(s1))
print(s == s1)  # 无序的所以相等(True)
print(s.issubset(s1))  # 相同互为子集(True)
s1 = {1, 2, 3}
print(s.issubset(s1))  # s不是s1的子集(False)
print(s1.issubset(s))  # s1是s的子集(True)
print(s.issuperset(s1))  # s是s1的超集(True)
print(s1.issuperset(s))  # s1不是s的超集(False)
print(s.isdisjoint(s1))  # s和s1有交集(False)
s = {3, 4, 5}
print(s.intersection(s1))  # s和s1的交集
print(s & s1)  # s和s1的交集,等价于intersection()
print(s.union(s1))  # s和s1的并集
print(s | s1)  # s和s1的并集,等价于union()
print(s.difference(s1))  # s的差集
print(s - s1)  # s的差集,等价于difference()
print(s1.difference(s))  # s1的差集
print(s1 - s)  # s1的差集,等价于difference()
print(s.symmetric_difference(s1))  # s和s1的对称差集
print((s - s1) | (s1 - s))  # s和s1的对称差集,等价于symmetric_difference()

# 集合生成式  {元素 for 变量 in 对象}
s = {i for i in range(5)}
print(s)

# 集合判空(方式1)
s = set()
if not s:
    print("s为空")

# 集合判空(方式2)
if s == set():
    print("s为空")

# list去重技巧
l = [1, 1, 3, 3, 5, 6, 6]
s = list(set(l))
print(s)
