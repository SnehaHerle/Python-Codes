#! /usr/bin/python

import	os
import	time

source = ['/home/sneha/Pictures/Wallpapers/2.jpg','/home/sneha/Pictures/Wallpapers/3.jpg']

target_dir = '/home/sneha/backup'

if not os.path.exists(target_dir):
	os.mkdir(target_dir)		

today =	target_dir + os.sep + time.strftime('%Y%m%d')
print today

now = time.strftime('%H%M%S')
print now

target	= today	+ os.sep + now	+ '.zip'

if not os.path.exists(today):
	os.mkdir(today)
	print('Successfully created directory',	today)

zip_command = "zip -r {0} {1}".format(target, " ".join(source))

print("Zip command is:")
print(zip_command)
print("Running:")
if os.system(zip_command) == 0:
	print('Successful backup to', target)
else:
	print('Backup FAILED')