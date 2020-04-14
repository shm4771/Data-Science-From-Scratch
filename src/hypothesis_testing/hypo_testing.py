#here we will explore 3 methods of hypothesis testing via example of "fair coin"
#null hypothesis is that coin is fair so
#H0: P = 0.5
#H1: P != 0.5


import math
from ds_modules import distributions
import random

def normal_approx_binomial(n, p):
	""" population parameters from binomial distribution B(n, p)"""
	mu = n * p 
	sigma = math.sqrt(n * p * (1 - p))
	return mu, sigma


## we can also write functions to find probabilites in given intervals
def normal_probability_lower(low, mu=0, sigma=1):
	return distributions.normal_cdf(low, mu, sigma)


def normal_probability_upper(high, mu=0, sigma=1):
	return (1- distributions.normal_cdf(high, mu, sigma))


def normal_probability_two_sided(low, high, mu=0, sigma=1):
	return normal_probability_lower(low, mu, sigma) + normal_probability_upper(high, mu, sigma)


# we can also exploit the central limit theorem to compute the confidence interval
def normal_bound_upper(upper_probability, mu=0, sigma=1):
	"""The probability here is cummulative probability till desired point """
	return distributions.normal_cdf_inverse(1- upper_probability, mu, sigma)


def normal_bound_lower(lower_probability, mu=0, sigma=1):
	"""The probability here is cummulative probability till desired point """
	return distributions.normal_cdf_inverse(lower_probability, mu, sigma)


def normal_bound_two_sided(probability, mu=0, sigma=1):
	"""Assumption that the inetrval is symmatric about the mean value """
	tail_probability = (1 - probability) / 2
	low, high = normal_bound_lower(tail_probability, mu, sigma), normal_bound_upper(tail_probability, mu, sigma)
	return low, high


def significant_interval_two_sided(alpha, mu=0, sigma=1):
	return normal_bound_two_sided(1 - alpha, mu, sigma)


def calculate_p_val(x, mu=0, sigma=1):
	if sample_mean > mu:
		return 2 * normal_probability_upper(x, mu, sigma)
	else:
		return 2 * normal_probability_lower(x, mu, sigma)


def type_2_error_probability(n, p_actual, p_hypothesis, alpha):
	"""cases when we fail to reject H0 even it's not true"""
	"""How we know it's not true or value of p_actual? leave it on God"""

	mu_hypothesis, sigma_hypothesis = normal_approx_binomial(n, p_hypothesis)
	lo, hi = significant_interval_two_sided(alpha, mu_hypothesis, sigma_hypothesis)
	mu_actual, sigma_actual = normal_approx_binomial(n, p_actual)
	return distributions.normal_cdf(hi, mu_actual, sigma_actual) - distributions.normal_cdf(lo, mu_actual, sigma_actual)



"""
###Let's run a simulation for n=1000, p=0.5 (H0)
n,p = 1000, 0.5
alpha = 0.05
mu_0, sigma_0 = normal_approx_binomial(n, p)
lo, hi = significant_interval_two_sided(alpha, mu_0, sigma_0)

count_heads = 0
for _ in range(n):
	count_heads += 1 if random.random() <= 0.5 else 0

print(count_heads)
print(type_2_error_probability(n, 0.55, 0.5, alpha))
"""