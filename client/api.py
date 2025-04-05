import fileinput
import os
import re
import sys
from pathlib import Path

import dearpygui.dearpygui as dpg

import client.base.config as CONFIG
import client.base.util as UTIL
import common.common_const as COMMON_CONST
import common.util as COMMON_UTIL
from client.base.async_dpg import dpgStartAsync, asyncCallback, dpgStop
from client.base.extend import *
from client.base.lang import L
from client.base.macro import *
from client.base.network import ClientComponent
