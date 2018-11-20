#!/usr/bin/python
#-*- coding: utf-8 -*-

from snownlp import SnowNLP

s = SnowNLP(u'我操你大爷的')

print (s.words)
print (s.tags)

