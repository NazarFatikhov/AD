import matplotlib.pyplot as plt
import random
from means import *

n = 100
x = [random.randint(1, 100) for i in range(n)]
y = [random.randint(1, 100) for i in range(n)]

c = [0] * 9

for k in range(2, 9):
    x, y, cluster, R, count, x_cc, y_cc = k_means(x, y, k)
    c[k] = sqr_sum(x, y, cluster, x_cc, y_cc)

d = [0] * 9

for k in range(2, len(d) - 1):
    d[k] = np.abs(c[k] - c[k + 1])/np.abs(c[k] - c[k - 1])

min_d = d[2]
min_d_ind = 2
for i in range(2, len(d) - 1):
    if d[i] < min_d:
        min_d = d[i]
        min_d_ind = i

opt_k = min_d_ind

print(opt_k)

x, y, cluster, R, count, x_cc, y_cc = k_means(x, y, opt_k)

for i in range(opt_k):
    plt.scatter(x_cc[i], y_cc[i], color="black")

for i in range(0, n):
    cl = cluster[i] + 1
    plt.scatter(x[i], y[i], color=((1/cl), 0.2, 0.4))

print(cluster)

plt.show()



