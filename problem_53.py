from math import factorial as f 

def choose(n,r):

	z = f(n)/(f(r) * f(n - r))

	return z

su = 0

for n in range(1,101):

	for r in range(1,n - 1):

		if choose(n,r) > 1000000:

			su += 1

			print n, r

print su



