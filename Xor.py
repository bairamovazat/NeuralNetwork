import numpy, mnist #не работает ((
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils

from NeuralNetwork import Map

numpy.random.seed(42)

data = Map.get_data();
X_train = [[0, 0], [0, 1], [1, 0], [1, 1]] #нейронная сеть принимает 2 мерный массив где элемент - 1 тест
y_train = [[0,0], [1,1], [1,1], [0,0]] #2 мерный массив правильных ответов

model = Sequential()
model.add(Dense(300, input_dim=2, activation="relu", kernel_initializer="normal"))
model.add(Dense(2, activation="softmax", kernel_initializer="normal"))
model.compile(loss="categorical_crossentropy",optimizer="SGD", metrics=["accuracy"])
model.fit(X_train, y_train, batch_size=4, epochs=100)
result = model.predict_proba(X_train,batch_size=4)
print(X_train)
print(y_train)
print(result)
#сеть обучилась, осталось протестить.