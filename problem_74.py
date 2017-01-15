from math import factorial as f


def sum_factorial(n):

	s = [f(int(x)) for x in str(n)]

	return sum(s)

#stops = [145, 169, 871, 872]

collect_steps = [0] * 1000000

for n in range(1,1000000):

	if n%1000 == 0:
		print n

	non_repeating = True

	start = n

	steps = []

	while non_repeating:

		steps.append(start)

		start = sum_factorial(start)

		if start in steps:

			non_repeating = False

	collect_steps[n] = len(steps)

su = 0
for n in collect_steps:

	if n == 60:
		su+=1

print su




