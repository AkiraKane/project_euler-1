ms = [2,3,4]

def pandigital(s):

	l = list(s)

	l = [int(x) for x in l]

	l.sort()

	return l == [1,2,3,4,5,6,7,8,9]

for i in range(1,999999):

	for m in ms:

		products = []

		for n in range(m):

			products.append(i*(n+1))

		s = [str(x) for x in products]

		s = ''.join(map(str, s))

		if pandigital(s):

			print i, m, s



