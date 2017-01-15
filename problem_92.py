

def step(n):

	return sum([int(x) ** 2 for x in str(n)])

#print step(44)

arrive_at_89 = [89]
arrive_at_1 = [1]

for n in range(1,100000):

	if n%1000==0:
		print n

	go = True

	x = n

	steps = [x]

	while go:

		if x in arrive_at_89:

			arrive_at_89.extend(steps)  

			go = False

		if x in arrive_at_1:

			arrive_at_1.extend(steps)

			go = False

		x = step(x)
		steps.append(x)

	arrive_at_89 = list(set(arrive_at_89))
	arrive_at_1 = list(set(arrive_at_1))

#arrive_at_89.pop(0)
#arrive_at_1.pop(0)

print len(set(arrive_at_89))
print len(set(arrive_at_1))


	




