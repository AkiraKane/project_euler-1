


def same_digits(l):

	# Takes a list of integers

	s = [list(str(x)) for x in l]

	s[0].sort()

	for m in s:

		m.sort()

		if m != s[0]:

			return False

	return True


for n in range(1,10000000):

	st = [2*n, 3*n, 4*n, 5*n, 6*n]

	if same_digits(st):

		print n, st

