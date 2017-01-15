fractions = []

for d in range(2,1000000):

	if d%1000 == 0:
		print d

	for n in range(int(3*d/7) - 5,int(3*d/7) + 5):

		fractions.append([n,d,float(n)/d])

#print fractions

fractions.sort(key=lambda x: x[2])

for f in fractions:

	if f[0] == 3 and f[1] == 7:

		ind = fractions.index(f)

for j in fractions[ind-5:ind+5]:

	print j



