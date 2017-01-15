

# Find Primes under 1000 for possible b's

def div(n):

	div = []

	for i in range(1,n/2 + 1):

		if n%i == 0:

			div.append(i)

	#div.append(n)

	return div

def is_prime(n):

	d = div(n)

	return d == [1]

primes = []

for i in range(1,1001):

	if is_prime(i):

		primes.append(i)

#print primes

max_run = 1

for b in primes:

	for a in range(-1000,1000):

		n = 0

		still_making_primes = True

		while still_making_primes:

			still_making_primes = is_prime(n**2 + a*n + b)

			if still_making_primes:

				n += 1

		if n > max_run:

			print 'new max!', a, b

			max_run = n








