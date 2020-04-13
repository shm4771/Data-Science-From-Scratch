##In this file we will provide vector operations using list as representation

from functools import partial, reduce
import math

def vector_add(u, v):
	"""This function adds two vectors componnet wise """
	return [u_i + v_i for u_i, v_i in zip(u, v)]

def vector_subtract(u, v):
	"""This function subtracts two vectors componnet wise """
	return [u_i - v_i for u_i, v_i in zip(u, v)]


#we want one more function to add a list of vectors
#vector_sum[v1, v2, v3, ..., vn]
vector_sum = partial(reduce, vector_add)

def scalar_multiply(c, v):
	return [c * v_i for v_i in v]


def vector_mean(vectors):
	n = len(vectors)
	return scalar_multiply(1/n, vector_sum(vectors))

def dot(u, v):
	""" u_1 * v_1 + ... = v_n*w_n"""
	return sum(u_i * v_i for u_i, v_i in zip(u, v))

def sum_of_squares(v):
	return dot(v, v)

def magnitude(v):
	return math.sqrt(sum_of_squares(v))

def squared_distance(u, v):
	return sum_of_squares(vector_subtract(u, v))

def distance(u, v):
	return math.sqrt(squared_distance(u, v))
