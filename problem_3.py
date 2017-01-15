# PE Problem 3: What is the largest prime factor of 600851475143
from math import ceil

x = 600851475143

half = int(ceil(x/2))
print half

def factors(n):

	factors = []

	for i in xrange(1,half + 1):

		#print i

		if n%(i) == 0:

			factors.append(i)

	factors.append(n)

	return factors

def is_prime(n):

	f = factors(n)
	print f

	if f == [1, n]:

		return True

	else:

		return False


facts = factors(x)

for x in reversed(facts):

	print is_prime(x)

# Does python have an is_prime function?


