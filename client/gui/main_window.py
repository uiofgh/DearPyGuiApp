from client.api import *

WIDTH = size(600)
HEIGHT = size(200)


def main():
    dpg.create_context()
    with dpg.window(tag="Primary Window"):
        dpg.add_text("Hello, world")
        dpg.add_button(label="Save")
        dpg.add_input_text(label="string", default_value="Quick brown fox")
        dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

    UI.initViewport(L("main_window_title"), WIDTH, HEIGHT, "Primary Window")
    connectServer()

    UI.startEventLoop()

    disconnectServer()
    gEventLoop.stop()
