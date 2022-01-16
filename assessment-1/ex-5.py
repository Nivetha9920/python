str = input("Enter the numbers:")
dim=[int(x) for x in str.split(',')]
rowNum=dim[0]
colNum=dim[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print(multilist)
