# PE Problem 1: Find the sum of all the multiples of 3 or 5 below 1000

def mult_3_or_5(x):

	if x%3 == 0 or x%5 == 0:

		return x

	else:

		return 0

su = 0

for i in range(1000):

	su += mult_3_or_5(i)

print su