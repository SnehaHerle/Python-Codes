#!/usr/bin/python

import sys

def wc_function():
	num_lines = 0
	num_words = 0
	num_chars = 0
	line_length = []
	with open(fname, 'r') as f:
		for line in f:
			words = line.split()
			num_lines += 1
			num_words += len(words)
			num_chars += len(line)
			if(option == '-L'):
				line_length.append(len(line))

	if(option == 0):
		print " ",num_lines, "",num_words ,num_chars , sys.argv[1]
	elif(option == '-c'):
		print num_chars , sys.argv[2]
	elif(option == '-l'):
		print num_lines,sys.argv[2]
	elif(option == '-w'):
		print num_words, sys.argv[2]
	elif(option == '-L'):
		print max(line_length)-1 , sys.argv[2]
	return


if(len(sys.argv) == 2):
	fname = sys.argv[1]
	option = 0
elif(len(sys.argv)== 3):
	option = sys.argv[1]
	fname = sys.argv[2]

wc_function()



