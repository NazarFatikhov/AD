import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Train data generator
def generateData(numberOfClassEl, numberOfClasses):
    data = []
    for classNum in range(numberOfClasses):
        # Choose random center of 2-dimensional gaussian
        centerX, centerY = random.random() * 5.0, random.random() * 5.0
        # Choose numberOfClassEl random nodes with RMS=0.5
        for rowNum in range(numberOfClassEl):
            data.append([[random.gauss(centerX, 0.5), random.gauss(centerY, 0.5)], classNum])
    return data

def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def cmp(val1, val2):
    return dist(val1[0][0], val1[0][1], x_new, y_new) - \
            dist(val2[0][0], val2[0][1], x_new, y_new)

def cmp_to_key(cmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return cmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return cmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return cmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return cmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return cmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return cmp(self.obj, other.obj) != 0
    return K



n = 20
k = np.int(np.sqrt(n))
data = []
data = generateData(n, k)
x, y = [], []
for i in range(n):
    x.append(data[i][0][0])
    y.append(data[i][0][1])
plt.scatter(x, y)
# print(data)
min_x, max_x = np.min(x), np.max(x)
min_y, max_y = np.min(y), np.max(y)
x_new = min_x + np.random.random() * (max_x - min_x)
y_new = min_y + np.random.random() * (max_y - min_y)
plt.scatter(x_new, y_new, color='r')
plt.show()

# Сортируем data по приближенности к новой точке
sorted_data = sorted(data, key=cmp_to_key(cmp))

# Для проверки сортировки сопоставляем дистанции отсортированному датафрэйму.
dists = []
for i in range(len(sorted_data)):
    dists.append(dist(sorted_data[i][0][0], sorted_data[i][0][1], x_new, y_new))

# Инициализируем и заполняем словарь кол-ва точек входящих в каждый кластер
# в первых k точек отсортированного списка
counts = {"clust_0": 0,
          "clust_1": 0,
          "clust_2": 0,
          "clust_3": 0}

for i in range(k):
    counts["clust_{}".format(sorted_data[i][1])] += 1

# Выведем список кол-ва соседей в каждом кластере в отсортированном виде
print({k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)})