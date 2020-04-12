##tuples are just non-changable lists
my_list = [1, 2]
my_tuple = (1, 2)

my_list[1] = 3

try:
	my_tuple[1] = 3
except TypeError:
	print("can not modify a tuple")

#tuples are conevnient to return multiple values from a function
def sum_and_multiply(x,y):
	return (x + y),(x * y)

s, p = sum_and_multiply(2, 3)

#swaping using tuples
s, p = p, s