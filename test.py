#!/usr/bin/python
#-*- coding: utf-8 -*-

str =raw_input('birth:')
if isinstance(str,int):
	age=int(str)
else:
	age=15
xxx=20
if age>xxx:
	print 'your arge >%s is %d' % (xxx,age);
elif age==xxx:
	print 'you'
else:
	print 'your age is< ',age


#for

name=['name1','bo']
for x in name:
	print x

for x in xrange(10):
	print x


def muPro(x,y=20):
	return x,y,x+y

print muPro(12,23)
print muPro(60)

def my_abs(x):
	if x>=0:
		return x
	else:
		return -x


print 'this is abs test:%s' % my_abs(age)

if __name__ == '__main__':
	x = my_abs(-34)
	print x
