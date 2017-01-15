def div(n):

	div = []

	for i in range(2,n/2 + 1):

		if n%i == 0:

			div.append(i)

	div.append(n)

	return div


def resilient(n,d):

	if n == 1:

		return True

	ds = div(n)

	for k in ds:

		if d%k == 0:

			return False

	return True

	#return not d%n == 0

def resilience(d):

	r = 0

	for n in range(1,d):

		#print n, r

		if resilient(n,d):

			r += 1

		#print n, r

	return float(r)/(d-1)

min_res = 0.37

d = 90000

while min_res >= float(15499)/94744:

	d += 1

	res = resilience(d)

	if res < min_res:

		min_res = res

	print d, min_res


print d


