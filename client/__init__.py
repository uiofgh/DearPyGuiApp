from client.api import *

FONT_PATH = {
    "win32": "C:\Windows\Fonts\msjh.ttc",
    "darwin": "/System/Library/Fonts/STHeiti Medium.ttc",
}

dpg.create_context()

system = sys.platform
fontPath = FONT_PATH[system]
with dpg.font_registry():
    # 设置中文字体
    with dpg.font(
        fontPath, 20 * CONFIG.get("dpiMultiplier", 1)
    ) as font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
        dpg.bind_font(font)
