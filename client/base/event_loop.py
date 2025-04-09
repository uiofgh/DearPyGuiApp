import asyncio
import time
import inspect
from concurrent.futures import Future
from client.base.log import error

gEventLoop = asyncio.get_event_loop()


async def sleep(seconds: float):
    """An asyncio sleep.

    On Windows this achieves a better granularity than asyncio.sleep

    Args:
        seconds (float): Seconds to sleep for.

    """
    await gEventLoop.run_in_executor(None, time.sleep, seconds)


def onTaskFinish(task: Future):
    if not task.exception():
        return
    error(task.exception())


def asyncCallback(method):
    """用于从其他线程回调到主线程中，比如dpg的回调"""

    def decorator(*args):
        arg_slice = args[: len(inspect.signature(method).parameters)]
        task = asyncio.run_coroutine_threadsafe(method(*arg_slice), gEventLoop)
        task.add_done_callback(onTaskFinish)

    return decorator
