from math import sqrt

def is_prime(n):

	if n == 1:

		return False

	if n < 4:

		return True

	if n%2 == 0:

		return False

	if n<9:

		return True

	if n%3 == 0:

		return False

	r = int(sqrt(n))

	f = 5

	while f <= r:

		if n%f == 0:

			return False

		if n%(f + 2) == 0:

			return False

		f += 6

	return True



primes = []

for i in range(1,1000001):

	if is_prime(i):

		primes.append(i)

#print len(primes)

#print primes.index(953)

max_target = 953

max_window = 21

'''
for p in range(160,1000):

	target = primes[p]

	for n in range(0,p - max_window):

		test_sum = sum(primes[n:n + max_window + 1])

		if test_sum
'''

collect = []

i = 100

for p in range(len(primes)-1,len(primes) - i,-1):

	print p

	target_prime = primes[p]

	#print ""
	#print target_prime

	for n in range(p):

		for m in range(1,p - n + 1):

			if m < n:
				break

			test_sum = sum(primes[n:m])

			#print n, m, primes[n:m], test_sum

			if test_sum == target_prime:

				print 'SUM FOUND!', target_prime

				#print target_prime

				collect.append([target_prime, len(primes[n:m])])

			if test_sum > target_prime:

				break

print collect









