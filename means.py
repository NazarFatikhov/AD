import numpy as np

# Для красивого вывода матрицы
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()

def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def clust(x, y, x_cc, y_cc, k):
    cluster = []
    for i in range(0, n):
        d = dist(x[i], y[i], x_cc[0], y_cc[0])
        numb = 0
        for j in range(0, k):
            if dist(x[i], y[i], x_cc[j], y_cc[j]) < d:
                d = dist(x[i], y[i], x_cc[j], y_cc[j])
                numb = j
        cluster.append(numb)
    return cluster

def k_means(x, y, k, max_count=10):
    x_c = np.mean(x)
    y_c = np.mean(y)

    R = 0
    for i in range(0, n):
        r = dist(x_c, y_c, x[i], y[i])
        if r > R:
            R = r

    x_cc = [R * np.cos(2 * np.pi * i / k) + x_c for i in range(k)]
    y_cc = [R * np.sin(2 * np.pi * i / k) + y_c for i in range(k)]

    cluster = clust(x, y, x_cc, y_cc, k)

    prev_R = R
    new_R = 0
    count = 1
    while ((prev_R != new_R) or (new_R == 0)) and (count != max_count):
        x_sums = [0] * k
        x_counts = [0] * k
        y_sums = [0] * k
        y_counts = [0] * k
        for i in range(n):
            ind = cluster[i]
            x_sums[ind] += x[i]
            x_counts[ind] += 1
            y_sums[ind] += y[i]
            y_counts[ind] += 1

        x_means = [x_sums[i] / x_counts[i] for i in range(k)]
        y_means = [y_sums[i] / y_counts[i] for i in range(k)]

        R = 0
        for i in range(0, n):
            ind = cluster[i]
            r = dist(x_means[ind], y_means[ind], x[i], y[i])
            if r > R:
                R = r

        x_cc = [R * np.cos(2 * np.pi * i / k) + x_means[i] for i in range(k)]
        y_cc = [R * np.sin(2 * np.pi * i / k) + y_means[i] for i in range(k)]

        cluster = clust(x, y, x_cc, y_cc, k)
        prev_R = new_R
        new_R = R
        count += 1

    return x, y, cluster, R, count, x_cc, y_cc

def sqr_sum(x, y, cluster, x_cc, y_cc):
    s = 0

    for i in range(len(x)):
        clust_num = cluster[i]
        d = dist(x[i], y[i], x_cc[clust_num], y_cc[clust_num])
        s += d ** 2

    return s