import asyncio

from autobahn.asyncio.component import Component, run
from autobahn.asyncio.wamp import ApplicationSession

import common.common_const as COMMON_CONST


class ClientSession(ApplicationSession):
    def __init__(self, config):
        super().__init__(config)

    async def onJoin(self, details):
        pass

    def onDisconnect(self):
        pass


class ClientComponent:
    session: ClientSession = None
    component: Component = None

    def __init__(self):
        if not self.session:
            self.initSession()

    def initSession(self):
        comp = Component(
            session_factory=self.createSession,
            realm=COMMON_CONST.CROSSBAR_REALM,
            transports={"url": COMMON_CONST.WAMP_URL, "serializers": ["json"]},
        )
        run([comp], start_loop=False)
        self.component = comp

    def createSession(self, config):
        self.session = ClientSession(config)
        return self.session

    async def call(self, func: str, *args, **kwargs):
        try:
            ret = await self.session.call(func, *args, **kwargs)
            return ret
        except Exception as e:
            print(e)
