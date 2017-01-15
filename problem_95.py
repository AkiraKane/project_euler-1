

def divisors(n):

	div = [1]

	for i in range(2, int(n/2) + 1):

		if n%i == 0:

			div.append(i)

	return div

def sum_div(n):

	return sum(divisors(n))

max_len = 2

for n in range(1,15000):

	v = True

	if n%200 == 0:
		print n

	chain = []

	x = n

	while x not in chain:

		chain.append(x)

		x = sum_div(x)

		if x > 1000000:

			v = False
			break

	chain.append(x)

	

	if chain[-1] == chain[0] and len(chain) > max_len and v:

		print n, chain
		max_len = len(chain)	

#14316