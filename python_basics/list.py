fname = open(input("Enter file name: "))
x = 0

for line in fname:
    if line.startswith("From "):
        l = line.split()
        print(l[1])
        x = x+1

print("There were", x, "lines in the file with From as the first word")
