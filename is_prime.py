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