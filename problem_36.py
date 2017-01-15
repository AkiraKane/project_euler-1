

def palindrome(s):

	return s == s[::-1]


su = 0

for i in range(1,1000000):

	if palindrome(str(i)) and palindrome(bin(i)[2:]):

		print i, bin(i)[2:]
		su += i

print su

