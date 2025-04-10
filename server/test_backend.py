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
from autobahn.wamp.types import CallResult

from common.util import startComponent


class MyApplicationSession(ApplicationSession):
    """
    Application component that provides procedures which
    return complex results.
    """

    async def onJoin(self, details):

        def add_complex(a, ai, b, bi):
            return CallResult(c=a + b, ci=ai + bi)

        await self.register(add_complex, "com.myapp.add_complex")

        def split_name(fullname):
            forename, surname = fullname.split()
            return CallResult(forename, surname)

        await self.register(split_name, "com.myapp.split_name")


if __name__ == "__main__":
    startComponent(MyApplicationSession)
