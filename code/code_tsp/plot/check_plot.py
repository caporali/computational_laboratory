import matplotlib.pyplot as plt
import numpy as np


#font matplotlib
plt.rcParams["font.weight"] = "bold"
plt.rcParams["font.sans-serif"] = "Courier New"
plt.rcParams.update({"font.size": 9})
plt.rcParams["axes.axisbelow"] = True


#plot del grafo
def plot_figure(route, n, cities, index, title):
	plt.figure(index)

	#plot segmenti
	app = int(route[0])
	for i in route[1:]:
		i = int(i)
		plt.plot([cities[0, app], cities[0, i]], [cities[1, app], cities[1, i]], "gray", linewidth = 0.8)
		app = i
	plt.plot([cities[0, int(route[n - 1])], cities[0, int(route[0])]], [cities[1, int(route[n - 1])], cities[1, int(route[0])]], "gray", linewidth = 0.8)

	#plot punti
	plt.scatter(cities[0, :], cities[1, :], c = "k", s = 6)
	
	number = 0
	for x, y in zip(cities[0, :], cities[1, :]):
		label = f"{number}"
		plt.annotate(label, (x, y), textcoords = "offset points", xytext = (0,5), ha = "left")
		number += 1
    
    #plot extra settings
	plt.axis("off")		
	plt.gca().set_aspect("equal", adjustable = "box")

	#label
	plt.title(title + "\n \n", fontsize = 11, fontweight = "bold")