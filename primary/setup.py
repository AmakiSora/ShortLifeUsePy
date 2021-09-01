"""
发布模块
      制作发布压缩包必须要有setup.py文件
      在终端里执行命令 python setup.py build 构建模块,构建后会出现一个build目录
      在终端里执行命令 python setup.py sdist 生成压缩包,生成后会出现一个dist目录,dist里面的压缩包即为要发布的包
安装模块
      在拿到压缩包后,先用命令 tar zxvf 压缩包名 解压压缩包
      用管理员身份安装 sudo python setup.py install 安装模块,模块会安装在python的目录中
卸载模块
      找到包的安装目录,一般在python/dost-packages中
      也可以用 包名.__file__ 来获取模块的安装目录
      直接删除对应的包即可
"""
from distutils.core import setup

setup(name='Package',  # 包名
      version='1.0',  # 版本名
      description='测试发布包',  # 描述信息
      long_description='测试发布包',  # 完整描述信息
      author='COSMOS',  # 作者
      author_email='961737902@qq.com',  # 作者邮箱
      url='amaki-sora.cn',  # 主页
      py_modules=['Package.test1',  # 包含的模块
                  'Package.test2'])
