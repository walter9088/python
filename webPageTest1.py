#!/usr/bin/python
#-*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import re
from transfer2num import getResultForDigit
from transfer2date import getDigitDate



url = "http://www.jxsggzy.cn/web/jyxx/002006/002006001/20180203/0b08ab2f-5e46-4e74-8718-7c0d5a8358e5.html"

content = urllib2.urlopen(url)

soup = BeautifulSoup(content)

tags = soup.select("div.article-info")

lists = []
for tag in tags:
    lines = tag.text.splitlines()

    for line in lines:

            strip_line = line.strip()
            if strip_line != u"":
                lists.append(strip_line.strip())

str_convert = '\n'.join(lists)

print str_convert


str_convert = u'1、招标编号： JXFZ2017-C021-2'

pattern = re.compile(ur'(?:[\[（(【])?(?:项目|招标|采购)编号[:：]?[ ]*.{6,}(?:[\]）)】]|\w)$')
match = re.findall(pattern,str_convert)
m = ','.join(match)
print m


##招标项目编号
pattern = re.compile(ur'[\[（(【](?:项目|招标)编号 [:：]?[\w]{11,}[\]）)】]')
match = re.findall(pattern,str_convert)
m = ','.join(match)
print m

##招标代理机构
pattern = re.compile(ur'招标代理(?:机构|单位)[:：]?[\W]{6,}[司]')
match = re.findall(pattern,str_convert)
m1 = ','.join(match)
print m1

##招标代理机构
pattern = re.compile(ur'采购(?:人|单位)[:：]?[\W]{6,}[司局]')
match = re.findall(pattern,str_convert)
m1 = ','.join(match)
print m1



##开标时间
#开标时间为2018年2月26日下午14:00时
##投标截止时间和开标时间为2018年2月26日下午14:00时（北京时间）。届时请投标人的法定代表人或经正式授权的代表携带CA数字证书出席开标大会,签到时间以递交CA数字证书时间为准
#投标截止时间为2018年2月26日下午14:00时（北京时间）。届时请投标人的法定代表人或经正式授权的代表携带CA数字证书出席开标大会,签到时间以递交CA数字证书时间为准

pattern = re.compile(ur'(?:投标截止|开标)时间[为]?[:：]?\d{,4}[年-]\d{,2}(?:月|-)\d{,2}(?:日|-)(?:上午|下午)?\d{,2}(?:时|-|:)\d{,2}时')
match = re.findall(pattern,str_convert)
m1 = ','.join(match)
print m1



pattern = re.compile(ur'[\[]\W{,2}[市县](?:本级|市级)[\]]')
match = re.findall(pattern,str_convert)
m1 = ','.join(match)
print m1



