
convergents = []

for n in range(1,100):

	convergents.extend([1, 2 * n, 1])

denoms = [1, 3]

numerators = [1, 2]

fractions = []

for n in range(1,100):

	denom = denoms[-1] * convergents[n + 1] + denoms[-2]

	denoms.append(denom)

	numer = numerators[-1] * convergents[n + 1] + numerators[-2]

	numerators.append(numer)

	fractions.append([numer + 2 * denom, denom])

#for f in fractions:
#	print f

print fractions[96]

print sum([int(x) for x in list(str(fractions[96][0]))])











#print denoms







