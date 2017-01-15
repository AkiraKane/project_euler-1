#def reduce(n, d):








fractions = []

for d in range(2,12):

	if d%100 == 0:
		print d

	for n in range(int(d/3) - 2,int(d/2) + 2):

		fractions.append([n, d, float(n)/d])

fractions.sort(key=lambda x: x[2])

for f in fractions:
	if f[0] == 1 and f[1] == 3:
		s_ind = fractions.index(f)
	if f[2]== 0.5:

		e_ind = fractions.index(f)
		break
dec = []
for f in fractions[s_ind:e_ind+1]:
	dec.append(f[2])

prin




