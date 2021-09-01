"""
文件
    打开文件(open)
        访问方式:
            r 只读方式,如果文件不存在抛出异常
            w 只写方式,如果文件存在会被覆盖,如果文件不存在会创建
            a 追加方式,如果文件存在,文件指针会在文件结尾,如果不存在会创建新文件写入
            r+读写方式,文件指针在文件开头,如果文件不存在抛出异常
            w+读写方式,如果文件存在会被覆盖,如果文件不存在会创建
            a+读写方式,如果文件存在,文件指针会在文件结尾,如果不存在会创建新文件写入
    读取文件(read)
    写入文件(write)
    关闭文件(close)
    管理文件(os模块)
"""
# 打开文件 open(文件路径,访问方式) 访问方式默认是r(只读方式)
file = open('D:\\cosmos\\test\\1.txt', 'r+')
# 读取文件
text = file.readline()  # 读取一行
print(text)
text = file.read()  # read()后,文件指针会在文件末尾
print(text)
# 写入文件
file.write("阿这")
# 关闭文件
file.close()

# 管理文件
import os

# 目录列表 os.listdir(路径)
print(os.listdir('D:\\cosmos\\test'))
# 创建目录 os.listdir(路径) 当目录已存在时,抛出异常
os.mkdir('D:\\cosmos\\test\\233')
# 删除目录 os.rmdir(路径) 当目录不存在时,抛出异常
os.rmdir('D:\\cosmos\\test\\233')
# 获取当前目录 os.getcwd()
print(os.getcwd())
# 修改工作目录 os.chdir(路径) 当目录不存在时,抛出异常
os.chdir('D:\\cosmos\\test')
# 判断是否为目录 os.path.isdir(路径)
print(os.path.isdir('D:\\cosmos\\test\\1.txt'))
# 文件重命名 os.rename(源路径,目标路径)
os.rename('D:\\cosmos\\test\\1.txt', 'D:\\cosmos\\test\\233.txt')
# 删除文件 os.remove(路径)
os.remove('D:\\cosmos\\test\\233.txt')
