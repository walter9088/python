#!/usr/bin/python
#-*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import re
from transfer2num import getResultForDigit
from transfer2date import getDigitDate


pattern2 = re.compile(ur'项目名称[^\n|\s]*[:：]{1}[\S]*')#项目采购名称 项目名称[^\n|\s]*[:：]{1}[\S]*
pattern3 = re.compile(ur'[零壹贰叁肆伍陆柒捌玖拾佰仟万亿元圆角]{1,20}[分整]?')#采购金额 中标.*?[零壹贰叁肆伍陆柒捌玖拾佰仟万亿元圆角]{1,20}[分整]?
pattern32 =re.compile(r'\d{0,3}[,，]?\d{0,3}[,，]?\d{0,3}[,，]?\d{1,3}\W?\d{0,3}\W{0,3}元')  #采购金额不是大写中文
pattern4 = re.compile(ur'联.{0,3}系.{0,3}人.{0,30}\W.{0,20}电.{0,3}话.{0,6}?\W*?\d{4}.\d{6,7}') #采购联系人

pattern5 = re.compile(ur'.{0,4}年.{1,3}月.{1,4}日') #日期


pattern8 = re.compile(ur'中标.{0,5}[:：]{1}.{1,16}[厂司处所局院校站坊部]') #中标供应商名称
# 中标[^\n]\W{0,5}名称[:：]{1}(.*)[厂司处所局厅院校站]
pattern9 = re.compile(ur'中标.{1,5}地址[:：]{1}.*?[号层室厂部栋厦]{1}|中标.{1,5}地址[:：]{1}.*?[\S]*') #中标供应商地址
pattern10 = re.compile(ur'[（(]{1}[A-Z][\w\d]{1,8}.[\w\d]{1,2}.\d{1,5}.[A-Z]{1,5}[）)]{1}|[（(]{1}[A-Z][\w\d]{2,15}.\d{3}[）)]{1}')#去除名称里面的编号
pattern11 = re.compile(ur'中标.{0,5}地址[:：]{1}.*') #去除中标供应商里面的地址
pattern12 =re.compile(ur'招\W{0,3}标{0,3}人\W*[局校司所院厂学心队会处站室]{1}') #采购人特殊情况，写了招标人
pattern13 =re.compile(ur'采购项目名称(.*?)\n')        #去除采购人名称里面的采购项目名称

pattern14 = re.compile(ur'#及电话\W{1,3}[\S]|#\W{1,3}[\S]') #采购联系人
pattern15 =re.compile(ur'\d{4}.\d{6,7}')#联系人电话或者传真

pattern_if1 = re.compile(ur'中标.{0,4}公告如下.{1}|中标.{0,5}信息.{1}')



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

##招标项目编号
pattern = re.compile(ur'[\[（(【](?:项目|招标)编号[:：]?[\w]{11,}[\]）)】]')
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
pattern = re.compile(ur'开标时间[为]?[:：]?\d{,4}(?:年|-)\d{,2}(?:月|-)\d{,2}(?:日|-)(?:上午|下午)?\d{,2}(?:时|-|:)\d{,2}时')
match = re.findall(pattern,str_convert)
m1 = ','.join(match)
print m1



