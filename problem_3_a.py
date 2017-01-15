# PE Problem 3: What is the largest prime factor of 600851475143
from math import ceil

x = 600851475143

def is_prime(x):

	i = 2

	#print (int(x/2) + 1)

	while i < (int(x/2) + 1):

		#print i

		if x%i == 0:

			return False

		i += 1

	return True

'''


def prime_factors(x):

	factors = []

	i = 1

	while i < int(x/2) + 1:

		if x%i == 0 and is_prime(i):

			#factors.append(i)
			print 'prime!', i

		i += 2

		if (i-1)%10000000 == 0:
			print float(100*i)/x

	#factors.append(x)

	return factors

print prime_factors(x)

'''

x = 21222000

half = x/2

z = True

num = half

while z:

	#print num

	if x%num == 0 and is_prime(num):

		print num

		z = False

	num = num - 1


	


'''
half = int(ceil(x/2))
print half

def factors(n):

	factors = []

	for i in xrange(1,half + 1):

		#print i

		if n%(i) == 0:

			factors.append(i)

	factors.append(n)

	return factors

def is_prime(n):

	f = factors(n)
	print f

	if f == [1, n]:

		return True

	else:

		return False


facts = factors(x)

for x in reversed(facts):

	print is_prime(x)

# Does python have an is_prime function?

'''


