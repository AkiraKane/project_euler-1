
def right_tri(a,b,c,p):

	return (a+b+c == p) and ((a**2) + (b**2) == (c**2))


max_solutions = 1

for p in range(400,1001):

	if p%10==0:
		print p

	solutions = []

	for a in range(1,p):

		for b in range(1,a):

			for c in range(1,p - a - b + 1):

				if right_tri(a,b,c,p):

					sol = [a,b,c]
					sol.sort()

					if sol not in solutions:

						solutions.append(sol)

	if len(solutions) > max_solutions:

		print p, len(solutions), solutions
		max_solutions = len(solutions)



