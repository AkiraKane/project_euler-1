# PE Problem 9: find a, b, c such that a**2 + b**2 = c**2 and a+b+c=1000

import math

squares = [x**2 for x in range(1000)]

for c in squares[::-1]:

	for b in squares[::-1]:

		for a in squares:

			if a + b == c:

				if math.sqrt(a) + math.sqrt(b) + math.sqrt(c) == 1000:

					print math.sqrt(a*b*c)

					print math.sqrt(a), math.sqrt(b), math.sqrt(c)