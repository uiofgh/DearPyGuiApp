import asyncio
import time
import inspect

gEventLoop = asyncio.get_event_loop()


async def sleep(seconds: float):
    """An asyncio sleep.

    On Windows this achieves a better granularity than asyncio.sleep

    Args:
        seconds (float): Seconds to sleep for.

    """
    await gEventLoop.run_in_executor(None, time.sleep, seconds)


def asyncCallback(method):
    def decorator(*args):
        arg_slice = args[: len(inspect.signature(method).parameters)]
        asyncio.run_coroutine_threadsafe(method(*arg_slice), gEventLoop)

    return decorator
