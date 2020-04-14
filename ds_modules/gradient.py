## first we will apply batch gradient algorithm
#rather than fixing constant step size, we will range of step sizes and will choose which will minimize the error function or bigger benefit

import vectors
from functools import partial, reduce
import vectors
import random

def linear_hypothesis(X, theta):
	return vectors.dot(theta, X)

def partial_difference_quotient(target_fn, v, i, h):
	"""This function caluculate ith derivative"""
	w = [v_i + (h if i == j else 0) for j, v_i in enumerate(v)]
	return (target_fn(w) - target_fn(v)) / h

def estimated_gradient(target_fn, v, h=0.0001):
	"""return the gradient function of the given hypothesis funtion"""
	return [partial_difference_quotient(target_fn, v, i, h) for i,_ in enumerate(v)]


def step(step_size, gradient, theta):
	"""return the modified theta value"""
	return vectors.vector_subtract(theta, vectors.scalar_multiply(step_size, gradient))


def negate(f):
	""" to calculate the negative of real valued function f for given input"""
	return lambda *args, **kwargs: -f(*args, **kwargs)

def negate_all(f):
	"""return the negative of vector valued f (a list as output)"""
	return lambda *args, **kwargs: [- f_i for f_i in f(*args, **kwargs)] 

def minimum_batch(target_fn, gradient_fn, theta_0, tolerence = 0.00001):
	"""This function minimizes the target function for theta parameter """
	step_sizes = [100, 10, 1, 0.1, 0.01, 0.0001, 0.00001]
	theta = theta_0
	value = target_fn(theta_0)
	error = 1000
	print("theta:", theta, "error:", error, value)
	while error >= tolerence:
		gradient = gradient_fn(theta)
		next_thetas = [step(step_size_i, gradient, theta) for step_size_i in step_sizes]
		next_theta = min(next_thetas, key=target_fn)
		next_val = target_fn(next_theta)
		error = value - next_val
		theta, value = next_theta, next_val
		print("theta:", theta, "error:", error, value)

	return theta


def maximum_batch(target_fn, gradient_fn, theta_0, tolerence = 0.00001):
	return minimum_batch(negate(target_fn), negate_all(gradient_fn), theta_0)


"""
#code for testing batch gradient & linear_regression using batch gradient 

def square_error(e):
	#just a function to test the gradient algo 
	return sum((e_i **2) for e_i in e)


## To test the batch gradient descent
gradient = partial(estimated_gradient, square)
maximum_batch(square, gradient, [100, 20])


#using batch gradient in Linear Regression
def cost(data_x, data_y, theta):
	m = len(data_x)
	cost = 0
	y_pred = [linear_hypothesis(data_i, theta) for data_i in data_x]
	error = square(vectors.vector_subtract(y_pred, data_y))
	return error / m 

#testing batch gradient with linear regression
#z = 2 + 3x + 2y
x_data = [[0,0], [1,1], [2,0], [3,4], [2,4]]
y_data = [1.9, 7.1, 7.8, 19.1, 16]
target_error_fn = partial(cost, x_data, y_data)
gradient = partial(estimated_gradient, target_error_fn)
minimum_batch(target_error_fn, gradient, [0, 0]) 

"""
	

## stochastic gradient discent
#here we will only pick one point at a time to compute the gradient


def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
 data = zip(x, y)
 theta = theta_0 # initial guess
 alpha = alpha_0 # initial step size
 min_theta, min_value = None, float("inf") # the minimum so far
 iterations_with_no_improvement = 0
 # if we ever go 100 iterations with no improvement, stop
 while iterations_with_no_improvement < 100:
 value = sum( target_fn(x_i, y_i, theta) for x_i, y_i in data )
 if value < min_value:
 # if we've found a new minimum, remember it
 # and go back to the original step size
 min_theta, min_value = theta, value
 iterations_with_no_improvement = 0
 alpha = alpha_0
 else:
 # otherwise we're not improving, so try shrinking the step size
 iterations_with_no_improvement += 1
 alpha *= 0.9
 # and take a gradient step for each of the data points
 for x_i, y_i in in_random_order(data):
 gradient_i = gradient_fn(x_i, y_i, theta)
 theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))
 return min_theta


def maximize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
 return minimize_stochastic(negate(target_fn),
 negate_all(gradient_fn),
 x, y, theta_0, alpha_0)

