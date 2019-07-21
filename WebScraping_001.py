#!/usr/bin/env PYTHONIOENCODING=UTF-8 python3
# -*- coding: utf-8 -*-
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re

page = 1
target_url = 'https://www.jobplanet.co.kr/companies?industry_id=701&page='
temp_req = Request(target_url, headers={'User-Agent': 'Mozilla/5.0'})
temp_html = urlopen(temp_req).read()
temp_soup = BeautifulSoup(temp_html, 'html5lib')
temp_last_page = temp_soup.find(class_='btn_pglast').get('href')
last_page = re.search('&page=(.*)', temp_last_page).group(1)

no = 0
for i in range(int(last_page)):
    req = Request(target_url + str(page + i), headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req, timeout=100).read()
    soup = BeautifulSoup(html, 'html5lib')
    companies = soup.find(class_='list_companies')

    for company in companies.find_all(class_='company'):
        no = no + 1
        c_no = str(no)
        c_name = company.find(class_='us_titb_l3').find('a')
        c_locate = company.find_all(class_='us_stxt_1')[1]
        c_value = company.find(class_='gfvalue')
        c_notranslate = company.find(class_='notranslate')

        detail_req = Request('https://www.jobplanet.co.kr' + c_name.get('href'), headers={'User-Agent': 'Mozilla/5.0'})
        detail_html = urlopen(detail_req).read()
        detail_soup = BeautifulSoup(detail_html, 'html5lib')
        c_url_el = detail_soup.find(class_='link_to')
        c_url = ''
        if c_url_el is not None:
            c_url = c_url_el.get('href')

        print(c_no + '\t' + c_name.get_text() + '\t' + c_locate.get_text() + '\t' + c_value.get_text() + '\t' + c_notranslate.get_text() + '\t' + c_url)
