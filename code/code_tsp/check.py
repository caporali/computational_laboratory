#previene la creazione di cache
import sys
sys.dont_write_bytecode = True


#librerie importate
import numpy as np
import random
import itertools as it


#funzioni importate
from main.input import *
from main.function import *
from main.output import *
from plot.check_plot import *


#controllo attendibilità del random
n = 5

c = np.zeros(n)
for i in range(0, 1000):
	prob = random.randint(0, n - 1)
	c[prob] = c[prob] + 1 

#print([int(i) for i in c.tolist()])


#controllo correttezza del numero di 2-change
n = 50
k = n*(n-3)

c = 0
flag = 0
for alpha in range (0, n):
	if (alpha + 3 >= n):
		for beta in range ((alpha + 3)%n, alpha):
			c = c + 1
	else:
		for beta in it.chain(range (alpha + 3, n), range (0, alpha)):
			c = c + 1

#print(c, " = ", k)


#controllo correttezza della ricostruzione delle 2-change
n = 5
k = n*(n-3)

for prob in range (0, k):
	c = -1
	flag = 0
	for alpha in range (0, n):
		if (alpha + 3 >= n):
			for beta in range ((alpha + 3)%n, alpha):
				c = c + 1
				if c == prob:
					flag = 1
					break
		else:
			for beta in it.chain(range (alpha + 3, n), range (0, alpha)):
				c = c + 1
				if c == prob:
					flag = 1
					break
		if (flag == 1):
			break

	#print("[", alpha, beta, "]")


#controllo correttezza della costruzione delle 2-change
n = 5

k = n*(n - 3)

cities = np.zeros((2, n))

cities[0,0] = 0.31
cities[1,0] = 0

cities[0,1] = 1.31
cities[1,1] = 0

cities[0,2] = 1.62
cities[1,2] = 0.95

cities[0,3] = 0.81
cities[1,3] = 1.54

cities[0,4] = 0
cities[1,4] = 0.95

begin = np.array([0, 1, 2, 3, 4])
label = "start"
route = begin
plot_figure(begin, n, cities, 0, label)

for prob in range (0, k):

	alpha_beta = find_two_change(prob, n)
	alpha = alpha_beta[0]
	beta = alpha_beta[1]

	newroute = build_two_change(route, alpha, beta, n)

	a = str(alpha)
	b = str(beta)
	label = "alpha: " + a + " beta: " + b

	plot_figure(newroute, n, cities, prob + 1, label)
	
plt.show()