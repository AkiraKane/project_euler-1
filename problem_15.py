# PE Problem 15: How many routes, only moving right and down are there in a 20x20 grid?

from math import factorial

def n_choose_k(n, k):

	return factorial(n)/(factorial(k)*factorial(n-k))

print n_choose_k(40,20)