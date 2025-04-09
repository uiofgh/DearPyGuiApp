from autobahn.asyncio.component import Component, run
from autobahn.asyncio.wamp import ApplicationSession
from autobahn.wamp.types import CallResult

import common.common_const as COMMON_CONST
from client.base.dispatcher import Dispatcher


class ClientSession(ApplicationSession, Dispatcher):
    def __init__(self, config):
        super().__init__(config)

    async def onJoin(self, details):
        gNetMgr.dispatchMsg("connectServer")

    def onDisconnect(self):
        gNetMgr.dispatchMsg("disconnectServer")


class NetMgr(Dispatcher):
    def __init__(self):
        super().__init__()
        self.session: ClientSession = None
        self.component: Component = None

    def connect(self):
        if self.session:
            return
        comp = Component(
            session_factory=self.createSession,
            realm=COMMON_CONST.CROSSBAR_REALM,
            transports={"url": COMMON_CONST.WAMP_URL, "serializers": ["json"]},
        )
        self.component = comp
        run([comp], start_loop=False)

    def createSession(self, config):
        self.session = ClientSession(config)
        return self.session

    def disconnect(self):
        if self.session:
            self.session.leave()


class ClientComponent(Dispatcher):
    def __init__(self):
        super().__init__()
        self.listenMsg(gNetMgr, "connectServer", self.onServerConnect)
        self.listenMsg(gNetMgr, "disconnectServer", self.onServerDisconnect)

    def onServerConnect(self):
        pass

    def onServerDisconnect(self):
        pass


gNetMgr = NetMgr()


def connectServer():
    gNetMgr.connect()


def disconnectServer():
    gNetMgr.disconnect()


async def callServer(func: str, *args, **kwargs) -> CallResult:
    try:
        ret = await gNetMgr.session.call(func, *args, **kwargs)
        return ret
    except Exception as e:
        print(e)
