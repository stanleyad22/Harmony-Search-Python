import math
import random
import numpy as np
import pandas as pd

HM = 10
hmcr = 0.7
PAR = 0.3
bandwidth = 0.5
pratice = 1000
ukuran_populasi = 10
populasiX = []
populasiY = []
fitness = []
xNew = 0
yNew = 0

xl = -3.0
xu = 12.1

yl = 4.1
yu = 5.8

hasilSemuaIterasi = pd.DataFrame({'X' : np.array([]),
                                    'Y': np.array([]),
                                  'Fitness': np.array([])})

def hitungFitness(x,y):
    return 21.5 + (x * math.sin(4 * math.pi * x)) + (y * math.sin(20 * math.pi * y))

# inisialisasi
for i in range(ukuran_populasi):
    populasiX.append(random.uniform(xl, xu))
    populasiY.append(random.uniform(yl, yu))

for i in range(ukuran_populasi):
    fitness.append(hitungFitness(populasiX[i], populasiY[i]))

for i in range(pratice):
    rand = random.random()
    if rand <= hmcr:
        Xold = random.randrange(1, ukuran_populasi)
        rand2 = random.random()
        if rand2 <= PAR:
            xNew = populasiX[Xold] - bandwidth if random.random() > 0.5 else populasiX[Xold] + bandwidth
            if xNew <= xl:
                xNew = xl
            elif xNew > xu:
                xNew = xu
        else:
            xNew = xl + (random.random() *(xu - xl))

    rand = random.random()
    if rand <= hmcr:
        Yold = random.randrange(1, ukuran_populasi)
        rand2 = random.random()
        if rand2 <= PAR:
            yNew = populasiX[Yold] - bandwidth if random.random() > 0.5 else populasiX[Yold] + bandwidth
            if yNew <= yl:
                yNew = yl
            elif yNew > yu:
                yNew = yu
        else:
            yNew = yl + (random.random() * (yu - yl))

    if hitungFitness(xNew, yNew) < min(fitness):
        populasiX[fitness.index(min(fitness))] = xNew
        populasiY[fitness.index(min(fitness))] = yNew
        fitness[fitness.index(min(fitness))] = hitungFitness(xNew, yNew)

    for i in range(len(populasiX)):
        hasilSemuaIterasi.loc[i, 'x'] = populasiX[i]
        hasilSemuaIterasi.loc[i, 'y'] = populasiY[i]
        hasilSemuaIterasi.loc[i, 'Fitness'] = fitness[i]

hasilSemuaIterasi
