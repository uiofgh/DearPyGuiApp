import types

# -*- coding: utf-8 -*-
listenData = {}


def _listenMsg(listener, dispatcher, msg, func):
    assert type(func) == types.FunctionType or type(func) == types.MethodType
    global listenData
    if not dispatcher in listenData:
        listenData[dispatcher] = {}

    if not listener in listenData[dispatcher]:
        listenData[dispatcher][listener] = {}

    if isinstance(msg, (tuple, list)):
        for _msg in msg:
            listenData[dispatcher][listener][_msg] = func
    elif isinstance(msg, str):
        listenData[dispatcher][listener][msg] = func
    else:
        assert None, "invalid msg %s" % msg


def _unListenMsg(listener, dispatcher, msg):
    if dispatcher:
        if dispatcher in listenData:
            if not msg:
                listenData[dispatcher].pop(listener, None)
            elif listener in listenData[dispatcher]:
                if isinstance(msg, (tuple, list)):
                    for _msg in msg:
                        listenData[dispatcher][listener].pop(_msg, None)
                elif isinstance(msg, str):
                    listenData[dispatcher][listener].pop(msg, None)
    else:
        for _dispatcher, _listenDict in listenData.items():
            if not msg:
                _listenDict.pop(listener, None)
            elif listener in _listenDict:
                if isinstance(msg, (tuple, list)):
                    for _msg in msg:
                        _listenDict[listener].pop(_msg, None)
                elif isinstance(msg, str):
                    _listenDict[listener].pop(msg, None)


def _unDispatchMsg(dispatcher):
    listenData.pop(dispatcher, None)


def _dispatchMsg(dispatcher, msg, *arg):
    global listenData
    dispatcherData = listenData.get(dispatcher)
    if not dispatcherData:
        return
    for _listener, _msgDict in dispatcherData.items():
        if _listener in dispatcherData:
            if msg in _msgDict:
                func = _msgDict[msg]
                if not func:
                    continue
                if type(func) == types.FunctionType:
                    func.msg = msg
                try:
                    func(*arg)
                except:
                    import sys

                    sys.excepthook(*sys.exc_info())


def update():
    global listenData

    for dispatcher, listeners in listenData.items():
        for listener, msgDict in listeners.items():
            newDict = {}
            for msg, func in msgDict.items():
                newFunc = getattr(listener, func.__name__, None)
                if newFunc:
                    newDict[msg] = newFunc

            listenData[dispatcher][listener] = newDict


# --------------------------------
# dispatch 方法类
# --------------------------------
class Dispatcher(object):
    __slots__ = ()

    def listenMsg(self, dispatcher, msg, func):
        _listenMsg(self, dispatcher, msg, func)

    def unListenMsg(self, dispatcher=None, msg=None):
        _unListenMsg(self, dispatcher, msg)

    def dispatchMsg(self, msg, *arg):
        _dispatchMsg(self, msg, *arg)

    def release(self):
        _unDispatchMsg(self)
        self.unListenMsg()
