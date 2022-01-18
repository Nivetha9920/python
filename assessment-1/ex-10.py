S={}
while True:
 sin=input("Do you want to Add/Modify/Exit:")
 if sin == 'Add': #the Dictionary
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        S[key]=value
        print("Dict values are",S)
 elif sin=="Modify":
     key = input("Enter the key: ")
     value = input("Enter the value: ")
     S[key]=value
     print("Dict values are",S)
 else:
   quit()
