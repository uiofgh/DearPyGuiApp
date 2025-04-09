from server.api import *


class PatchService(ApplicationSession):
    async def onJoin(self, details):

        def checkLatest(clientVer):
            latestVer = "123"
            if clientVer == latestVer:
                return CallResult(needPatch=False)
            return CallResult(needPatch=True, latestVer=latestVer)

        await self.register(checkLatest, "xy3.patch.checkLatest")
