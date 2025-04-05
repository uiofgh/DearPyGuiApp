from autobahn.asyncio.component import Component, run

import common.common_const as COMMON_CONST


def startComponent(ApplicationSession):
    comp = Component(
        session_factory=ApplicationSession,
        realm=COMMON_CONST.CROSSBAR_REALM,
        transports={"url": COMMON_CONST.WAMP_URL, "serializers": ["json"]},
    )
    run([comp])
