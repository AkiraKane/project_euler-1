

def fractionater(n, d):

	val = float(n)/d

	nn = [int(x) for x in list(str(n))]

	dd = [int(x) for x in list(str(d))]

	#print nn, dd

	if nn[0] in dd:

		dd.pop(dd.index(nn[0]))

		#nn.pop(0)

		target = float(nn[1])/dd[0]

		#print nn[1], dd[0]

		if target == val:

			print 'DING!', n, d

	elif nn[1] != 0 and nn[1] in dd:

		#print n, d

		dd.pop(dd.index(nn[1]))

		#nn.pop(1)

		#print nn[0], dd[0]
		
		try:
			target = float(nn[0])/dd[0]

			if target == val:

				print 'DING!', n, d

		except:
			pass

		


for d in range(11,100):

	for n in range(10,d):

		fractionater(n, d)

