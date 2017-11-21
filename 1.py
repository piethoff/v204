import numpy as np

data = np.genfromtxt("content/dynamische_messung2.txt", unpack=True)

data[0] = data[0]*2

extr1 = []
time1 = []
extr2 = []
time2 = []

#Datenreihen
data1 = 7
data2 = 8
th = 0

def mean(a):
    sum = 0
    for i in a:
        sum += i
    sum = sum/len(a)
    return sum

def var(a):
    mean2 = mean(a)
    sum = 0
    for i in a:
        sum += (i-mean2)**2
    sum = sum/len(a)
    sum = sum/(len(a) - 1)
    return np.sqrt(sum)


pos = False
for i in range(len(data[data1])-2):
    if pos:
        if data[data1][i] < data[data1][i+1]-th:
            extr1.append(data[data1][i])
            time1.append(data[0][i])
            pos = False
    else:
        if data[data1][i] > data[data1][i+1]+th:
            extr1.append(data[data1][i])
            time1.append(data[0][i])
            pos = True
#print("Extr1: \n", np.array(extr1))

#print("Amp1: \n", np.array(amp1))


pos = False
for i in range(len(data[data2])-2):
    if pos:
        if data[data2][i] < data[data2][i+1]-th:
            extr2.append(data[data2][i])
            time2.append(data[0][i])
            pos = False
    else:
        if data[data2][i] > data[data2][i+1]+th:
            extr2.append(data[data2][i])
            time2.append(data[0][i])
            pos = True

#print("Extr2: \n", np.array(extr2))

#print("Amp2: \n", np.array(amp2))

#print("Time1: \n", np.array(time1))
#print("Time2: \n", np.array(time2))

#print("T: \n", np.array(t))


data = np.genfromtxt("content/ablesen.txt", unpack=True)
data2 = np.genfromtxt("content/ablesen2.txt", unpack=True)

amp = [[], [], [], [], [], []]

for i in range(0, 4):
    for j in range(data[2*i].size-1):
        amp[i].append((np.abs(data[2*i][j] - data[2*i][j+1]))/2)
for i in range(0, 2):
    for j in range(data2[2*i].size-1):
        amp[i+4].append((np.abs(data2[2*i][j] - data2[2*i][j+1]))/2)
#print(amp)

t = [[], [], []]
for i in range(0, 2):
    for j in range(data[4*i+1].size):
        t[i].append(np.abs(data[4*i+1][j] - data[4*i+3][j]))
for i in range(0, 1):
    for j in range(data2[4*i+1].size):
        t[i+2].append(np.abs(data2[4*i+1][j] - data2[4*i+3][j]))
#print(t)

print("Amplitudes(1, 2, 5, 6, 7, 8): ")
for i in amp:
    print(mean(i), "+/-", var(i))

print("Mean DT(1/2, 5/6, 7/8): ")
for i in t:
    print(mean(i), "+/-", var(i))


#Amplitudes(1, 2, 5, 6, 7, 8):
#0.483421052632 +/- 0.0689033273027
#1.54578947368 +/- 0.0664307923277
#0.896578947368 +/- 0.0741748493728
#1.88736842105 +/- 0.0715853970262
#3.80433333333 +/- 0.0999331522601
#0.905666666667 +/- 0.094626919892
#Mean DT(1/2, 5/6, 7/8):
#13.5 +/- 1.23863252271
#6.9 +/- 0.469602295341
#47.75 +/- 2.28673712234

