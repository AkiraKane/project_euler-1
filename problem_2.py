# PE Problem 2: sum of even fibonacci numbers below 4 million

f = [1, 2]

while f[-1] < 4000001:

	f.append(f[-1] + f[-2])

f.pop()

su = 0

for n in f:

	if n%2 == 0:

		su += n

print su