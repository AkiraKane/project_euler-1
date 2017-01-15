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

def trunc_left(s):

	return s[1:]

def trunc_right(s):

	return s[:-1]


def check_for_evens(i):

	s = list(str(i))

	if len(s) == 2:

		return True

	return ('0' not in s and '2' not in s and '4' not in s and '6' not in s and '8' not in s)



upper = 1000000

primes = []

for n in range(1,upper):

	if is_prime(n):
		primes.append(n)

for p in primes[:]:

	p_r = p
	p_l = p

	truncs = []

	if check_for_evens(p):

		for n in range(len(str(p)) - 1):

			p_r = int(trunc_right(str(p_r)))

			p_l = int(trunc_left(str(p_l)))

			truncs.append(p_r)
			truncs.append(p_l)

	if truncs != []:

		if all(x in primes for x in truncs):

			print p

			







