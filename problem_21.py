# PE Problem 21: Amicable Numbers - evaluate the sum of all amicable numbers under 10000

def div(n):

	div = []

	for i in range(1,n/2 + 1):

		if n%i == 0:

			div.append(i)

	#div.append(n)

	return div

def d(n):

	return sum(div(n))

d_nums = []

for i in range(1,10001):

	d_nums.append([i, d(i)])

amicable = []

for j in d_nums:

	for k in d_nums:

		if j != k:

			if j[0] == k[1] and k[0] == j[1]:

				if k not in amicable:

					amicable.extend(j)

print amicable
print sum(amicable)
