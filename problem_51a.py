from math import sqrt
import itertools

def is_prime(n):

	if n == 1:

		return False

	if n < 4:

		return True

	if n % 2 == 0:

		return False

	if n < 9:

		return True

	if n % 3 == 0:

		return False

	r = int(sqrt(n))

	f = 5

	while f <= r:

		if n % f == 0:

			return False

		if n % (f + 2) == 0:

			return False

		f += 6

	return True


primes = []

for n in range(1000000):

	if is_prime(n):

		primes.append(n)

len_digits = 6
target = 8

selected_primes = []

for p in primes:

	if len(str(p)) == len_digits:

		selected_primes.append(p)

	if len(str(p)) > len_digits:

		break

print len(selected_primes)

combos = [list(f) for f in list(itertools.product([0,1], repeat = len_digits))]

#print combos
combos.pop(0)
combos.pop(-1)
#print combos

def replacer(insert_val, starting_num, template):

	if insert_val == 0 and template[0] == 1:

		#print 'starting zero'
		return starting_num

	s = [int(f) for f in list(str(starting_num))]

	#print s

	for d in range(len(template)):

		

		if template[d] == 1:

			s[d] = insert_val

		#print 'd:', d, 's:', s

		new_num = ''.join(map(str, s))

	return int(new_num)


for p in selected_primes[:]:

	if selected_primes.index(p)%100 == 0:
		print selected_primes.index(p) 

	for c in combos:

		collector = [p]

		for replace_val in range(10):

			new_num = replacer(replace_val, p, c)
			#print replace_val, p, c, new_num, len(c)

			if new_num in selected_primes and new_num not in collector:

				collector.append(new_num)

		#print c, collector, len(collector)

		if len(collector) - 1 == target:
			print p, c, collector




'''
for p in selected_primes[:]:

	#print p


	for d in range(len(str(p))):

		s = [int(f) for f in list(str(p))]

		note = list(s)

		note[d] = '*'

		record = [note]

		start = 0

		if d == 0:

			start = 1

		for replace_val in range(start, 10):

			s[d] = replace_val

			new_num = ''.join(map(str, s))

			new_num = int(new_num)

			if new_num in selected_primes:

				record.append(new_num)

		#print record, len(record) - 1

		if len(record) - 1 == target:

			print p
			print record, len(record) - 1
			print "GOT IT!!!"

	#print ""
'''








