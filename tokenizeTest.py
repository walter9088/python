#!/usr/bin/python
#-*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
url="http://www.jxsggzy.cn/web/jyxx/002004/002004004/20171130/926e6b9b-17e6-4dbc-8f91-53076c4422a3.html"
content=urllib2.urlopen(url)
soup=BeautifulSoup(content)

print soup
