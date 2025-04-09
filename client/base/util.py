def getPatchVer():
    from client.api import SAVE

    return SAVE.get("patchVer", "")
