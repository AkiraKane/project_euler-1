import numpy as np 
import time
'''
a = 1
b = 1
c = 1
d = 1
e = 1
f = 1
g = 1
h = 1
i = 1
'''
#m = [[a, b, c], [d, e, f], [g, h, i]]

#print np.dot(m,m)

def idempotent(m):

	return (np.matrix(m) == (np.dot(m,m))).all()

#print idempotent(m)

for n in range(1,10):
	su = 0



	for a in range(-1 * n, n + 1):
		print 'a', a
		
		for b in range(-1 * n, n + 1):
			#print 'b', b
			for c in range(-1 * n, n + 1):
				#print 'c', c
				for d in range(-1 * n, n + 1):
					for e in range(-1 * n, n + 1):
						for f in range(-1 * n, n + 1):
							#for g in range(-1 * n, n + 1):
							#start = time.time()

							for h in range(-1 * n, n + 1):
								for i in range(-1 * n, n + 1):

									try:
										g = c*d*h/b*f
									except:
										continue
									
									m = [[a, b, c], [d, e, f], [g, h, i]]

									if idempotent(m):
										su += 1

							#end = time.time()
							#print end - start


		

		
	print n, su