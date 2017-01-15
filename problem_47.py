

from math import sqrt

def is_prime(n):

	if n == 1:

		return False

	if n < 4:

		return True

	if n % 2 == 0:

		return False

	if n < 9:

		return True

	if n % 3 == 0:

		return False

	r = int(sqrt(n))

	f = 5

	while f <= r:

		if n % f == 0:

			return False

		if n % (f + 2) == 0:

			return False

		f += 6

	return True

def prime_factorization(n, primes):

	prime_ind = 0

	smaller = True

	while smaller:

		smaller = primes[prime_ind] < n

		prime_ind += 1

	factors = []

	#print prime_ind

	for p in primes[:prime_ind]:

		done = False

		while not done:

			if n % p == 0:

				factors.append(p)

				n /= p

			else:

				done = True

	return factors

primes = []

upper = 1000000

for n in range(1,upper):

	if is_prime(n):

		primes.append(n)

#print primes

count = 0

g = 99970

while count != 4:

	z = len(set(prime_factorization(g, primes)))

	#print g, z, len(set(z))

	if z == 4:

		count += 1
		print g, z, count

	else:

		count = 0

	g += 1

	if count == 4:

		print 'HOORAY DONE!'





