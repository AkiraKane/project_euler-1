

cubes = []

for n in range(465,50000):

	d = [int(x) for x in str(n**3)]
	d.sort()

	z = [n, n**3, d]
	cubes.append(z)
	#print z

for c in cubes:

	su = 0

	for e in cubes:

		if c[2] == e[2]:

			su += 1

	print c, su
	if su == 5:
		print 'GOT IT!'
		break