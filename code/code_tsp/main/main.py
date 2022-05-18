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
from plot.plot import *


#set random
random.seed()


#activate or not
y_n = activate_or_not()

output_costs_flag = y_n[0]
plotfig = y_n[1]
numbers = y_n[2]


#input
inp = input_main()

n = inp[0]
k = inp[1]
cities = inp[2]
begin = inp[3]


#first computation
dist = distances(n, cities)

f_begin = f(begin, n, dist)

route = begin
f_route = f_begin


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
	output_costs[0] = f_route


for t in range(0, it):											

	#seleziona 2-change aleatoriamente
	prob = probability(k)

	#trova la 2-change estratta
	alpha_beta = find_two_change(prob, n)
	alpha = alpha_beta[0]
	beta = alpha_beta[1]

	#costruisce la 2-change estratta
	newroute = build_two_change(route, alpha, beta, n)

	#computa f_newroute
	f_newroute = f_short(f_route, route, alpha, beta, n, dist)

	#esegue scelta in accordo con la catena
	out = input_mb(ty, route, f_route, newroute, f_newroute, t, tyt)

	route = out[0]
	f_route = out[1]


	#y_n (0)
	if output_costs_flag == 1:
		output_costs[t + 1] = f_route

	if t%10000 == 0:
		print("Iteration: " , t)
		print("Time: ", time.time() - tot)

#separa i print delle iterazioni dall'output
print()


#output
text_output(begin, route, f_begin, f_route)


#end-timer
tot = time.time() - tot
print()
print("Time: ", tot)


#plot

#y_n (1)
if plotfig == 1:
	#y_n (1.1)
	plot_figure(begin, n, cities, 0, numbers)													
	plot_figure(route, n, cities, 1, numbers)

if output_costs_flag == 1:
	#y_n (0)
	plot_descent(it + 1, output_costs)

if plotfig == 1 or output_costs_flag == 1:
	plt.show()