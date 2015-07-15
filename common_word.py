
############################################ Get the highest message sender ############################################
# read input text file
# pick lines starting with 'From '
# second word in that line is the sender email address
# create a dict with key: sender & value: count of messages
# Loop through the dict and find the highest message sender "Largest count number"

# Get file in
name = raw_input("Enter file:")

# Default input file
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

for lines in handle:
	# ignore blank lines
	if lines.strip():
		words = lines.split()
		# get lines starting with 'From '
		if words[0] == 'From':
			# get all senders words[1]
			# print words[1]

			# create empty dict
			sender_count = dict()
			sender = words[1]

			# if sender isn't in sender_count add him and his count
			sender_count[sender] = sender_count.get(sender, 0) + 1

print sender_count
