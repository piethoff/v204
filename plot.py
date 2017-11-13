import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.use('pgf')
mpl.rcParams.update({
    'pgf.preamble': r'\usepackage{siunitx}',
})

data = np.genfromtxt('content/statische_messung.txt', unpack=True)

plt.subplot(1, 2, 1)
plt.plot(5*data[0], data[1], label="Temperatur 1")
plt.plot(5*data[0], data[4], label="Temperatur 4")
plt.xlabel(r'$t / \si{\second}$')
plt.ylabel(r"$T/\si{\celsius}$")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(5*data[0], data[5], label="Temperatur 5")
plt.plot(5*data[0], data[8], label="Temperatur 8")
plt.xlabel(r'$t / \si{\second}$')
plt.ylabel(r"$T/\si{\celsius}$")
plt.legend()
plt.tight_layout()

plt.savefig("build/plot.pdf")
plt.clf()


plt.subplot(1, 2, 1)
plt.plot(5*data[0], data[7]-data[8], label="Edelstahl")
plt.xlabel(r'$t / \si{\second}$')
plt.ylabel(r"$T/\si{\celsius}$")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(5*data[0], data[2]-data[1], label="Messing")
plt.legend()
plt.xlabel(r'$t / \si{\second}$')
plt.ylabel(r"$T/\si{\celsius}$")
plt.tight_layout()

plt.savefig("build/plot2.pdf")
plt.clf()


data = np.genfromtxt('content/dynamische_messung1.txt', unpack=True)
fig = plt.figure()
fig = fig.add_subplot(1,1,1)
plt.plot(2*data[0], data[1], label="Temperatur 1")
plt.plot(2*data[0], data[2], label="Temperatur 2")
plt.ylim(19, 37)
plt.xlabel(r'$t / \si{\second}$')
plt.ylabel(r"$T/\si{\celsius}$")
maj = np.arange(0, 2*data[0][-1], 80)
min = np.arange(0, 2*data[0][-1], 20)
tmaj = np.arange(19, 37, 2)
tmin = np.arange(19, 37, 1)
fig.set_xticks(maj)
fig.set_xticks(min, minor=True)
fig.set_yticks(tmaj)
fig.set_yticks(tmin, minor=True)
fig.grid(which="minor", alpha = 0.3, ls="dashed")
fig.grid(which="major", alpha = 0.6)
plt.legend()
plt.tight_layout()

plt.savefig("build/plot3.pdf")
plt.clf()

fig = plt.figure()
fig = fig.add_subplot(1,1,1)
plt.plot(2*data[0], data[5], label="Temperatur 5")
plt.plot(2*data[0], data[6], label="Temperatur 6")
plt.ylim(19, 37)
plt.xlabel(r'$t / \si{\second}$')
plt.ylabel(r"$T/\si{\celsius}$")
maj = np.arange(0, 2*data[0][-1], 80)
min = np.arange(0, 2*data[0][-1], 20)
tmaj = np.arange(19, 37, 2)
tmin = np.arange(19, 37, 1)
fig.set_xticks(maj)
fig.set_xticks(min, minor=True)
fig.set_yticks(tmaj)
fig.set_yticks(tmin, minor=True)
fig.grid(which="minor", alpha = 0.3, ls="dashed")
fig.grid(which="major", alpha = 0.6)
plt.legend()

plt.savefig("build/plot4.pdf")
plt.clf()


data = np.genfromtxt('content/dynamische_messung2.txt', unpack=True)

fig = plt.figure()
fig = fig.add_subplot(1,1,1)
plt.plot(2*data[0], data[7], label="Temperatur 7")
plt.plot(2*data[0], data[8], label="Temperatur 8")
plt.xlabel(r'$t / \si{\second}$')
plt.ylabel(r"$T/\si{\celsius}$")
plt.ylim(22, 45)
maj = np.arange(0, 2*data[0][-1], 400)
min = np.arange(0, 2*data[0][-1], 100)
tmaj = np.arange(22, 45, 2)
tmin = np.arange(22, 45, 1)
fig.set_xticks(maj)
fig.set_xticks(min, minor=True)
fig.set_yticks(tmaj)
fig.set_yticks(tmin, minor=True)
fig.grid(which="minor", alpha = 0.3, ls="dashed")
fig.grid(which="major", alpha = 0.6)

plt.legend()
plt.tight_layout()

plt.savefig("build/plot5.pdf")
