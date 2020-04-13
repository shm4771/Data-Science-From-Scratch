##here we will implement uniform pdf (probability distribution function)
##uniform_cdf(cumulative distribution function), normal_pdf, normal_cdf,
#normal_cdf_inverse to calculate the point corresponding to the probability

from functools import reduce
import matplotlib.pyplot as plt 
import math

import random
from collections import Counter

def uniform_pdf(x):
	return 1 if x >= 0 and x < 1 else 0

def uniform_cdf(x):
	if x < 0: return 0
	elif x < 1: return x 
	else: return 1

"""
#plotting Uniform cdf
xs = [x_i/100 for x_i in range(-100, 200)]
ys = [uniform_cdf(x_i) for x_i in xs]

plt.plot(xs, ys, 'g-')
plt.title("The uniform cdf")
plt.axis([-1, 2, -1, 2])
plt.show()
"""

def normal_pdf(x, mu=0, sigma=1):
	sqrt_two_pi = (math.sqrt(2 * math.pi)) 

	return math.exp(- (x-mu) **2 / (2 * sigma **2)) / (sqrt_two_pi * sigma)

def normal_cdf(x, mu=0, sigma=1):
	return (1 + math.erf((x-mu) / (math.sqrt(2) * sigma))) / 2

"""
#plotting normal pdf
xs = [x_i/100 for x_i in range(-600, 600)]
ys = [normal_pdf(x_i, sigma=0.5) for x_i in xs]

plt.plot(xs, ys, 'g-')
plt.title("The normal pdf")
plt.axis([-6, 6, 0, 1])
plt.show()
"""

def normal_cdf_inverse(p, mu=0, sigma=1, tolerence=0.00001):
	""" we will use binary search for find the point X for which cumulative probability is known """
	z_min, z_max = -10, 10
	#p_min, p_max = normal_cdf(-10), normal_cdf(10)

	error = 10
	while error > tolerence:
		z_mid = (z_min + z_max)/2 
		error = abs(normal_cdf(z_mid) - p)
		if abs(error) <= tolerence:
			return mu + sigma * z_mid
		elif error > 0:
			z_max = z_mid
		else:
			z_min = z_mid


## Bunomials and bernoulli distribution

def bernoulli_trial(p):
	return 1 if random.random() < p else 0


def binomial(n, p):
	return sum([bernoulli_trial(p) for _ in range(n)])

