import numpy as np
import math as mt
import random
import itertools as it


#definisce una matrice delle distanze tra ciascuna coppia di nodi
def distances(n, cities):
	dist = np.zeros((n, n))

	for i in range(0, n):
		for j in range(0, n):
			dist[i, j] = np.sqrt((cities[0, i] - cities[0, j])**2 + (cities[1, i] - cities[1, j])**2)

	return dist


#computa la lunghezza del percorso route
def f(route, n, dist):
	f_route = 0 

	app = int(route[0])
	for i in route[1:]:
		i = int(i)
		f_route += dist[app, i]
		app = i
	f_route += dist[int(route[n - 1]), int(route[0])]

	return f_route


#computa la lunghezza del percorso newroute a partire da route, alpha e beta
def f_short(f_route, route, alpha, beta, n, dist):
	alpha_less = dist[int(route[alpha]), int(route[(alpha + 1)%n])]
	beta_less = dist[int(route[beta]), int(route[(beta - 1)%n])]
	alpha_add = dist[int(route[alpha]), int(route[(beta - 1)%n])]
	beta_add = dist[int(route[beta]), int(route[(alpha + 1)%n])]

	return (f_route - alpha_less - beta_less + alpha_add + beta_add)


#estrae con distribuzione uniforme un valore da 0 a (k - 1)
def probability(k):
	return random.randint(0, k - 1)


#estrae aleatoriamente una 2-change nella neighborhood
def find_two_change(prob, n):
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
			#it.chain() unisce e concatena i due range
			for beta in it.chain(range (alpha + 3, n), range (0, alpha)):	
				c = c + 1
				if c == prob:
					flag = 1
					break
		if (flag == 1):
			break

	return alpha, beta


#costruisce la 2-change estratta aleatoriamente nella funzione precedente
def build_two_change(route, alpha, beta, n):
	newroute = np.zeros((n))

	if (beta >= alpha + 3):
		for i in range (0, alpha + 1):
			newroute[i] = route[i]
		for i in range (alpha + 1, beta):
			newroute[i] = route[beta + alpha - i]
		for i in range (beta, n):
			newroute[i] = route[i]
	elif (beta <= (alpha - 1)):
		for i in range (beta, alpha + 1):
			newroute[i] = route[i]
		for i in range (alpha + 1, n):
			newroute[i] = route[(beta + alpha - i)%n]
		for i in range (0, beta):
			newroute[i] = route[(beta + alpha - i)%n]

	return newroute


#Metropolis con Temperatura 1/sqrt(t)
def function_m1(f_route, f_newroute, t):
	return np.exp((f_route - f_newroute)*np.sqrt(t))


#Metropolis con Temperatura 1/t
def function_m2(f_route, f_newroute, t):
	return np.exp((f_route - f_newroute)*t)


#Metropolis con Temperatura 0.95^t
def function_m3(f_route, f_newroute, t):
	return np.exp((f_route - f_newroute)*((1/(0.95))**t))


#Metropolis
def metropolis(route, f_route, newroute, f_newroute, t, tyt):
	if f_route >= f_newroute:
		route = newroute
		f_route = f_newroute 
	else:
		accept = random.uniform(0, 1)

		if tyt == 0:
			aij_t = function_m1(f_route, f_newroute, t)
		elif tyt == 1:
			aij_t = function_m2(f_route, f_newroute, t)
		elif tyt == 2:
			aij_t = function_m3(f_route, f_newroute, t)

		if accept <= aij_t:
			route = newroute 
			f_route = f_newroute

	return route, f_route


#Barker con Temperatura 1/sqrt(t)
def function_b1(f_route, f_newroute, t):
	return 1/(1 + np.exp(-(f_route - f_newroute)*np.sqrt(t)))


#Barker con Temperatura 1/t
def function_b2(f_route, f_newroute, t):
	return 1/(1 + np.exp(-(f_route - f_newroute)*t))


#Barker con Temperatura 0.95^t
def function_b3(f_route, f_newroute, t):
	return 1/(1 + np.exp(-(f_route - f_newroute)*((1/(0.95))**t)))


#Barker
def barker(route, f_route, newroute, f_newroute, t, tyt):
	#sopprime warning per underflow e overflow (numpy usa 0 e +infty automaticamente) 
	np.seterr(all='ignore')

	accept = random.uniform(0, 1)

	if tyt == 0:
		aij_t = function_b1(f_route, f_newroute, t)
	elif tyt == 1:
		aij_t = function_b2(f_route, f_newroute, t)
	elif tyt == 2:
		aij_t = function_b3(f_route, f_newroute, t)

	if accept <= aij_t:
		route = newroute 
		f_route = f_newroute

	return route, f_route


#Metropolis o Barker
def input_mb(ty, route, f_route, newroute, f_newroute, t, tyt):
	if ty == 0:
		out = metropolis(route, f_route, newroute, f_newroute, t, tyt)
	elif ty == 1:
		out = barker(route, f_route, newroute, f_newroute, t, tyt)

	return out