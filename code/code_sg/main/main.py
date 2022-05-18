#previene creazione di cache
import sys
sys.dont_write_bytecode = True

import os
import numpy as np
import random

#funzioni importate
from input import *
from function import *
from output import *
#parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))	
from plot.plot import*


#set random
random.seed()


#activate or not
y_n = activate_or_not()

output_costs_flag = y_n[0]
plotfig = y_n[1]
edges = y_n[2]


#input
inp = input_main()

begin = inp[0]
n = inp[1]


#computation of J
computation = J(n)

J_0 = computation[0]
J_1 = computation[1]


#first computation
H_begin = H(begin, n, J_0, J_1)

#viene fatto np.matrix(begin) altrimenti l'assegnazione sarebbe
#eseguita come puntatore e avrei delle modifiche di begin ogni qual volta
#modifico sigma_0 (anche dopo)
sigma_0 = np.matrix(begin)
H_sigma_0 = H_begin


#iteration
it_type = input_iteration()

it = it_type[0]
ty = it_type[1]
tyt = it_type[2]


#start-timer
import time
tot = time.time()


#y_n (0)
if output_costs_flag == 1:
	output_costs = np.zeros(it + 1)
	output_costs[0] = H_sigma_0


for t in range(0, it):											

	#seleziona neighbor aleatoriamente
	prob = probability(n)

	line = prob[0]
	column = prob[1]

	sigma_1 = np.matrix(sigma_0)
	sigma_1[line, column] = -sigma_0[line, column]

	H_sigma_1 = H_short(sigma_0, H_sigma_0, line, column, n, J_0, J_1)

	#esegue scelta in accordo con la catena
	out = input_mb(ty, sigma_0, H_sigma_0, sigma_1, H_sigma_1, t, tyt)

	sigma_0 = np.matrix(out[0])
	H_sigma_0 = out[1]


	#y_n (0)
	if output_costs_flag == 1:
		output_costs[t + 1] = H_sigma_0


#output
text_output(sigma_0, H_sigma_0, begin, H_begin, J_0, J_1)


#end-timer
tot = time.time() - tot
print()
print("Time: ", tot)


#plot

if n >= 21:
	plotfig = 0

if n >= 6:
	edges = 0

if plotfig == 1:
	#y_n (1)
	plot_figure(begin, n, 0)
	plot_figure(sigma_0, n, 1)

	if edges == 1:
		#y_n (1.1)
		plot_edges(J_0, J_1, n, 2)

if output_costs_flag == 1:
	#y_n (0)
	plot_descent(it + 1, output_costs)

if plotfig == 1 or output_costs_flag == 1:
	plt.show()