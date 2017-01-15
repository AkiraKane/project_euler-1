
def trunc(n,x):

	return int(str(n)[-x:])

p = 1

for i in range(78300):

	if i%100 == 0:
		print i

	p *= trunc(2 ** 100, 12)

	p = trunc(p, 12)

	#print p

p *= trunc(2 ** 457, 12)

p *= 28433

p += 1

print p



