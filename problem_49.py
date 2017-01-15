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

for n in range(1000,10000):

	if is_prime(n):

		primes.append(n)

#print primes

digits = []

for p in primes:

	z = [int(x) for x in list(str(p))]

	z.sort()

	#if p == 8147:

	#	print z

	digits.append([p, z])

candidates = []

for d in digits:

	src = d[1]

	cand = [d]

	count = 0

	for a in digits:

		if src == a[1]:

			#count += 1
			cand.append(a)

	#if count == 3:

		#candidates.append(cand)

	candidates.append(cand)

	#if d[0] == 8147:

		#print d[1]
		#print cand

def steps(l):

	for n in range(len(l)):

		start = l[n]

		for m in range(n + 1,len(l)):

			end = l[m]

			diff = end - start

			if end + diff in l:

				print 'match!', l

				return True

	return False





for j in candidates:

	nums = list(set([x[0] for x in j]))

	#primes = [x[1] for x in j]

	nums.sort()

	#print nums

	if len(nums) < 3:

		continue

	if steps(nums):

		print j
