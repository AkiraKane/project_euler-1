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

start = 1

corners = [0]

for s in range(3,35000,2):

	for n in range(4):

		start += (s - 1)

		#corners.append(start)

		if is_prime(start):

			corners.append(1)

		else:

			corners.append(0)

		

	if float(sum(corners))/len(corners) < 0.1:

		print s

#print corners	