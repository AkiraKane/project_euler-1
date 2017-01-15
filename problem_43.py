from itertools import permutations

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

p = [list(x) for x in list(permutations(digits))]

def prime_time(l):

	primes = [2, 3, 5, 7, 11, 13, 17]

	for n in range(1,8):

		s = 100 * l[n] + 10 * l[n + 1] + 1 * l[n + 2]

		if s % primes[n - 1] != 0:

			return False

	return True

su = 0

for i in range(len(p)):

	#print p[i]

	if prime_time(p[i]):

		print p[i]


