##Covariance and correlation

from data_science_from_scratch.linear_algebra import vectors
import dispersion_measures as dm
import central_measures as cm

def covariance(x, y):
	n = len(x)
	return vectors.dot(dm.de_mean(x, cm.mean(x)), dm.de_mean(y, cm.mean(y))) / (n-1)


def correlation(x, y):
	return covariance(x, y) / (dm.std_deviation(x) * dm.std_deviation(y))
