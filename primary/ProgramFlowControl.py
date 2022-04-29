"""
程序流程控制
"""
# 分支控制,python没有switch
a, b = 1, 1
# 对于python来说,要严格控制缩进
if a < b:
    print('a < b')
elif a > b:
    print('a > b')
else:
    print('a = b')

print('a = b' if a == b else 'a != b')  # 简写

# pass,什么都不做,占位符,用于需要写语句,但没有想好写什么的地方使用
if a == b:
    pass

# 技巧1,all()
x = "x"
y = "y"
z = 50
if x == "x" and y == "y" and z < 100:
    pass
# 等价于
conditions = [
    x == "o",
    y == "p",
    z < 100,
]
if all(conditions):
    pass

# 技巧2,any()
x = "x"
y = "y"
z = 50
if x == "x" or y == "y" or z < 100:
    pass
# 等价于
conditions = [
    x == "o",
    y == "p",
    z < 100,
]
if any(conditions):
    pass

# 技巧3,
name = "ali"
age = 22
if name:
    print(name)
if name and age > 18:
    print("ok")
# 等价于
print(name if name else "")
name and print(name)
age > 18 and name and print("ok")

# 循环控制
# while的使用
while a == b:
    a -= 1
    print(a)
else:  # else可加载while或for的最后
    print('a != b')

while a != 10:
    a += 1
    print('现在a =', a)
    if a == 3:
        a += 1
        continue  # 结束本次循环,开始下次循环
    if a == 6:
        break  # 跳出循环
print(a)

# for的使用
for i in 'hello':
    print(i)

for i in range(5):
    print(i)
