def palindrome(s):
	return s == s[::-1]

su = 0

for n in range(1,10000):

	s = str(n)

	for n in range(1,51):

		r_s = s[::-1]

		#print s, r_s

		si = int(s)
		r_si = int(r_s)

		#print si, r_si

		s = str(si + r_si)

		if palindrome(s):

			#print n, si, r_si, s
			
			break

		if n == 50:

			su += 1

print su


