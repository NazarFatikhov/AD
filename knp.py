import sys
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from means import *


def first_connection():
    minim = weight[0][1]
    i_min, j_min = 0, 1
    for i in range(n):
        for j in range(i + 1, n):
            if minim > weight[i][j]:
                minim = weight[i][j]
                i_min, j_min = i, j
    tree[i_min][j_min] = minim
    tree[j_min][i_min] = minim
    weight[i_min][j_min] = weight[j_min][i_min] = sys.maxsize
    connect_pnt[i_min] = connect_pnt[j_min] = 1


def lync_all():
    minim = sys.maxsize
    i_min, j_min = None, None
    for i in range(n):
        if connect_pnt[i] == 1:
            for j in range(n):
                if connect_pnt[j] == 0:
                    if (minim > weight[i][j]):
                        minim = weight[i][j]
                        i_min, j_min = i, j
    tree[i_min][j_min] = minim
    tree[j_min][i_min] = minim
    weight[i_min][j_min] = weight[j_min][i_min] = sys.maxsize
    connect_pnt[i_min] = connect_pnt[j_min] = 1


def delete_connection():
    maxim = 0
    i_max = j_max = 0
    for i in range(n):
        for j in range(i + 1, n):
            if tree[i][j] > maxim:
                maxim = tree[i][j]
                i_max, j_max = i, j
    tree[i_max][j_max] = tree[j_max][i_max] = 0


def cluster(cl):
    change = False
    for i in range(n):
        for j in range(n):
            if tree[i][j] != 0:
                clust_pnt[i] = clust_pnt[j] = cl
                tree[i][j] = tree[j][i] = 0
                change = True
    return change


n, k = 15, 3
# weight = np.random.randint(1,100, (n,n))
weight = [[0 for i in range(n)] for i in range(n)]
for i in range(0, n):
    for j in range(i + 1, n):
        weight[i][j] = np.random.randint(1, 100)
        weight[j][i] = weight[i][j]
tree = [[0 for i in range(n)] for i in range(n)]
connect_pnt = [0 for i in range(n)]
# Находим пару точек с минимальным p[i][j] и соединяем их ребром
first_connection()
# Пока есть изолированные точки, соединяем с изолированную точку с ближаейшей неизолированной
while 0 in connect_pnt:
    lync_all()

# Отрисовываем граф с зелеными ребарми
G = nx.Graph()
for i in range(len(tree)):
    for j in range(i + 1, len(tree[i])):
        if tree[i][j] != 0:
            G.add_edge(i, j, weight=tree[i][j], color='green')

# Рисуем граф для демонстрации
colors = nx.get_edge_attributes(G,'color').values()
nx.draw(G, edge_color=colors, with_labels=True)
plt.show()

# Копируем дерево, чтобы потом сравнить с получившимся деревом (для проверки)
old_tree = tree.copy()

# Помечаем k - 1 самых длиных ребра красным цветом, чтобы визиулизировать кластеризацию
for _ in range(k - 1):
    maxim = 0
    i_max = j_max = 0
    for i in range(n):
        for j in range(i + 1, n):
            if tree[i][j] > maxim:
                maxim = tree[i][j]
                i_max, j_max = i, j
    print(maxim)
    tree[i_max][j_max] = tree[i_max][j_max] = 0
    weight = G.get_edge_data(i_max, j_max)['weight']
    G.remove_edge(i_max, j_max)
    G.add_edge(i_max, j_max, weight=weight, color='red')

# Прорисовываем кластеризованный граф
colors = nx.get_edge_attributes(G,'color').values()
nx.draw(G, edge_color=colors, with_labels=True)
plt.show()