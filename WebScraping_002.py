#!/usr/bin/env PYTHONIOENCODING=UTF-8 python3
# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen("https://www.yahoo.co.jp/").read()
soup = BeautifulSoup(html, 'html5lib')
a = soup.find_all("a")
print(a)
