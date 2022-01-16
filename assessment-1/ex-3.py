# Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = int(input("Enter a number: "))

# check if the number is negative
if num < 0:
   print("factorial does not exist for negative numbers")
else:
   print(recur_factorial(num))
