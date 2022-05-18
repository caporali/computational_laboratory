import numpy as np
import random


#input 5x5
def input_1():
	#definizione di n per Lambda_n
	n = int(input("Insert n for size of lattice (-n, n): "))

	sigma = np.zeros((2*n + 1, 2*n + 1))

	for i in range(0, 2*n + 1):
		for j in range(0, 2*n + 1):
			sigma[i,j] = random.choices([-1, 1])[0]

	return sigma, n


#input activate or not
def activate_or_not():
	print("Activate or not:")
	output_costs_flag = int(input("	0. Record costs during iterations and plot descent: "))
	plotfig = int(input("	1. Figure plot (possible only if n <= 20): "))
	if plotfig == 1:
		edges = int(input("		1.1. Plot edges (possible only if n <= 5): "))
	else:
		edges = 0

	print()

	return output_costs_flag, plotfig, edges


#input principale
def input_main():
	print("Insert scenario:")
	print("	0. Random scenario")

	scenario = int(input("	Scenario: "))

	print()

	if scenario == 0:
		inp = input_1()

	return inp


#input tipologia iterazioni
def input_iteration():
	it = int(input("Insert number of iterations: "))

	print("Insert type of iterations: ")
	print("	0. Metropolis")
	print("	1. Barker")

	ty = int(input("	Type: "))

	print("	Insert type of cooling schedule: ")
	print("		0. T(t) = 1/sqrt(t)")
	print("		1. T(t) = 1/t")
	print("		2. T(t) = (0.95)^t")

	tyt = int(input("		Temperature: "))

	print()
	
	return it, ty, tyt