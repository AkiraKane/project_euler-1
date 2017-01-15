def step(n):

	return sum([int(x) ** 2 for x in str(n)])

ends_at_89 = [89]
ends_at_1 = [1]

su = 0

for n in range(1,10000000):

	if n%50000 == 0:
		print n

	x = n 

	while x != 1 and x != 89:

		x = step(x)

	if x == 89:

		su += 1	

print su




'''
for n in range(1,10000000):

	if n%1000 == 0:
		print n

	#x = n

	steps = [n]

	while steps[-1] not in ends_at_89 and steps[-1] not in ends_at_1:

		steps.append(step(steps[-1]))

		if steps[-1] in ends_at_89:

			ends_at_89.extend(steps[:-1])

		if steps[-1] in ends_at_1:

			ends_at_1.extend(steps[:-1])

'''

	#print n, steps
	#print ends_at_89
	#print ends_at_1

#print len(ends_at_89)
#print len(ends_at_1)
#print len(set(ends_at_89))
#print len(set(ends_at_1))
		

		





'''

for n in range(1,100000):

	if n%1000==0:
		print n

	if n in ends_at_89 or n in ends_at_1:

		continue

	steps = []

	x = n

	go = True

	while go:

		steps.append(x)

		x = step(x)

		if x in ends_at_89:

			ends_at_89.extend(steps)
			ends_at_89 = list(set(ends_at_89))
			go = False

		if x in ends_at_1:

			ends_at_1.extend(steps)
			ends_at_1 = list(set(ends_at_1))
			go = False

	#print n, steps

print len(ends_at_89)
print len(ends_at_1)
'''
		

