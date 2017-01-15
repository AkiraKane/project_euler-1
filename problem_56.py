

mx = 1

for a in range(1,100):

	for b in range(1,100):

		s = [int(x) for x in str(a ** b)]
		#print s

		s = sum(s)

		if s > mx:

			print a, b, s
			mx = s