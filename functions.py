#type 1 - use define keyword with explicity parameters

def double(x):
	""" This place is used to define the finction behavior"""
	return x ** 2

# type 2 - we can also treat function names 
#as variable and pass them as parameters
def apply_to_one(f):
	""" use the function name and call it with some arguements"""
	return f(1)

my_double = double
print(apply_to_one(my_double))


#Lambda functions to write 1 line expression
y = apply_to_one(lambda x: x+4)
print(y)


##functions can also given default favlues
def income_rise(a, b=0.1):
	""" a is the base income an b is percentage rise"""
	return a * (1+b)

print(income_rise(a=10, b=0.12))