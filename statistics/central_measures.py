## we will make functions to calculate mean, median, mode and percentile

def mean(x):
	try:
		return sum(x)/len(x)

	except ZeroDivisionError:
		print("input list is empty")


def median(x):
	n = len(x)
	try:
		return sorted(x)[n // 2] if n % 2 != 0 else mean([sorted(x)[n//2 -1], sorted(x)[n//2]])
	except IndexError:
		print("input list is empty")


def quantile(x, p=0.5):
	try:
		p_index = int(p * len(x))
		return sorted(x)[p_index]
	except IndexError:
		print("p value should be between 0 to 1 and input data list can't be empty")



