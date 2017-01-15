

su = 0

for n in range(1,80):

	for e in range(1,50):

		p = n ** e

		if len(str(p)) == e:

			print n, '**', e, '=', p

			su += 1

print su