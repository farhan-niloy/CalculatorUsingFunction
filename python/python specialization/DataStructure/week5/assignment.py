name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# Initialize an empty dictionary to store sender counts
sender_counts = dict()

for line in handle:
    line = line.rstrip()

    # Check if the line starts with 'From '
    if line.startswith('From '):
        words = line.split()

        # Extract the sender's email address (the second word in the 'From ' lines)
        sender = words[1]

        # Update the count for the sender in the dictionary
        sender_counts[sender] = sender_counts.get(sender, 0) + 1

handle.close()

# Find the most prolific sender using a maximum loop
largest_count = -1
most_prolific_sender = None

for sender, count in sender_counts.items():
    if count > largest_count:
        largest_count = count
        most_prolific_sender = sender

# Print the result
print('Done', most_prolific_sender, largest_count)
