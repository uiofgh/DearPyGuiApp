import sys
import random
from pathlib import Path


def size(n: int):
    import client.base.config as CONFIG

    return n * CONFIG.get("dpiMultiplier", 1)


def resPath(*args: str | Path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        return Path(sys._MEIPASS) / Path(*args)
    except Exception:
        return Path(*args)
