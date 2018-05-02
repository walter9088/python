# -*- coding: UTF-8 -*-
import xlrd
import codecs

data = xlrd.open_workbook("test.xlsx")

table = data.sheets()[0]

lists = []

for i in range(0,5271):
    str = ""
    for n in range(1,4):

        v_cell = table.cell(i,n).value

        if v_cell != "":
            if str !="":
                str = str +" "+v_cell+"\n"
            else:
                str = str+v_cell


    lists.append(str)

f=codecs.open('zhaobiao','w', 'UTF-8')
for list in lists:
    f.write(list)

f.close()

