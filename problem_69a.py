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

primes = []

for n in range(1,1000000):

	if is_prime(n):

		primes.append(n)

maxi = 0.5

for j in range(1,1000000):

	if j%1000 == 0:
		print j

	rt = int(sqrt(j)) + 1

	primes_divide_into = []

	for p in primes:

		if j%p == 0:

			primes_divide_into.append(p)

		if p > j:

			break

	product = j * 1.0

	for p in primes_divide_into:

		product *= (1 - 1.0/p)

	cand = 1.0 * j / product

	if cand > maxi:

		print j, cand
		maxi = cand
