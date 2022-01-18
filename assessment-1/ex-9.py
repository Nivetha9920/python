def checkKey(S, key):

    if key in S:
        print("Present, ", end =" ")
        print("value =", S[key])
    else:
        print("Not present")
S = {} #the Dictionary
maximum = int (input("Enter the Maximum:"))
for i in range(0,maximum):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    S[key]=value
print("Dict values are",S)
key=input("Enter the key to search:")
checkKey(S, key)
