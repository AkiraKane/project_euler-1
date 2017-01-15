from math import sqrt
from decimal import *

getcontext().prec = 103

total = 0

#n = 2

#s = Decimal(n).sqrt()
#st = str(s)[0] + str(s)[2:101]

#print st
#print len(st)
#print sum([int(x) for x in list(st)])



for n in range(101):

	#s = Decimal(n).sqrt()

	s = Decimal(n).sqrt()
	st = str(s)[0] + str(s)[2:101]

	#print n, s[:10], len(s)
	#s = s[2:]
	#print len(s)
	ad = sum([int(x) for x in list(st)])
	#print s
	print n, ad
	total += ad

print total




