

a = [2, 5]
#b = [1, 2]

su = 0

for i in range(1000):

	denominator = 2 * a[-1] + a[-2]

	new_second_half = a[-1]

	a.append(denominator)

	numerator = denominator + new_second_half

	#rint numerator, '/', denominator

	if len(str(numerator)) > len(str(denominator)):

		su+= 1

print su
	