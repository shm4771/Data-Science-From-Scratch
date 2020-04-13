## The theorem says that the avg of identically distrubted independent variables
##is roughly normal distributed

## we will use bunomial distribution to draw variable

import random
from collections import Counter
import matplotlib.pyplot as plt

def bernoulli_trial(p):
	return 1 if random.random() < p else 0


def binomial(n, p):
	return sum([bernoulli_trial(p) for _ in range(n)])


#we will make a histogram of K such trials

def make_hist(p, n, num_points):
	data = [binomial(n, p) for _ in range(num_points)]

	histogram = Counter(data)
	plt.bar([x - 0.4 for x in histogram.keys()], [v / num_points for v in histogram.values()])

	plt.show()


#make_hist(0.4, 10, 1000)
