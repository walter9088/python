# -*- coding: UTF-8 -*-
import xlrd
import codecs
import jieba

from gen import word2vec
data = xlrd.open_workbook("jy.xlsx")

table = data.sheets()[0]

lists = []

f=codecs.open('qyvector','w', 'UTF-8')

for i in range(0,9999):
    v_cell = table.cell(i,1).value

    if v_cell ==0.0 or v_cell == 'null':
        continue
    seglist = jieba.cut(v_cell, cut_all=False)  # 精确模式

    output = ' '.join(list(seglist))
    f.write(output)

word2vec.word2vec()
word2vec.word2vec('qyvector', 'wordVec.bin')





