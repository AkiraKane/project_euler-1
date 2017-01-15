# PE Problem 4: Find the largest palindrome made from the product of two 3-digit numbers

def is_palindrome(x):

	s = str(x)

	#print s, s[::-1]

	return s == s[::-1]

#print is_palindrome(555494945551)

#print is_palindrome(71799717)

largest_pal = 0

for x in xrange(999,100,-1):

	for y in xrange(999,100,-1):

		z = x*y

		if is_palindrome(z) and z > largest_pal:

			print x, y
			largest_pal = z

print largest_pal
			