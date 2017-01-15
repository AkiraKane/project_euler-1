from math import sqrt
from itertools import permutations

def rotate(p,n):

	l = str(p)

	return int(l[n:] + l[:n])

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

print len(primes)

su = 0

for p in primes:

	#rots = []

	#for j in range(len(str(p))):

	#	rots.append(rotate(p,j))

	rots = [rotate(p,j) for j in range(len(str(p)))]

	rots = [is_prime(x) for x in rots]

	if all(x for x in rots):

		su += 1

print su









#su = 0 # Excludes 2, so start at one, 22 under primes[:10000], 0 more up to 50000
'''
for i in range(50000,len(primes)):

	p = primes[i]

	if i%200 == 0:

		print i



	digits = [int(x) for x in list(str(p))]



	if 0 in digits or 2 in digits or 4 in digits or 6 in digits or 8 in digits or 5 in digits:
		#print 'skip bo!'
		continue

	#print digits
	

	z = list(permutations(digits))



	#print z

	#z = [list(x) for x in z]

	#print z

	z = [int(''.join(map(str, list(x)))) for x in z]

	#print z

	zz = [d in primes for d in z]

	#print z
	#print zz

	if all(x == True for x in zz):

		su += 1
		print p

print su
'''