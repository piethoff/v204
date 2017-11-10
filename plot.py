import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('content/statische_messung.txt', unpack=True)

plt.subplot(1, 2, 1)
plt.plot(data[0], data[1], label="Temperatur 1")
plt.plot(data[0], data[4], label="Temperatur 4")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(data[0], data[5], label="Temperatur 5")
plt.plot(data[0], data[8], label="Temperatur 8")
plt.legend()

plt.tight_layout()

plt.savefig("build/plot.pdf")
plt.clf()

#data = np.genfromtxt('content/dynamische_messung1.txt', unpack=True)
#data = np.genfromtxt('content/dynamische_messung2.txt', unpack=True)


