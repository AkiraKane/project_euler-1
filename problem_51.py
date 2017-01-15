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

def diff(s1, s2):

	z = [0] * len(s1)

	d = [s1[x] == s2[x] for x in range(len(s1))]

	for n in range(len(s1)):

		if not d[n]:

			z[n] = 1

	return z

primes = []
upper = 1000000

for i in range(11,upper):

	if is_prime(i):
		primes.append(i)

length = 6

target_primes = []

for p in primes:

	if len(str(p)) == length:

		target_primes.append([int(x) for x in str(p)])

	if len(str(p)) > length:

		break

#print target_primes

for p in target_primes:

	print p


'''
for p in primes[:50]:

	s = list(str(p))

	for q in primes[:100]:

		t = list(str(q))

		if len(s) == len(t):

			dif = diff(s,t)

			print s, t, dif


'''

