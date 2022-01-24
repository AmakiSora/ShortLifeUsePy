"""
asyncio模块的使用(python3.4以上的版本使用)
    asyncio 是用来编写 并发 代码的库，使用 async/await 语法。
    asyncio 被用作多个提供高性能 Python 异步框架的基础，包括网络和网站服务，数据库连接库，分布式任务队列等等。
    asyncio 往往是构建 IO 密集型和高层级 结构化 网络代码的最佳选择。
async关键字(python3.5以上版本)
    协程函数,定义函数的时候async def 函数名
    协程对象,执行 协程函数() 得到的协程对象
"""
import asyncio

# 示例1:使用装饰器,3.5以上版本不推荐使用----------------------------------------------------------
import aiohttp as aiohttp


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
print('-----------------------')


# 示例2:async的基本使用-------------------------------------------------------------------------
async def func():
    print('协程函数!')
    # await + 可等待的对象(协程对象,Future,Task对象->IO等待)
    await asyncio.sleep(2)  # 耗时的IO操作
    print('结束!')


obj = func()  # 协程对象

# loop = asyncio.get_event_loop()
# loop.run_until_complete(obj)
asyncio.run(obj)  # 等价于上面两条语句

print('-----------------------')


# 示例3:图片下载------------------------------------------------------------------------------
async def download_handle(session, url):
    print('发送请求:' + url)
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()
        file_name = url.rsplit('/')[-1]
        with open(file_name, mode='wb') as file_obj:
            file_obj.write(content)
        print('下载完成')


async def download(url_list):
    async with aiohttp.ClientSession() as session:
        tasks2 = [asyncio.create_task(download_handle(session, url)) for url in url_list]
        await asyncio.wait(tasks2)


url_list = [
    'https://i0.hdslb.com/bfs/album/d1bac1a1d6522afc49cccceb5c28851995b93454.png',
    'https://i0.hdslb.com/bfs/album/a1b5fb1c761c829e3f66cd35b253626ae3950ee0.jpg',
    'https://i0.hdslb.com/bfs/album/b2a50f6f0424f6bc87657219b43c8af574d63d6a.png',
    'https://i0.hdslb.com/bfs/album/f02345fac0d262f7eef8c71bfb873982ad4b90f9.png',
]
asyncio.run(download(url_list))
print('-----------------------')


# 示例4:协程嵌套--------------------------------------------------------------------------------
async def others():
    print('开始!')
    await asyncio.sleep(2)
    print('结束!')
    return '返回值'


async def funq():
    print('执行func2')
    re = await others()
    print('结果为:', re)


asyncio.run(funq())
print('-----------------------')


# 示例5:加入Task对象进入时间循环------------------------------------------------------------------
async def funt():
    print(1)
    await asyncio.sleep(3)
    print(2)
    return 233


async def main():
    print('主线程')

    # 创建Task对象,将当前执行的funt函数任务加入到时间循环中
    task1 = asyncio.create_task(funt())
    print('加入task1')

    # 创建Task对象,将当前执行的funt函数任务加入到时间循环中
    task2 = asyncio.create_task(funt())
    print('加入task2')

    # 等待task任务执行完毕
    re1 = await task1
    re2 = await task2
    print(task1, task2)


asyncio.run(main())
print('-----------------------')


# 示例6:等待多任务结束-------------------------------------------------------------------------
async def funm():
    print(1)
    await asyncio.sleep(3)
    print(2)
    return 666


async def mains():
    print('主线程')

    # 多个task对象放到列表中
    task_list = [
        asyncio.create_task(funm(), name='t1'),
        asyncio.create_task(funm(), name='t2')
    ]

    # 等待所有task任务执行完毕,所有任务执行完毕后会放入done对象里
    done, pending = await asyncio.wait(task_list, timeout=None)  # timeout参数设置等待任务的时间(None为无限)
    print(done)


asyncio.run(mains())
print('-----------------------')

# 示例7:简化示例6-------------------------------------------------------------------------
task_list = [
    funm(),
    funm()
]
# 简化后asyncio会在内部自动创建funm()任务
done, pending = asyncio.run(asyncio.wait(task_list))
print(done)

