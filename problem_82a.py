

s = 3

for i in range(rows):

	minimum_to_right = mat[i][s + 1]

	# Above

	a = mat[i - 1][s]