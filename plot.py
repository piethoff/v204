import matplotlib.pyplot as plt
import numpy as np

t, a, b, c, d, e, f, g, h = np.genfromtxt('content/statische_messung.txt', unpack=True)

plt.subplot(1, 2, 1)
plt.plot(t, a, label="Temperatur 1")
plt.plot(t, d, label="Temperatur 4")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t,e, label="Temperatur 5")
plt.plot(t,h, label="Temperatur 8")
plt.legend()

plt.tight_layout()

plt.savefig("build/plot.pdf")
