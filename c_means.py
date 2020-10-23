from means import *
import random
from math import isnan

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()

def check_f(f_prev, f_cur, e):
    if ((len(f_prev) != len(f_cur)) | (len(f_prev[0]) != len(f_cur[0]))):
        raise Exception("Different lengths")
    for i in range(len(f_prev)):
        for j in range(len(f_prev[i])):
            if (abs(f_prev[i][j] - f_cur[i][j]) >= e):
                return False
    return True


n = 10
K = 3
E = 0.01

x = [random.randint(1, 100) for i in range(n)]
y = [random.randint(1, 100) for i in range(n)]

x_c = np.mean(x)
y_c = np.mean(y)

R = 0
for i in range(0, n):
    r = dist(x_c, y_c, x[i], y[i])
    if r > R:
        R = r

# len = k
v_x = [R * np.cos(2 * np.pi * i / K) + x_c for i in range(K)]
v_y = [R * np.sin(2 * np.pi * i / K) + y_c for i in range(K)]

d = []
for k in range(K):
    clust = []
    for i in range(n):
        clust.append(dist(x[i], y[i], v_x[k], v_y[k]))
    d.append(clust)

f = []
for k in range(n):
    clust = []
    for i in range(K):
        sum = 0
        for j in range(K):
            sum += (d[i][k]/d[j][k]) ** (2/(n - 1))
        clust.append(1/sum)
    f.append(clust)

f_prev = [[0 for i in range(K)] for j in range(n)]
f_cur = f

count = 1

while(not check_f(f_prev, f_cur, E)):
    v_x = []
    v_y = []
    for i in range(K):
        sum = 0
        for j in range(n):
            sum += f_cur[j][i] ** n
        v_x.append((sum * x[i]) / sum)
        v_y.append((sum * y[i]) / sum)

    d = []
    for k in range(K):
        clust = []
        for i in range(n):
            clust.append(dist(x[i], y[i], v_x[k], v_y[k]))
        d.append(clust)

    f = []
    for k in range(n):
        clust = []
        for i in range(K):
            sum = 0
            for j in range(K):
                sum += (d[i][k] / d[j][k]) ** (2 / (n - 1))
                if (isnan(sum)):
                    sum = E
            clust.append(1 / sum)
        f.append(clust)

    f_prev = f_cur
    f_cur = f
    count += 1

print_matrix(f_cur)
print(count)