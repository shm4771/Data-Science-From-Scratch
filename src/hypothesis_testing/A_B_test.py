# Here we will conduct a A/B test
import math

from hypo_testing import normal_probability_two_sided

def estimated_parameter(n, N):
	p = n / N
	sigma = math.sqrt(p * N * (1- p))
	return N * p, sigma

def a_b_test_statistics(n_a, N_a, n_b, N_b):
	p_a, sigma_a = estimated_parameter(n_a, N_a)
	p_b, sigma_b =estimated_parameter(n_b, N_b)
	print(p_a, p_b, math.sqrt(sigma_a **2 + sigma_b ** 2))
	return (p_a - p_b) / math.sqrt(sigma_a **2 + sigma_b ** 2)

z = abs(a_b_test_statistics(200, 1000, 180, 1000))


print(z)
probability = normal_probability_two_sided(-z, z)

print(probability)