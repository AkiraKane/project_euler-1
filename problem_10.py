# PE Problem 10: Find the sum of all primes below two million

from math import sqrt

def is_prime(x):

	i = 2

	#print (int(x/2) + 1)

	while i < (int(sqrt(x)) + 1):

		#print i

		if x%i == 0:

			return False

		i += 1

	return True

su = 0

for i in range(2,2000000):

	if is_prime(i):
		
		su += i

print su