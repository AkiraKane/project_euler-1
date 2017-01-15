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

def pandigital(n):

	digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	z = [int(x) for x in list(str(n))]

	for i in range(len(z)):

		try:
			z.pop(z.index(digits[i]))
		except:
			pass

	if z == []:

		return True

	else:

		return False

primes = []

for n in range(10000000):

	if is_prime(n):

		primes.append(n)

for p in primes:

	if pandigital(p):

		print p

