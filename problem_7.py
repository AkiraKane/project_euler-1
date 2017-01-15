

def is_prime(x):

	i = 2

	#print (int(x/2) + 1)

	while i < (int(x/2) + 1):

		#print i

		if x%i == 0:

			return False

		i += 1

	return True

primes = [2]

i = 3

while len(primes) < 10001:

	if is_prime(i):

		primes.append(i)

	i += 2

print primes

