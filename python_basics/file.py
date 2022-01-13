# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
num = 0
try:
    fh = open(fname)
except:
    print('invalid file name')
    quit()
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    pst = line.find('0')
    snum = line[pst:]
    fnum = float(snum)
    count = count + 1
    num = num + fnum
print('Average spam confidence:',num/count)
