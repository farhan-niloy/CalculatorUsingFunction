fhand = open('txt.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    domain = pieces[1]
    print(domain)
