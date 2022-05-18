import matplotlib.pyplot as plt
import numpy as np

#suppress warning
import warnings
warnings.filterwarnings("ignore")


#font matplotlib
plt.rcParams["font.weight"] = "bold"
plt.rcParams["font.sans-serif"] = "Courier New"
plt.rcParams.update({"font.size": 6})
plt.rcParams["axes.axisbelow"] = True


#plot della configurazione
def plot_figure(sigma, n, index):
	fig = plt.figure(index)

	#dimensione dei punti
	size = -4.5*n + 104.5

	#plot punti
	for i in range(0, 2*n + 1):
		for j in range(0, 2*n + 1):
			#la coppia (i,j) nella matrice della configuraizone
			#identifica in Lambda_n il punto (j - n, n - i)
			if sigma[i,j] == 1:
				plt.scatter(j - n, n - i, c= "k", s = size)
			else:
				plt.scatter(j - n, n - i, edgecolors= "k", s = size, facecolors = "none")

	#plot extra settings
	plt.grid()
	v = np.arange(-n, n + 1)
	plt.yticks(v)
	plt.xticks(v)

	plt.axis([-n - 1, n + 1, -n - 1, n + 1])

	ax = fig.add_subplot(111)
	ax.spines["bottom"].set_color("gray")
	ax.spines["top"].set_color("gray")
	ax.spines["right"].set_color("gray")
	ax.spines["left"].set_color("gray")
	ax.xaxis.label.set_color("gray")
	ax.tick_params(axis="x", colors="gray")
	ax.yaxis.label.set_color("gray")
	ax.tick_params(axis="y", colors="gray")

	if n >= 16:
		ax.set_yticklabels([])
		ax.set_xticklabels([])

	plt.gca().set_aspect("equal", adjustable = "box")


#plot della struttura degli archi
def plot_edges(J_0, J_1, n, index):
	fig = plt.figure(index)

	#set linewidth
	lw = 1.5

	#plot archi orizzontali
	for i in range(0, 2*n + 1):
		for j in range(0, 2*n):
			if J_0[i,j] == 1:
				plt.plot([j - n, j - n + 1], [n - i, n - i], "gray", linestyle = "-", linewidth = lw)
			else:
				plt.plot([j - n, j - n + 1], [n - i, n - i], "gray", linestyle = "--", linewidth = lw)

	#plot archi verticali
	for j in range(0, 2*n + 1):
		for i in range(0, 2*n):
			if J_1[i,j] == 1:
				plt.plot([j - n, j - n], [n - i, n - i - 1], "gray", linestyle = "-", linewidth = lw)
			else:
				plt.plot([j - n, j - n], [n - i, n - i - 1], "gray", linestyle = "--", linewidth = lw)

	#plot nodi 
	for i in range(0, 2*n + 1):
		for j in range(0, 2*n + 1):
			plt.scatter(j - n, n - i, edgecolors = "k", s = 7, facecolors = "none")

	#plot extra settings
	plt.grid()
	v = np.arange(-n, n + 1)
	plt.yticks(v)
	plt.xticks(v)

	plt.axis([-n - 1, n + 1, -n - 1, n + 1])

	ax = fig.add_subplot(111)
	ax.spines["bottom"].set_color("gray")
	ax.spines["top"].set_color("gray")
	ax.spines["right"].set_color("gray")
	ax.spines["left"].set_color("gray")
	ax.xaxis.label.set_color("gray")
	ax.tick_params(axis="x", colors="gray")
	ax.yaxis.label.set_color("gray")
	ax.tick_params(axis="y", colors="gray")

	if n >= 16:
		ax.set_yticklabels([])
		ax.set_xticklabels([])

	plt.gca().set_aspect("equal", adjustable = "box")


#plot discesa
def plot_descent(iteration, output_costs):
	plt.figure(-1)

	time = np.arange(iteration)
	plt.plot(time, output_costs, "gray", linewidth = 1)

	plt.xlabel("t (time)")
	plt.ylabel("H(sigma(t)) (energy of the configuration)")