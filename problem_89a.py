

nu = 'MMMDLXVIIII'

def recast_roman(s):

	numeral = list(s)

	counts = {'M': 0, 'D': 0, 'C': 0, 'L': 0, 'X': 0, 'V': 0, 'I': 0}

	for i in numeral:

		counts[i] += 1

	return counts


x = recast_roman(nu)

for j in x:
	print x[j]


