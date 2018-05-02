#!/usr/bin/python
#-*- coding: utf-8 -*-
import urllib2
import xlrd
import jieba
from bs4 import BeautifulSoup

data = xlrd.open_workbook('test.xls')



table = data.sheets()[0]
table = data.sheet_by_index(0)
table = data.sheet_by_name(u'Sheet1')


nrows = table.nrows
ncols = table.ncols

for i in range(nrows):
    cell_v1 = table.cell(i, 5).value
    print cell_v1