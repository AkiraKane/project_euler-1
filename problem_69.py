def factors(n):

	factors = []

	for i in range(1,int(n/2) + 1):

		if n%i == 0:

			factors.append(i)

	factors.append(n)

	return factors

def coprime(f1, f2):

	f1.pop(0)
	f2.pop(0)

	for f in f1:

		if f in f2:

			return False

	return True


def totient(n):

	relatively_prime = 0

	for i in range(1,n):

		if coprime(factors(n), factors(i)):

			relatively_prime += 1

	return relatively_prime

maximum = 0.5

for n in range(10000,2, -2):

	if n%500 == 0:

		print n

	if float(n)/totient(n) > maximum:

		maximum = float(n)/totient(n)

		print n, maximum



