# PE Problem 15: Longest collatz path starting less than one million

def collatz(z):

	nums = [z]

	while nums[-1] != 1:

		if nums[-1]%2 == 0:

			nums.append(nums[-1]/2)

		else:

			nums.append(3*nums[-1] + 1)

	return nums

max_collatz = [16, 8, 4, 2, 1]

for i in range(1000000,1,-1):

	max_len = len(max_collatz)

	if i not in max_collatz:

		col_path = collatz(i)

		leng = len(col_path)

		if leng > max_len:

			print 'new longest collatz!'

			#print col_path
			print 'i:', i, 'length:', leng
			#print leng

			max_collatz = col_path





