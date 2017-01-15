

n = 156

s = []

print n
print '---'

while n > 999:

	n -= 1000
	s.append('M')

while n > 499:

	n-= 500
	s.append('L')

while n > 99:

	n -= 100
	s.append('C')

while n > 49:

	n -= 50
	s.append('D')

while n > 9:

	n -= 10
	s.append('X')

while n > 4:

	n -= 5
	s.append('V')

while n > 0:

	n -= 1
	s.append('I')

print n
print s

