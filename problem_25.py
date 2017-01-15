# PE Problem 25: Index of the first fibonacci number to have 1000 digits

f = [1, 1]

max_dig = 1

while max_dig < 1000:

	#print f[-1]

	f.append(f[-1] + f[-2])

	max_dig = len(str(f[-1]))

	#print len(str(f[-1]))

print len(f)