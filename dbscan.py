import matplotlib.pyplot as plt
import numpy as np
from means import dist


n = 500
eps, minPts = 5, 3

# точки
x = [np.random.randint(1, 100) for i in range(n)]
y = [np.random.randint(1, 100) for i in range(n)]

# каждой точке соспоставляется флаг g, y или r
flags = []

# Для каждой точки смотрим кол-во соседей перебором остальных точек.
# Если кол-во соседей >= minPts, даем зеленый флаг, иначе красный.
for i in range(0, n):
    neighb = -1
    for j in range(0, n):
        if dist(x[i], y[i], x[j], y[j]) <= eps:
            neighb += 1
    if neighb >= minPts:
        flags.append('g')
    else:
        flags.append('r')

# Для каждой красной точки ищем хотябы одного соседа с зеленым флагом.
# Если такой есть, ставим точке желтый флаг.
for i in range(0, n):
    if flags[i] == 'r':
        for j in range(0, n):
            if flags[j] == 'g':
                if dist(x[i], y[i], x[j], y[j]) <= eps:
                    flags[i] = 'y'

# Изображение разукрашивания
for i in range(0, n):
    plt.scatter(x[i], y[i], color=flags[i])
plt.show()

# Класетеризуем зеленые точки
clust = [-1] * n
# список посещения точек. 0 - не посещенная, 1 - посещенная
is_visited = [0] * n
clust_num = 0

for i in range(n):
    # Пропускаем не зеленые точки
    if flags[i] != 'g':
        continue
    for j in range(n):
        # Сразу пропускаем далеких соседей
        if dist(x[i], y[i], x[j], y[j]) > eps:
            continue
        # Втсречаем зеленую точку соседа
        if flags[j] == 'g':
            # Если обе точки еще не посещенные, даем им один кластер
            if clust[i] == -1 and clust[i] == -1:
                clust[i] = clust[j] = clust_num
            # Если одна точка не посещена, даем ей кластер соседа
            elif clust[i] != -1 and clust[i] == -1:
                clust[i] = clust[j]
            elif clust[i] == -1 and clust[j] != -1:
                clust[j] = clust[i]
            # Если обе точки уже имеют номер кластера, значит нужно определяться.
            # Дадим точке тот кластер, который меньше по номеру.
            else:
                if (clust[i] < clust[j]):
                    clust[j] = clust[i]
                else:
                    clust[i] = clust[j]
        # Если встретилась желтая сосдедка и кластер у точки не опеределен, значит дошли до момента,
        # когда нужно окончательно давать номер кластеру.
        elif flags[j] == 'y' and clust[i] == -1:
            if clust[i] == -1:
                clust[i] = clust_num
                clust_num += 1

# Решаем вопрос с желтыми флажками. Нужно выбрать, к какому кластеру они относяться.
# Находим первого ближайшего соседа с зеленым флагом и даем точке кластер этого соседа.
for i in range(0, n):
    if flags[i] == 'y':
        for j in range(0, n):
            if flags[j] == 'g':
                if dist(x[i], y[i], x[j], y[j]) <= eps and clust[j] != -1:
                    clust[i] = clust[j]

# В результатае получилось распредение по кластерам. Если номер кластера >= 0,
# значит точка находится в этом кластере, если -1, то это выброс.
print(clust)
print(len(set(clust)))

