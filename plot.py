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

plt.subplot(1, 2, 1)
plt.plot(data[0], data[7]-data[8], label="Edelstahl")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(data[0], data[2]-data[1], label="Messing")
plt.legend()

plt.tight_layout()

plt.savefig("build/plot2.pdf")
plt.clf()


data = np.genfromtxt('content/dynamische_messung1.txt', unpack=True)

plt.subplot(1, 2, 1)
plt.title("Temperaturverlauf für Messing")
plt.plot(data[0], data[1], label="Temperatur 1")
plt.plot(data[0], data[2], label="Temperatur 2")
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Temperaturverlauf für Aluminium")
plt.plot(data[0], data[5], label="Temperatur 5")
plt.plot(data[0], data[6], label="Temperatur 6")
plt.legend()

plt.tight_layout()

plt.savefig("build/plot3.pdf")
plt.clf()


data = np.genfromtxt('content/dynamische_messung2.txt', unpack=True)

plt.title("Temperaturverlauf für Edelstahl")
plt.plot(data[0], data[7], label="Temperatur 7")
plt.plot(data[0], data[8], label="Temperatur 8")
plt.legend()

plt.savefig("build/plot4.pdf")
