import numpy as np
import pandas as pd

disease = pd.read_csv('disease.csv', delimiter=";")
sympotom = pd.read_csv('symptom.csv', delimiter=";")

rand_symp = [np.random.randint(0, 2) for i in range(23)]

p_disease = []
for i in range(len(disease) - 1):
    p_disease.append((disease['количество пациентов'][i]) / (disease['количество пациентов'][len(disease) - 1]))

p_dis_sympt = [1] * (len(disease) - 1)

# Высчитваем произведение средних вероятностей появление каждого симптома, который указан в тестовой выборке
p = 1
for i in range(1, 23 + 1):
    if rand_symp[i - 1] == 1:
        p *= sum(sympotom.iloc[i][1:]) / 9

# Для каждой болезни D[I] высчитываем вероятнсоти
# P(C1|D1) * P(C2|D1) * ... * P(C23|D1) * P(D1)
# ---------------------------------------------
#          P(C1) * P(C2) * ... P(C23)
for i in range(len(disease) - 1):
    p_dis_sympt[i] *= p_disease[i]
    for j in range(len(sympotom) - 1):
        if rand_symp[j] == 1:
            p_dis_sympt[i] *= float(sympotom.iloc[j + 1][i + 1])
    p_dis_sympt[i] /= p

# Делаем словарь: {болезнь: вероятность}
disease_p = {}
for i in range(len(disease) - 1):
    disease_p[disease.iloc[i][0]] = p_dis_sympt[i]

# Выводим болезни в порядке возрастания вероятностей
print(sorted(disease_p, key=disease_p.get))
