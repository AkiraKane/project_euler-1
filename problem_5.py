# PE Problem 5: Smallest positive number evenly divisible by all numbers from 1 to 20
import numpy as np




z = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

factors = []

for n in z:

	factors.append(n)

	for j in range(len(z)):

		if z[j]%n == 0:

			z[j] = z[j]/n

		else:

			z[j] = z[j]

	print factors
	#print z

print np.prod(factors)






