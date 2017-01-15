nums = []

for a in range(2,101):

	for b in range(2,101):

		z = a**b

		if z not in nums:

			nums.append(z)

print len(nums)

