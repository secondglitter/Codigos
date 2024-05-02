import nltk 
from nltk.stem import WordNetLemmatizer
import json
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.optimizers.schedules import ExponentialDecay
import random

nltk.download('punkt')
nltk.download('wordnet')

with open('chats/opciones.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    intentos = data['intentos']

lemmatizer = WordNetLemmatizer()

words = []
classes = []
documents = []
ignore_words = ['?', '!']

# Recorre cada intento en la lista de intentos
for intento in intentos:
    tema = intento['tema']
    opciones = intento['opciones']
    respuestas = intento['respuestas']
    # Agrega el tema a la lista de clases si no está presente
    if tema and tema not in classes:
        classes.append(tema)
    for opcion in opciones:
        # Tokeniza las palabras en cada opción y las agrega a la lista de palabras
        w = nltk.word_tokenize(opcion)
        words.extend(w)
        # Agrega el par (opción, tema) a la lista de documentos
        documents.append((w, tema))

# Lematiza las palabras y las convierte en minúsculas, excluyendo las palabras ignoradas
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

# Guarda las listas de palabras y clases en archivos pickle
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

training = []
output_empty = [0] * len(classes)

# Crear el conjunto de entrenamiento
for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    for word in words:
        # Crear una bolsa de palabras binaria para cada opción
        bag.append(1) if word in pattern_words else bag.append(0)
    output_row = list(output_empty)
    # Crear un vector de salida con un 1 en la posición correspondiente al tema de la intención
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

# Mezclar aleatoriamente el conjunto de entrenamiento
random.shuffle(training)

# Divide el conjunto de entrenamiento en características (train_x) y etiquetas (train_y)
train_x = np.array([row[0] for row in training])
train_y = np.array([row[1] for row in training])

# Crea el modelo de red neuronal
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Configura el optimizador con una tasa de aprendizaje exponencialmente decreciente
lr_schedule = ExponentialDecay(
    initial_learning_rate=0.01,
    decay_steps=10000,
    decay_rate=0.9
)

sgd = SGD(learning_rate=lr_schedule, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Entrena el modelo con el conjunto de entrenamiento
hist = model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1)

# Guarda el modelo entrenado en un archivo h5
model.save('chatbot_model.h5')

print('Modelo creado y guardado como chatbot_model.h5')
