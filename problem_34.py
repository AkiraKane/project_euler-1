from math import factorial as f 

def fact_sum(n):

	z = [f(int(x)) for x in list(str(n))]

	return sum(z)

for n in range(3,150000000):

	if fact_sum(n) == n:

		print n

