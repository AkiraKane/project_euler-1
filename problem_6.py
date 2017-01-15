# PE Problem 6: Find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum

def sum_of_the_squares(x):

	su = 0

	for i in range(x):

		su += (i+1)**2

	return su

def square_of_the_sum(x):

	su = 0

	for i in range(x):

		su += (i+1)

	return su**2

a = sum_of_the_squares(100)
b =  square_of_the_sum(100)
print b - a

