import sys
import random
import math
from pathlib import Path


def size(n: int):
    import client.base.config as CONFIG

    return math.floor(n * CONFIG.get("dpiMultiplier", 1))


def resPath(*args: str | Path):
    """如果是打包的exe，获取资源时要去临时目录里拿"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        return Path(sys._MEIPASS) / Path(*args)
    except Exception:
        return Path(*args)
