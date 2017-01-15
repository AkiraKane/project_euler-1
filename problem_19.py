# How many sundays fell on the first of the month from 1/1/1901 to 12/31/2000

year = 1901

sunday_first = 0

weekday = 1

for y in range(year,2001):

	leap = (y%4 == 0 and not y%400 == 0)

	if leap:

		feb = 29

	else:

		feb = 28

	months = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	for m in months:

		for d in range(m):

			weekday += 1



			if weekday == 7:

				weekday = 0

			#print year, m, d, weekday

			if d == 0 and weekday == 0:

				sunday_first += 1

	'''			
	if leap:
		print y, months, 'leap!'
	else:
		print y, months
	'''
	
print sunday_first