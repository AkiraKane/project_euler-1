
from num2words import num2words

def strip(s):

	s = s.replace(" ", "")

	s = s.replace("-", "")

	return s

su = 0

for i in range(1,1001):

	su += len(strip(num2words(i)))

print i
print su