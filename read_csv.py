#!/usr/bin/env python
#coding:utf8
import os
import csv
csvPath = os.path.expanduser("./test.csv")
with open(csvPath) as csvFile:
	csvReader = csv.reader(csvFile, delimiter=',')
	for row in csvReader:
		print(row)

