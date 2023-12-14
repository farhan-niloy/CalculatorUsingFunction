xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)

fhand = open('mbox.txt')
count = 0
for line in fhand:
    count += 1
print('Line Count: ', count)

lhand = open('mbox.txt')
inp = lhand.read()

print(len(inp))
print(inp[:20]) //slicing

xhand = open('mbox-short.txt')
for line in xhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

yhand = open('mbox-short.txt')
for line in xhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        print(line)

fname = input('Enter your file name: ')
try:
    fhand = open(fname);
except:
    print("File can't be opened:", fname)
    quit()

count = 0

for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)