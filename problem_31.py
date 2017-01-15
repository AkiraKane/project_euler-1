from math import ceil

combos = 0

for a in range(3):

	for b in range(2 - (2 * a) + 3):

		for c in range(4 - (2 * b) + 3):

			for d in range(10 + 2 - int(ceil(2.5 * c))):

				#print d

				for e in range(20 + 3 - (2 * d)):

					for f in range(40 + 3 - (2 * e)):

						for g in range(100 + 3 - int(ceil(2.5 * f))):

							for h in range(200 + 3 - (2 * g)):

								total = (a * 2) + (b * 1) + (c * 0.5) + (d * 0.2) + (e * 0.1) + (f * 0.05) + (g * 0.02) + (h * 0.01)

								if total == 2:

									combos += 1

									print [a, b, c, d, e, f, g, h], combos

									#break


print combos