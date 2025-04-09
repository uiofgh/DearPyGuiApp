from client.api import *

WIDTH = size(250)
HEIGHT = size(150)


class UpdaterWindow(ClientComponent):
    def __init__(self):
        super().__init__()
        self.window = dpg.generate_uuid()
        with dpg.window(
            tag=self.window,
            pos=(0, 0),
            width=WIDTH,
            height=HEIGHT,
        ):
            self.descTxt = dpg.add_text(L("checking_patch"))
            dpg.add_button(label="Save", callback=self.onClick)
            with dpg.item_handler_registry(tag="widget handler"):
                dpg.add_item_clicked_handler(callback=self.onClick)
            dpg.bind_item_handler_registry(self.descTxt, "widget handler")

    @asyncCallback
    async def onClick(self):
        ret = await callServer("xy3.patch.checkLatest", UTIL.getPatchVer())
        print(ret)

    @asyncCallback
    async def onServerConnect(self):
        ret = await callServer("xy3.patch.checkLatest", UTIL.getPatchVer())
        if not ret.kwresults.get("needPatch"):
            log("no patch")
            return
        log("start patch")


def main():
    dpg.create_context()
    updaterWindow = UpdaterWindow()
    UI.initViewport(L("update_window_title"), WIDTH, HEIGHT, updaterWindow.window)
    connectServer()

    UI.startEventLoop()

    disconnectServer()
    gEventLoop.stop()
