
pentagonal = []

for n in range(1,10000):

	pentagonal.append(n * (3 * n - 1) / 2)

for p in pentagonal:

	for b in pentagonal[:pentagonal.index(p)]:

		if p - b in pentagonal and p + b in pentagonal:

			print p, b

