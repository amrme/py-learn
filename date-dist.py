"""
Project: mail frequency counter/Histogram
Author: Amr M
Date: Aug 8 2015
"""

# get file
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

# loop through it 
for line in handle:
	# find relevant line: starting with 'From '
	words = line.split()
	if words:
		if words[0] == 'From':
			# print words[0]
			time = words[5].partition(':')
			hour = time[0]
			print hour