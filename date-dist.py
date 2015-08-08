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
	print line