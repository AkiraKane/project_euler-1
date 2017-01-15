

def pandigital_product(a,b,c):

	s = list(str(a) + str(b) + str(c))

	#s = s.extend(list(str(c)))

	s = [int(x) for x in s]

	#print s

	s.sort()

	if len(s) != 9:

		return False

	if s == [1,2,3,4,5,6,7,8,9]:

		return True

	return False

products = []


for m in range(5000):

	if m % 100 == 0:
		print m

	for u in range(2000):

		p = m * u

		

		if pandigital_product(p,m,u) and p not in products:

			products.append(p)

			print m, u, p, pandigital_product(m,u,p)

print sum(products)





