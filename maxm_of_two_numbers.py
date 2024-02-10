# Python program to find the
# maximum of two numbers


def maximum(a, b):
	
	if a >= b:
		return a
	else:
		return b
	
# Driver code
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
print("Maximum of a and b is : " ,maximum(a, b))
