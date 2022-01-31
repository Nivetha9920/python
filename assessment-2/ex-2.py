# import library
import re

# url link
s =input("Enter the url:")
print("URL:",s)
# finding the hostname which may
# contain dash or dots
obj2 = re.findall('://www.([\w\-\.]+)',
				s)
print("Host:",obj2)

# finding the protocol
obj1 = re.findall('(\w+)://',
				s)
print("Protocol:",obj1)
# finding the port number
obj3 = re.findall(':(\d+)', s)
print("Port number:",obj3)
