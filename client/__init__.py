from client.api import *

dpg.create_context()

with dpg.font_registry():
    # 设置中文字体
    with dpg.font(
        "C:\Windows\Fonts\msjh.ttc", 20 * CONFIG.get("dpiMultiplier", 1)
    ) as font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
        dpg.bind_font(font)
