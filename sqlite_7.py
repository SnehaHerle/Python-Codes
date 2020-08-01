#!/usr/bin/python
# -*- coding: utf-8 -*-
# Writing the output into .txt and .csv files.


import sqlite3 as lite
import sys
import csv

con = lite.connect('test.db')

with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM Cars")

    rows = cur.fetchall()

    for row in rows:
        print row

    with open('test.txt', 'w') as f:
    	for row in rows:
        	print row
        	f.write("%s\n" % str(row))
	
    with open('output.csv', 'wb') as f:
    	writer = csv.writer(f)
    	writer.writerow(['Column 1', 'Column 2', 'Column 3'])
    	writer.writerows(rows)

