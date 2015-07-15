
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

# create empty dict
sender_count = dict()

for lines in handle:
	# ignore blank lines
	if lines.strip():
		words = lines.split()
		# get lines starting with 'From '
		if words[0] == 'From':
			# get all senders words[1]
			# print words[1]
			sender = words[1]

			# if sender isn't in sender_count add him and his count
			sender_count[sender] = sender_count.get(sender, 0) + 1

# Now we have the total dictionalry of the sender count pairs
# print sender_count

max_mail = None
max_count = None
# Loop through the dict and find the max count then print the pair
for mail, ct in sender_count.items():
	if max_count == None or ct > max_count:
		max_mail = mail
		max_count = ct


# Print the max sender
print max_mail, max_count





