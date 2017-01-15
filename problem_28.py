

dim = 1001

steps = (dim - 1)/2

nums = [1]

for s in range(1, steps + 1):

	inc = s * 2

	for i in range(4):

		nums.append(nums[-1] + inc)

#print nums
print sum(nums)

