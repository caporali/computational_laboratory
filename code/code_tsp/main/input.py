import numpy as np
import random


#input ottagono
def input_1():
	#numero di nodi
	n = 8
	#numero di  2-change
	k = n*(n - 3)

	cities = np.zeros((2, n))

	cities[0,0] = 1
	cities[1,0] = 0

	cities[0,1] = 2
	cities[1,1] = 0

	cities[0,2] = 3
	cities[1,2] = 1

	cities[0,3] = 3
	cities[1,3] = 2

	cities[0,4] = 2
	cities[1,4] = 3

	cities[0,5] = 1
	cities[1,5] = 3

	cities[0,6] = 0
	cities[1,6] = 2

	cities[0,7] = 0
	cities[1,7] = 1

	begin = start_route_1()		

	return n, k, cities, begin

def start_route_1():
	#percorso iniziale
	#route = np.array([0, 1, 2, 3, 4, 5, 6, 7])
	route = np.array([0, 3, 6, 1, 4, 7, 2, 5])

	return route


def input_2():
	n = 50
	k = n*(n - 3)

	cities = np.zeros((2, n))
	
	cities[0, :] = [17, 23, 8, 44, 39, 11, 11, 3, 19, 49, 3, 33, 34, 45, 30, 11, 5, 16, 36, 21, 36, 23, 3, 16, 42, 6, 3, 37, 39, 34, 22, 11, 37, 11, 45, 3, 27, 46, 25, 3, 22, 29, 50, 36, 41, 33, 47, 17, 10, 0]
	cities[1, :] = [28, 26, 28, 19, 24, 30, 6, 48, 28, 3, 20, 3, 41, 45, 36, 8, 29, 22, 22, 30, 14, 34, 3, 41, 37, 46, 22, 25, 35, 40, 31, 19, 16, 7, 20, 4, 34, 42, 3, 17, 41, 42, 42, 40, 45, 21, 44, 27, 31, 25]

	begin = start_route_2()		

	return n, k, cities, begin

def start_route_2():
	route = np.arange(50)

	return route


#input generato automaticamente
def input_ag():
	n = int(input("Insert number of cities: "))
	
	k = n*(n - 3)		
	cities = np.zeros((2, n))

	for i in range(0, n):
		cities[0, i] = random.randint(0, n)
		cities[1, i] = random.randint(0, n)

	begin = start_route_ag(n)		

	return n, k, cities, begin

def start_route_ag(n):
	route = np.arange(n)

	return route


#input activate or not
def activate_or_not():
	print("Activate or not:")
	output_costs_flag = int(input("	0. Record costs during iterations and plot descent: "))
	plotfig = int(input("	1. Figure plot: "))
	if plotfig == 1:
		numbers = int(input("		1.1. Write numbers in figure plot: "))
	else:
		numbers = 0

	print()

	return output_costs_flag, plotfig, numbers


#input principale
def input_main():
	print("Insert scenario:")
	print("	0. Random scenario")
	print("	1. Octagon")
	print("	2. 50 fixed points")

	scenario = int(input("	Scenario: "))

	print()

	if scenario == 0:
		inp = input_ag()
	elif scenario == 1:
		inp = input_1()
	elif scenario == 2:
		inp = input_2()

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