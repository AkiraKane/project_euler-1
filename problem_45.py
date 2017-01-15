

tri = []
pent = []
hexx = []

for n in range(100000,200000):

	tri.append(n * (n + 1) / 2)
	pent.append(n * (3 * n - 1) / 2)
	hexx.append(n * (2* n - 1))

print tri[:10]
print pent[:10]
print hexx[:10]

for j in range(100001):

	t = tri[j]

	if t in pent and t in hexx:

		print t