#!/usr/bin/env PYTHONIOENCODING=UTF-8 python
# -*- coding: utf-8 -*-

import platform
import socket
import pytz  # $ pip install pytz
from datetime import datetime

res = {}
if not res:
    print('res is empty')
print(res)

print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

class Banners():
    def __init__(self, ip):
        self.ip = ip

    def getBanner(self):
        return 'bana'

banners = Banners('ip')
banner = banners.getBanner()
print(banner)
