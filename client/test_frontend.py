###############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) typedef int GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
###############################################################################

import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from autobahn.asyncio.component import Component, run
from autobahn.asyncio.wamp import ApplicationSession

from common.util import startComponent


class MyApplicationSession(ApplicationSession):
    """
    Application component that calls procedures which
    produce complex results and showing how to access those.
    """

    async def onJoin(self, details):

        res = await self.call("com.myapp.add_complex", 2, 3, 4, 5)
        print("Result: {} + {}i".format(res.kwresults["c"], res.kwresults["ci"]))

        res = await self.call("com.myapp.split_name", "Homer Simpson")
        print("Forname: {}, Surname: {}".format(res.results[0], res.results[1]))

        self.leave()

    def onDisconnect(self):
        asyncio.get_event_loop().stop()


if __name__ == "__main__":
    startComponent(MyApplicationSession)
