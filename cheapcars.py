#!/usr/bin/python
# -*- coding: utf-8 -*-
# Creates a table Cars, finds cheap cars out of it and writes it into a text file. 

import sqlite3 as lite
import sys
import csv

cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)


con = lite.connect('test.db')

with con:
    
    cur = con.cursor()    
    
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)

    cur.execute("SELECT * FROM Cars WHERE Price < 30000")

    rows = cur.fetchall()

    for row in rows:
        print row

    with open('cheapcars.txt', 'w') as f:
    	for row in rows:
        	f.write("%s\n" % str(row))
	
    with open('cheapcars.csv', 'wb') as f:
    	writer = csv.writer(f)
    	writer.writerow(['Id', 'Name', 'Price'])
    	writer.writerows(rows)

