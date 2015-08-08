"""
Project: mail frequency counter/Histogram
Author: Amr M
Date: Aug 8 2015
"""

# get file
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

# empty dict to keep track of (hour, count)
count = {}

# loop through it 
for line in handle:
	# find relevant line: starting with 'From '
	words = line.split()
	if words:
		if words[0] == 'From':
			# print words[0]
			time = words[5].partition(':')
			hour = time[0]
			# print hour
			# get the count 
			count[hour] = 1 + count.get(hour, 0)

sorted_count = count.items()
sorted_count.sort()
print sorted_count

# loop and print all the hour, count pairs
# for hours, counts in count.items().sort():
# 	print hours, counts