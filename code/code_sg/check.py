#previene creazione di cache
import sys
sys.dont_write_bytecode = True

import os
import numpy as np
import random


#set random
random.seed()


#risoluzione del problema np.matrix è un puntatore
def input_1():
	#definizione di n per Lambda_n
	n = 1

	sigma = np.zeros((2*n + 1, 2*n + 1))

	for i in range(0, 2*n + 1):
		for j in range(0, 2*n + 1):
			sigma[i,j] = random.choices([-1, 1])[0]

	return sigma, n


#input
inp = input_1()

begin = inp[0]
n = inp[1]

print("begin: ", begin)


sigma_0 = np.matrix(begin)
sigma_0[0,0] = -10

print("begin: ", begin)