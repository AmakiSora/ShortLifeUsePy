"""
字典{}
    可变序列
    字典的元素是无序的
    以键值对的方式存储数据
    key不可重复,value可重复
"""
# 字典的初始化1
d = {'A': 1, 3: 1, True: False}
print(d)

# 字典的初始化2
d = dict(name='cosmos', id='233')
print(d)

# 获取value(通过key)
print(d['name'])  # 找不到会报错
print(d.get('name'))
print(d.get('233'))  # 找不到默认返回None
print(d.get('233', 666))  # 找不到会返回666

# 判断某个key是否存在  key (not) in 字典名
print('name' in d)
print('name' not in d)

# 获取字典中所有的key,返回的类型是dict_keys,可通过list()函数转换成列表
print(dk := d.keys(), type(dk))

# 获取字典中所有的value,返回的类型是dict_values,可通过list()函数转换成列表
print(dv := d.values(), type(dv))

# 获取字典中所有的key-value,返回的类型是dict_items,可通过list()函数转换成元组
print(di := d.items(), type(di))

# 字典的遍历
for i in d:
    print(i, d[i])

# 字典的增删改
# 增
d['age'] = 18
print(d)

# 改
d['age'] = 23
print(d)

# 删
del d['age']  # 删除指定的key
print(d)
d.clear()  # 清空字典
print(d)

# 字典生成式  {key:value for key,value in zip(列表,列表)}
keys = ['A', 'B', 'C']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)
