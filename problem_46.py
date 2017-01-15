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

upper = 100000

for n in range(upper):

	if is_prime(n):

		primes.append(n)

adds = []

for n in range(1,upper):

	adds.append(2 * (n ** 2))

#print adds[:19]

top_prime = 2

print 'looping'

for i in range(3,upper,2):

	if i%5 == 0:

		print i

	if is_prime(i):

		top_prime = i 

		continue

	adds_ind = 0

	smaller = True

	while smaller:

		smaller = adds[adds_ind] < i

		adds_ind += 1

	'''
	for a in primes[:primes.index(top_prime) + 1]:

		for b in adds:

			if i == a + b:

				print i, '=', a, '+', b

				continue
	'''

	sums = [(a + b) for a in primes[:primes.index(top_prime) + 1] for b in adds[:adds_ind + 1]]

	if i not in sums:
		print 'DING DING!', i

			
