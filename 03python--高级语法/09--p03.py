# asyncio--01

import threading
import asyncio
# 使用协程
#@asyncio.coroutine 使用async替换
async def hello():
    print("Hello world (%s)" % threading.currentThread())
    print("Start (%s)" % threading.currentThread())
    #yield from asyncio.sleep(5)
    await asyncio.sleep(5)
    print("Done (%s)" % threading.currentThread())
    print("Hello again (%s)" %threading.currentThread())
# 启动消息循环
loop = asyncio.get_event_loop()
# 定义任务
tasks = [hello(), hello()]
# asyncio使用wait等待tasks执行完毕
loop.run_until_complete(asyncio.wait(tasks))
# 关闭消息循环
loop.close()

