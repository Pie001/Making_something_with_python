#!/usr/bin/env PYTHONIOENCODING=UTF-8 python
# -*- coding: utf-8 -*-

import platform
import socket
from datetime import datetime, timedelta
import pytz  # $ pip install pytz

utc_offset = timedelta(hours=9, minutes=0)  # +5:30
now = datetime.now(pytz.utc)  # current time
print({tz.zone for tz in map(pytz.timezone, pytz.all_timezones_set)
       if now.astimezone(tz).utcoffset() == utc_offset})

print(platform.python_version())
print(socket.gethostbyname(socket.gethostname()))



#現在の日付と日時
#now_datetime = datetime.datetime.now()
#print(now_datetime)
