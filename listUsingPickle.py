#! /usr/bin/python

"""
Python provides a standard module called pickle	using which you can store any plain Python object in a file and then get it back later. This is called storing the object persistently. Useful as you can get back to the previous state of object by loading it when you start your python shell again.
"""

import	pickle

# The name of the file where we	will store the object

shoplistfile = 'shoplist.data'

# The list of things to	buy

arr = raw_input("Enter the items separated by a space : ").split()

shoplist = []

for i in arr:
	shoplist.append(i)

# Write	to the file

f = open(shoplistfile,	'wb')

# Dump the object to a file

pickle.dump(shoplist,f)

f.close()

# Destroy the shoplist variable

del shoplist

#Read back from	the storage

f = open(shoplistfile, 'rb')

# Load the object from the file

storedlist = pickle.load(f)

print(storedlist)

