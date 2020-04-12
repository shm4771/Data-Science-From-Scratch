## range, variance, std. deviation, inter_quantile_range, de_mean

from central_measures import mean
import ../linear_algebra/vectors

def range(x):
	try:
		min_val = min(x)
		max_val = max(x)
		return max_val - min_val
	except ValueError:
		print("input list is empty")
	
def de_mean(x, x_bar):
	return x - x_bar

#def variance(x):



