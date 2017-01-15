
f = []

for n in range(1, 250000):

	f.extend(list(str(n)))


for e in range(7):

	print f[(10 ** e) - 1]

