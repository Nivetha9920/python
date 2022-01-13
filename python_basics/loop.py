largest = 0
smallest = 'none'
while True:
    val = input("Enter the number: \n")
    if val == "done":
        break
    try:
        fval = int(val)
    except:
        print("Invalid input")

    if fval > largest:
        largest = fval
    if smallest == 'none':
        smallest = fval
    if fval < smallest:
        smallest = fval
print("Maximum is", largest)
print("Minimum is", smallest)   
