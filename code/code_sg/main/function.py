import numpy as np
import math as mt
import random
import itertools as it


#computa l'energia di sigma
def H(sigma, n, J_0, J_1):
	H_sigma = 0

	#aggiungo contributo di archi orizzontali (identificati con 0)
	#i mi dice la riga in cui si trova l'arco, j il nodo da cui parte (sulla riga, da sx verso dx)
	#la componente i denota le y, la j le x (si vede nel plot)
	for i in range(0, 2*n + 1):
		for j in range(0, 2*n):
			H_sigma += 	J_0[i, j]*sigma[i, j]*sigma[i, j + 1]

	#aggiungo contributo di archi verticali (identificati con 1)
	#j mi dice la colonna in cui si trova l'arco, i il nodo da cui parte (sulla colonna, dall'up verso il down)
	#la componente i denota le y, la j le x (si vede nel plot)
	for j in range(0, 2*n + 1):
		for i in range(0, 2*n):
			H_sigma += 	J_1[i, j]*sigma[i, j]*sigma[i + 1, j]

	return H_sigma


#computa l'energia di sigma_1 sapendo quella di sigma_0
def H_short(sigma_0, H_sigma_0, line, column, n, J_0, J_1):
	H_sigma_1 = H_sigma_0

	if (line != 0):
		H_sigma_1 += -2*J_1[line - 1, column]*sigma_0[line - 1, column]*sigma_0[line, column]
	if (line != 2*n):
		H_sigma_1 += -2*J_1[line, column]*sigma_0[line, column]*sigma_0[line + 1, column]
	if (column != 0):
		H_sigma_1 += -2*J_0[line, column - 1]*sigma_0[line, column - 1]*sigma_0[line, column]
	if (column != 2*n):
		H_sigma_1 += -2*J_0[line, column]*sigma_0[line, column]*sigma_0[line, column + 1]

	return H_sigma_1


#computo di J
def J(n):
	J_0  = np.zeros((2*n + 1, 2*n))

	for i in range(0, 2*n + 1):
		for j in range(0, 2*n):
			J_0[i, j] = random.choices([-1, 1])[0]

	J_1  = np.zeros((2*n, 2*n + 1))

	for i in range(0, 2*n):
		for j in range(0, 2*n + 1):
			J_1[i, j] = random.choices([-1, 1])[0]

	return J_0, J_1


#estrae con distribuzione uniforme un valore da 0 a 2*n
def probability(n):
	line = random.randint(0, 2*n)
	column = random.randint(0, 2*n)

	return line, column

#Metropolis con Temperatura 1/sqrt(t)
def function_m1(H_sigma_0, H_sigma_1, t):
	return np.exp((H_sigma_0 - H_sigma_1)*np.sqrt(t))


#Metropolis con Temperatura 1/t
def function_m2(H_sigma_0, H_sigma_1, t):
	return np.exp((H_sigma_0 - H_sigma_1)*t)


#Metropolis con Temperatura 0.95^t
def function_m3(H_sigma_0, H_sigma_1, t):
	return np.exp((H_sigma_0 - H_sigma_1)*((1/(0.95))**t))


#Metropolis
def metropolis(sigma_0, H_sigma_0, sigma_1, H_sigma_1, t, tyt):
	if H_sigma_0 >= H_sigma_1:
		sigma_0 = sigma_1
		H_sigma_0 = H_sigma_1 
	else:
		accept = random.uniform(0, 1)

		if tyt == 0:
			aij_t = function_m1(H_sigma_0, H_sigma_1, t)
		elif tyt == 1:
			aij_t = function_m2(H_sigma_0, H_sigma_1, t)
		elif tyt == 2:
			aij_t = function_m3(H_sigma_0, H_sigma_1, t)

		if accept <= aij_t:
			sigma_0 = sigma_1 
			H_sigma_0 = H_sigma_1

	return sigma_0, H_sigma_0


#Barker con Temperatura 1/sqrt(t)
def function_b1(H_sigma_0, H_sigma_1, t):
	return 1/(1 + np.exp(-(H_sigma_0 - H_sigma_1)*np.sqrt(t)))


#Barker con Temperatura 1/t
def function_b2(H_sigma_0, H_sigma_1, t):
	return 1/(1 + np.exp(-(H_sigma_0 - H_sigma_1)*t))


#Barker con Temperatura 0.95^t
def function_b3(H_sigma_0, H_sigma_1, t):
	return 1/(1 + np.exp(-(H_sigma_0 - H_sigma_1)*((1/(0.95))**t)))


#Barker
def barker(sigma_0, H_sigma_0, sigma_1, H_sigma_1, t, tyt):
	#sopprime warning per underflow e overflow (numpy usa 0 e +infty automaticamente) 
	np.seterr(all='ignore')

	accept = random.uniform(0, 1)

	if tyt == 0:
		aij_t = function_b1(H_sigma_0, H_sigma_1, t)
	elif tyt == 1:
		aij_t = function_b2(H_sigma_0, H_sigma_1, t)
	elif tyt == 2:
		aij_t = function_b3(H_sigma_0, H_sigma_1, t)

	if accept <= aij_t:
		sigma_0 = sigma_1 
		H_sigma_0 = H_sigma_1

	return sigma_0, H_sigma_0


#Metropolis o Barker
def input_mb(ty, sigma_0, H_sigma_0, sigma_1, H_sigma_1, t, tyt):
	if ty == 0:
		out = metropolis(sigma_0, H_sigma_0, sigma_1, H_sigma_1, t, tyt)
	elif ty == 1:
		out = barker(sigma_0, H_sigma_0, sigma_1, H_sigma_1, t, tyt)

	return out