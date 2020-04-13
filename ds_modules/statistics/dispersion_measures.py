## range, variance, std. deviation, inter_quantile_range, de_mean


#import data_science_from_scratch.linear_algebra.vectors as vector
import central_measures as cm
from data_science_from_scratch.linear_algebra import vectors
import math

def range(x):
	try:
		min_val = min(x)
		max_val = max(x)
		return max_val - min_val
	except ValueError:
		print("input list is empty")
	
def de_mean(x, x_bar):
	return [x_i - x_bar for x_i in x]

def variance(x):
	try:
		n = len(x)
		x_bar = cm.mean(x)
		return vectors.sum_of_squares(de_mean(x, x_bar))/(n-1)

	except ZeroDivisionError:
		print("inputs data should have atleast 2 entries")

def std_deviation(x):
	try:
		return math.sqrt(variance(x))
	except ZeroDivisionError:
		print("inputs data should have atleast 2 entries")

def inter_quantile_range(x):
	try:
		return cm.quantile(x, 0.75) - cm.quantile(x, 0.25)
	except IndexError:
		print("input data list can not be empty")





