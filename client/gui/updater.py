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
            dpg.add_button(label="Save", callback=self.onClick)
            self.descTxt = dpg.add_text(L("checking_update"))
            with dpg.item_handler_registry(tag="widget handler"):
                dpg.add_item_clicked_handler(callback=self.onClick)
            dpg.bind_item_handler_registry(self.descTxt, "widget handler")

    async def onClick(self):
        ret = await self.call("xy3.update.check_update")
        print(ret)


def main():
    updaterWindow = UpdaterWindow()
    dpgStartAsync(L("update_window_title"), WIDTH, HEIGHT, updaterWindow.window)
