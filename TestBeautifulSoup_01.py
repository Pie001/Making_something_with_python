#!/usr/bin/env PYTHONIOENCODING=UTF-8 python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

txt = """<p>I have a dog.  His name is <span class="secret">Ken</span>.</p>"""
soup = BeautifulSoup(txt, "html5lib")
soup.get_text()
print(soup)

# remove an element by tag matching
soup.find("span", {"class":"secret"}).extract()
soup.get_text()
#: u'I have a dog.  His name is .'


# or you can replace that with something
soup = BeautifulSoup(txt, "html5lib")
soup.find("span", {"class":"secret"}).replace_with("confidential")
soup.get_text()
#: u'I have a dog.  His name is confidential.'
