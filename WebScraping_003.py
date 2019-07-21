#!/usr/bin/env PYTHONIOENCODING=UTF-8 python3
# -*- coding: utf-8 -*-
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests as reqs

response = reqs.get('https://www.google.com/')
print(response.status_code)     # To print http response code
print(response.text)            # To print formatted JSON response
