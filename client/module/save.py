import toml

SAVE_PATH = "save.toml"


class Save:
    def __init__(self):
        try:
            self.data = toml.load(SAVE_PATH)
        except:
            self.data = {}

    def get(self, key: str, default: any):
        return self.data.get(key, default)

    def set(self, key: str, value: any):
        self.data[key] = value
        toml.dump(self.data, SAVE_PATH)


gSave = Save()


def get(key: str, default: any = None):
    return gSave.get(key, default)


def set(key: str, value: any):
    return gSave.set(key, value)
