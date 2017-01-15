#PE Problem 12: Value of first triangle number to have over 500 divisors
'''
def div(n):

	div = []

	for i in range(1,n/2 + 1):

		if n%i == 0:

			div.append(i)

	div.append(n)

	return div
'''
def divisors(x):

	div = [1, x]

	trial_d = 2

	caught = False

	while not caught:

		if x%trial_d == 0:

			
			div.append(trial_d)
			div.append(x/trial_d)

		trial_d += 1

		if trial_d >= div[-1]:

			caught = True

	return div


i = 10000

tri = 49995000

max_divisors = 5

while max_divisors < 501:

	tri += i

	print "triangle #:", tri

	num_div = len(divisors(tri))

	print "num_div:", num_div
	#print div(tri)

	if num_div > max_divisors:

		max_divisors = num_div

	i += 1

print tri















'''

i = 10000

tri = 49995000*12

max_divisors = 5

print len(div(tri))

while max_divisors < 501:

	tri += i

	print "triangle #:", tri

	num_div = len(div(tri))

	print "num_div:", num_div
	#print div(tri)

	if num_div > max_divisors:

		max_divisors = num_div

	i += 1

print tri
'''