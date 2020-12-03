import numpy as np
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression

# Часть 1: Задание тренировочной выборки
# Кол-во точек
n = 100

# Координаты тренировочных точек
x = np.random.randint(0, 100, n)
y = np.random.randint(0, 100, n)
z = np.random.randint(0, 100, n)
# Класетры, которым каждая точка пренадлежит (1 или -1).
clusters = [0] * 100

# Задаем плоскость для разбиения по кластерам.
# В первую очередь задачем коэфиценты для уравления плоскости Ax + By + Cz + d = 0
a = 0.3 + np.random.random() * 0.2
b = 0.3 + np.random.random() * 0.2

# Описываем плоскость в виде матрицы x, y для изображения по оси z.
plane_z = np.ones((100, 100))
for i in range(0, 100):
    for j in range(0, 100):
        plane_z[i][j] = a * i + b * j

# Делаем для каждого кластера массив с координатами
x_clust_1 = []
y_clust_1 = []
z_clust_1 = []
x_clust_2 = []
y_clust_2 = []
z_clust_2 = []

# Заполняем массивы соответсвующими значениями.
# Если точка лежит ниже заданной плоскости, то кладем ее в вервый кластер (-1), иначе во второй кластер (1).
for i in range(100):
    if z[i] < (a * x[i] + b * y[i]):
        clusters[i] = -1
        x_clust_1.append(x[i])
        y_clust_1.append(y[i])
        z_clust_1.append(z[i])
    else:
        clusters[i] = 1
        x_clust_2.append(x[i])
        y_clust_2.append(y[i])
        z_clust_2.append(z[i])

# Часть 2: Поиск разделяющий плоскости методом логистической регрессии.
# Обучаем модель методом логистической регресии
points = []
for i in range(n):
    points.append((x[i], y[i], z[i]))
lr = LogisticRegression()
model = lr.fit(points, clusters)

# Строим разделяющую плоскость на основе модели
new_plane_z = np.ones((100, 100))
for i in range(0, 100):
    for j in range(0, 100):
        new_plane_z[i][j] = (-model.coef_[0][0] * i - model.coef_[0][1] * j - model.intercept_) / model.coef_[0][2]

fig = go.Figure(data=[
    go.Scatter3d(x=x_clust_1, y=y_clust_1, z=z_clust_1, mode="markers", name="-1"),
    go.Scatter3d(x=x_clust_2, y=y_clust_2, z=z_clust_2, mode="markers", name="1"),
    go.Surface(z=new_plane_z),
    go.Surface(z=plane_z)
])
fig.show()

print(new_plane_z)
print(x_clust_1)
print(y_clust_1)
print(z_clust_1)
print(a, b)
