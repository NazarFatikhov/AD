import numpy as np
from keras.datasets import mnist
from keras.models import load_model

# Проверка обучившейся сети для тестовых данных из MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

model = load_model('mnist.h5')
x = np.expand_dims(x_test[0], axis=-0)
res = model.predict(x)
print(res)
