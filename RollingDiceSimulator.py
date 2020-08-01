#!/usr/bin/python

flag = 'y'

while(flag is 'y'): 

	import random
	i = random.randrange(1,7)

	print "The number rolled on the dice is : ",i

	print "Do you want to roll again? (y/n) : "

	f = raw_input()

	flag = str(f)



