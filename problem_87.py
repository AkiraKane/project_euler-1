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

for n in range(1, 7100):

	if is_prime(n):

		primes.append(n)

print len(primes)

sums = []

for a in primes:

	if primes.index(a)%10 == 0:
		print primes.index(a), len(sums)

	for b in primes[:79]:

		#if b > 400:
		#	break

		for c in primes[:25]:

			#if c > 90:
			#	break

			x = a ** 2 + b ** 3 + c ** 4

			if x < 50000000:# and x not in sums:

				sums.append(x)

			else:
				#print a,b,c, x
				break


print len(list(set(sums)))
