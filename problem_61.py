

tri = []
square = []
pentagonal = []
hexag = []
heptag = []
octag = []

for n in range(1,500):

	tri.append(n*(n+1)/2)
	square.append(n**2)
	pentagonal.append(n*(3*n - 1)/2)
	hexag.append(n*(2*n - 1))
	heptag.append(n*(5*n - 3)/2)
	octag.append(n*(3*n - 2))


tri = [x for x in tri if len(str(x)) == 4]
square = [x for x in square if len(str(x)) == 4]
pentagonal = [x for x in pentagonal if len(str(x)) == 4]
hexag = [x for x in hexag if len(str(x)) == 4]
heptag = [x for x in heptag if len(str(x)) == 4]
octag = [x for x in octag if len(str(x)) == 4]

print len(tri), len(square), len(pentagonal), len(hexag), len(heptag), len(octag)

shapes = [tri, square, pentagonal, hexag, heptag, octag]
'''
primes = [2, 3, 5, 7, 11, 13]

nums = []

for s in shapes:

	for n in s:

		nums.append([n, primes[shapes.index(s)], str(n)[:2], str(n)[-2:]])

combinations


'''
collector = []

for x in tri:

	z = [x]

	for shape in shapes[1:]:

		z.append([[],[]])

		for n in shape:

			if str(x)[:2] == str(n)[-2:]:

				z[shapes.index(shape)][0].append(n)

			if str(x)[-2:] == str(n)[:2]:

				z[shapes.index(shape)][1].append(n)

	collector.append(z)

print collector[0]
print collector[1]
print collector[2]
print collector[3]
