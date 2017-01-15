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

def prime_up_to(n):

	p = [2]

	for i in range(3, n):

		if is_prime(i):

			p.append(i)

	return p

def prime_sums(n):

	primes = prime_up_to(n)

	primes_f = list(primes)

	primes.reverse