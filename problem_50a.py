from math import sqrt

def is_prime(n):

	if n == 1:

		return False

	if n < 4:

		return True

	if n%2 == 0:

		return False

	if n<9:

		return True

	if n%3 == 0:

		return False

	r = int(sqrt(n))

	f = 5

	while f <= r:

		if n%f == 0:

			return False

		if n%(f + 2) == 0:

			return False

		f += 6

	return True

primes = []

for i in range(1,1000001):

	if is_prime(i):

		primes.append(i)

#print len(primes)



for window in range(201,1000,2):

	for n in range(1001):#len(primes) - window):

		x = sum(primes[n:n + window])

		if x in primes:

			print x, window