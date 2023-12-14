# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of
# those values and produce an output as shown below. Do not use the sum() function or a variable named sum
# in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below
# enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total_pr = 0
count = 0
average = 0

for line in fh:
    line1 = line.strip()
    if not line1.startswith("X-DSPAM-Confidence:"):
        continue
    clone_position = line1.find(":")
    pr = float((line1[clone_position+2:]))
    total_pr += pr
    count += 1

average = total_pr / count
print("Average spam confidence: ", average)
print("Done")