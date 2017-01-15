

def div(n):

	div = []

	for i in range(1,n/2 + 1):

		if n%i == 0:

			div.append(i)

	#div.append(n)

	return div

def abundant(x):

	d = div(x)

	return (sum(d) > x)

abunds = []

for i in range(1,28124):

	if abundant(i):

		abunds.append(i)

#print abunds

su = []







for n in range(10001):

	if n%1000 == 0:
		print n

	for j in abunds:

		if j < (n - j + 1):

			if n - j in abunds and n not in su:

				su.append(n)

print su

ccc = 0

for i in range(28124):

	if i not in su:

		ccc += i

print ccc


