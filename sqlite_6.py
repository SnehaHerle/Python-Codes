#!/usr/bin/python
# -*- coding: utf-8 -*-
# creates andin memory table Friends.


import sqlite3 as lite
import sys

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()    
    cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")
        
    lid = cur.lastrowid
    print "The last Id of the inserted row is %d" % lid

