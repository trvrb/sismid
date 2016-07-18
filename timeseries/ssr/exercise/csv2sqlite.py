#!/usr/bin/env python

import os
import sys
import csv
import json
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

def dbExecute(c, sqlCmd, args=None):
# 	print(sqlCmd)
	if args is not None:
# 		print(args)
		c.execute(sqlCmd, args)
	else:
		c.execute(sqlCmd)

if __name__ == '__main__':
	if len(sys.argv) < 4:
		print('Usage: {0} <csv-input-filename> <sqlite-output-filename> <sqlite-table-name>'.format(__file__))
	
	csvFilename = sys.argv[1]
	dbFilename = sys.argv[2]
	tableName = sys.argv[3]
	
	with open(csvFilename, 'rU') as csvFile:
		cr = csv.reader(csvFile)
		colNames = cr.next()
		
		with sqlite3.connect(dbFilename) as db:
			c = db.cursor()
			
			createCmd = 'CREATE TABLE {0} ({1})'.format(tableName, ', '.join(colNames))
			dbExecute(c, createCmd)
			
			for row in cr:
				insertCmd = 'INSERT INTO {0} VALUES ({1})'.format(
					tableName, ','.join(['?'] * len(row))
				)
				dbExecute(c, insertCmd, [None if x == '' else x for x in row])
