

b = [15, 85, 493, 2871, 16731]
n = [21, 120, 697, 4060, 23661]

r = []

while n[-1] < 1000000000000:

	r.append(b[-1] + n[-1] - 1)

	new_b = range(int(5.828 * b[-1]), int(5.829 * b[-1]))

	for bd in new_b:

		new = r[-1] + bd

		s = (float(bd) * (bd - 1))/(new * (new - 1))

		if s == 0.5:

			print r[-1], bd, new
			b.append(bd)
			n.append(new)

			break

			

print b
print n
print r
