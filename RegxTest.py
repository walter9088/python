#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re   #第一步，要引入re模块
a = re.findall("匹配规则", "这个字符串是否有匹配规则的字符")   #第二步，调用模块函数
print(a.encode(encoding='UTF-8',errors='strict'))  #以列表形式返回匹配到的字符串