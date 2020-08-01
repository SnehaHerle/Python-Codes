#!/usr/bin/python

import csv
import json

csvfile = open('/home/sneha/Downloads/C2ImportGroupsSample.csv', 'r')
jsonfile = open('/home/sneha/Downloads/C2ImportGroupsSample.json', 'w')

fieldnames = ("GroupName","Groupcode","GroupOwner","GroupCategoryID")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')


with open('/home/sneha/Downloads/C2ImportGroupsSample.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
            print(row[0])
            line_count += 1
 
