

def fifth(n):

	z = [int(x)**5 for x in list(str(n))]

	return sum(z) == n

for i in range(2,10000000):

	if fifth(i):
		print i
