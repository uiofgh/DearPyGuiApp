import toml

CONFIG_PATH = "config.toml"


class Config:
    def __init__(self):
        try:
            self.data = toml.load(CONFIG_PATH)
        except:
            self.data = {}

    def get(self, key: str, default: any):
        return self.data.get(key, default)

    def set(self, key: str, value: any):
        self.data[key] = value
        toml.dump(self.data, CONFIG_PATH)


gConfig = Config()


def get(key: str, default: any = None):
    return gConfig.get(key, default)


def set(key: str, value: any):
    return gConfig.set(key, value)
