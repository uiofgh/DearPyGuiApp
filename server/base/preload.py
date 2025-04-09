from server.api import *
from autobahn.asyncio.component import Component, run


def createComponent(sessionFactory):
    comp = Component(
        session_factory=sessionFactory,
        realm=COMMON_CONST.CROSSBAR_REALM,
        transports={"url": COMMON_CONST.WAMP_URL, "serializers": ["json"]},
    )
    return comp


def startup():
    components = []

    components.append(createComponent(PATCH.PatchService))

    run(components)
