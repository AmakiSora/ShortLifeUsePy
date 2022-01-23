"""
Asyncio模块的使用(python3.4以后的版本使用,3.5以上版本不推荐使用)
    asyncio 是用来编写 并发 代码的库，使用 async/await 语法。
    asyncio 被用作多个提供高性能 Python 异步框架的基础，包括网络和网站服务，数据库连接库，分布式任务队列等等。
    asyncio 往往是构建 IO 密集型和高层级 结构化 网络代码的最佳选择。
"""
import asyncio


@asyncio.coroutine
def fun1():
    print(1)
    yield from asyncio.sleep(2)  # 遇到IO耗时操作时,程序会自动切换到task中的其他任务
    print(2)


# yield是手动切换的,而asyncio是遇到io阻塞自动切换
@asyncio.coroutine
def fun2():
    print(3)
    yield from asyncio.sleep(2)  # 遇到IO耗时操作时,程序会自动切换到task中的其他任务
    print(4)


tasks = [
    asyncio.ensure_future(fun1()),
    asyncio.ensure_future(fun2())
]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
# 如用python3.8以上版本,会报错提示无须装饰器(可忽略错误)
