import numpy, mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from NeuralNetwork import Map
from datetime import datetime
numpy.random.seed(42)
startTime = datetime.now(tz=None)
data = Map.get_data(2);
X_train = data[0]
y_train = data[1]
nb_epoch = data[2]
#= data["X_data"] #нейронная сеть принимает 2 мерный массив где элемент - 1 тест
#= data["y_data"] #2 мерный массив правильных ответов

model = Sequential()
model.add(Dense(800, input_dim=6, activation="tanh", kernel_initializer="normal"))
model.add(Dense(400, activation="tanh", kernel_initializer="normal"))
model.add(Dense(200, activation="tanh", kernel_initializer="normal"))
model.add(Dense(4, activation="sigmoid", kernel_initializer="normal"))
model.compile(loss="categorical_crossentropy",optimizer="SGD", metrics=["accuracy"])
model.fit(X_train, y_train, batch_size=20, nb_epoch=nb_epoch, verbose=1)
endTime = datetime.now(tz=None)
result = model.predict_proba(X_train,batch_size=5)
print(X_train)
print(y_train)
print(result)
static = 0;
for i in range(0, len(y_train)):
    maxInt = result[i][0];
    maxIndex = 0;
    for j in range(1, len(result[i])):
        if result[i][j] > maxInt :
            maxInt = result[i][j]
            maxIndex = j;
    if y_train[i][maxIndex] == 1:
        static+=1
    print(str(y_train[i]) + str(y_train[i][maxIndex] == 1) + " Index: " + str(maxIndex + 1))
print(str(static/len(X_train)))
print("Время работы:" + str(endTime-startTime))
# сеть обучилась, осталось протестить.
