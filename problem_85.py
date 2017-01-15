


collector = []

for s1 in range(3,200):

	if s1%10 == 0:
		print s1

	for s2 in range(1,s1 + 1):

		#s1 = 4
		#s2 = 4

		su = 0

		for a in range(1,s1 + 1):

			for b in range(1, s2 + 1):

				dim_s1 = s1 - a + 1
				dim_s2 = s2 - b + 1

				count = dim_s1 * dim_s2

				su += count

		collector.append([s1, s2, s1 * s2, su, abs(2000000 - su) ])

collector.sort(key = lambda x: x[4])

collector.reverse()

for i in collector:

	print i

		