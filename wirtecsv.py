#-*- coding: UTF-8 -*-  2.7版本对中文的要求
import csv

with open( './text.csv', 'wb') as f:
	writer = csv.writer(f)
	data = '哈哈'
	writer.writerows(data)

f.close()
