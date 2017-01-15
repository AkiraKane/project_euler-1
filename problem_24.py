from math import factorial as f 

targ = 1000000

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sorted_digits = []
'''
for n in range(1,10):

	s = f(10 - n)

	ind = targ/s

	targ -= s*ind

	sorted_digits.append(nums.pop(ind))

	print sorted_digits
	print nums

'''

test = [2,1,3]

from itertools import permutations as p 

#print len(list(p(nums,10)))

z = list(p(nums,10))
#print z
z.sort()
print z[targ-1]


