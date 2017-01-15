# PE Problem 26: Find the value of d < 1000 for 1/d contains the longest recurring cycle in its decimal fraction

from decimal import *

getcontext().prec = 2000

def fractioner(d):

	return str(Decimal(1)/Decimal(d))

def principal_period(s):
    i = (s+s).find(s, 1, -1)
    return None if i == -1 else s[:i]

#for i in range(1,1000):

#	print i, fractioner(i)

#window = 7

def screen(s):

	for i in range(5):

		segment = s[i:i + window]

		#print segment, s[i+window:i+2*window]

		if s[i+window:i+2*window] == segment:

			#print 'REPEAT!', window

			return True
'''
max_window = 984

for d in range(1,1000):

	st = fractioner(d)

	#print st
	#print len(st)

	if len(st) > 20:

		for w in range(10,2000):

			window = w

			if screen(st) and window < max_window:

				break

				#print "Repeat found, d:", d, "w:", window

			if screen(st):

				#print st

				print "Repeat found, d:", d, "w:", window

				max_window = window


'''


s = fractioner(983)

print s[4:986]

print ""

print s[986:2*986]

#print principal_period('7142857142857142850000')