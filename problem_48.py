

def get_last_ten_digits(n):

	s = str(n)[-10:]

	#print s

	return int(s)

su = 0

for n in range(999,0,-1):

	su += get_last_ten_digits(n ** n)

print get_last_ten_digits(su)