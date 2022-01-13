name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
di=dict()
handle = open(name)

for i in handle:
    i = i.rstrip()
    if i.startswith("From:"):
        a=i.split()
        email=a[1]
        if email in di:
            di[email]=di[email]+1
        else:
            di[email]=1
largest=-1
theword=None
for k,v in di.items():
    if v>largest:
        largest=v
        theword=k
print(theword,largest)
