

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
#for i in range(1,10001):

	if abundant(i):

		abunds.append(i)

print len(abunds)

su = []

for n in range(len(abunds)):

	if n%100 == 0:

		print n

	for j in range(n,len(abunds)-1):

		if abunds[n] + abunds[j] > 28123:

			top_ind = j
			break

	#print n, top_ind

	for m in range(n,top_ind):#len(abunds)):

		s = abunds[n] + abunds[m]

		if s not in su:

			su.append(s)

#print su


print su

ccc = 0

for i in range(28124):

	if i not in su:

		ccc += i

print ccc




'''

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

'''
