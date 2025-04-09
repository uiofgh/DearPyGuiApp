from client.api import *

gDpgAsync = None


class DearPyGuiAsync:
    _callback_task: asyncio.Task

    def __init__(self, loop=None):
        self.loop = loop

    async def setup(self):
        """
        Special method that runs when starting
        This is helpful for running code that has special setup behavior that may be asynchronous
        """
        pass

    async def teardown(self):
        """
        Special method that runs when shutting down.
        This is helpful for running code that has special shutdown behavior that may be asynchronous
        """
        pass

    async def run_callbacks(self, jobs):
        """
        Run the callbacks that were added
        """
        if jobs is None:
            pass
        else:
            for job in jobs:
                if job[0] is None:
                    pass
                else:
                    sig = dpg.inspect.signature(job[0])
                    args = []
                    for arg in range(len(sig.parameters)):
                        args.append(job[arg + 1])
                    if asyncio.iscoroutinefunction(
                        job[0]
                    ) or asyncio.iscoroutinefunction(job[0].__call__):
                        try:
                            await job[0](*args)
                        except Exception as e:
                            print(e)
                    else:
                        job[0](*args)

    async def callback_loop(self):
        """
        |coro|
        Processes the the callbacks asynchronously
        This will configure the app to manually manage the callbacks so overwrite this if you want to do something else
        """
        dpg.configure_app(manual_callback_management=True)
        while dpg.is_dearpygui_running():
            asyncio.create_task(self.run_callbacks(dpg.get_callback_queue()))
            dpg.render_dearpygui_frame()
            await sleep(0.0095)
        await self.teardown()

    async def start(self):
        """
        |coro|
        For starting the gui in an async context
        Usually to add a gui to another async process
        """
        await self.setup()
        self._callback_task = asyncio.create_task(self.callback_loop())

    async def __start(self):
        await self.setup()
        await self.callback_loop()

    async def stop(self):
        """
        |coro|
        Manually cancel the callback processing task
        """
        self._callback_task.cancel()
        await self.teardown()

    def run(self):
        """
        |blocking|
        Run DearPyGui with async compatibility
        Use this in place of `dpg.start_gui()`

        """
        self.loop.run_until_complete(self.__start())


def setTitle(oldTitle, newTitle):
    if sys.platform != "win32":
        return
    """循环检测窗口是否生成，生成之后修改窗口标题"""
    from ctypes import windll

    while True:
        hwnd = windll.user32.FindWindowW(None, oldTitle)
        if hwnd != 0:
            windll.user32.SetWindowTextW(hwnd, newTitle)
            break


def setFont():
    FONT_PATH = {
        "win32": "C:\Windows\Fonts\msjh.ttc",
        "darwin": "/System/Library/Fonts/STHeiti Medium.ttc",
    }

    system = sys.platform
    fontPath = FONT_PATH[system]
    with dpg.font_registry():
        # 设置中文字体
        with dpg.font(fontPath, 20 * CONFIG.get("dpiMultiplier", 1)) as font:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
            dpg.bind_font(font)


def initViewport(title="", width=100, height=100, primary_window=None):
    setFont()
    from screeninfo import get_monitors

    xPos, yPos = size(1000), size(500)
    for m in get_monitors():
        if m.is_primary:
            xPos = (m.width - width) // 2
            yPos = (m.height - height) // 2
            break

    RANDOM_TITLE = str(random.random())
    dpg.create_viewport(
        title=RANDOM_TITLE,
        min_width=width,
        min_height=height,
        width=height,
        height=height,
        x_pos=xPos,
        y_pos=yPos,
    )
    dpg.setup_dearpygui()
    if primary_window:
        dpg.set_primary_window(primary_window, True)
    dpg.show_viewport()
    threading.Thread(target=setTitle, args=(RANDOM_TITLE, title)).start()


def startEventLoop():
    """
    阻塞启动loop
    """
    global gDpgAsync
    gDpgAsync = DearPyGuiAsync(gEventLoop)
    gDpgAsync.run()
    dpg.destroy_context()


def exit():
    dpg.stop_dearpygui()
