


count = 0


for a in range(2):

	for b in range(3):

		for c in range(5):

			for d in range(11):

				for e in range(21):

					for f in range(41):

						for g in range(101):

							for h in range(201):

								s = (200 * a) + (100 * b) + (50 * c) + (20 * d) + (10 * e) + (5 * f) + (2 * g) + (1 * h)

								if s == 200:

									count += 1

									print [a, b, c, d, e, f, g, h], count

print count
