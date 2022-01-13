name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

di = dict()

for line in handle:
    if line.startswith('From'):
        words = line.rstrip().split()
        if len(words) <4:
            continue

        x,y,z = words[5].split(':')

        di[x]=di.get(x,0) + 1
for k,v in sorted(di.items()):
    print(k,v)
