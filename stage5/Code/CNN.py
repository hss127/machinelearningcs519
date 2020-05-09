from keras.layers import  Dense, Conv1D, MaxPooling1D,Flatten, Dropout
from keras.models import Sequential
from keras.optimizers import Adam
from parserf import range2,range1


model=Sequential()
model.add(Conv1D(filters=32, kernel_size=7,strides=3 ,padding='valid', activation='relu', input_shape=(range2-range1,1)))
#model.add(Dropout(0.04))
model.add(MaxPooling1D(pool_size=3))
model.add(Conv1D(filters=32, kernel_size=4,strides=3 ,padding='valid', activation='relu'))
model.add(Flatten())
model.add(Dense(256, activation='softmax'))
#model.compile(loss='categorical_crossentropy',optimizer='adam', metrics=['accuracy'])
optimizer = Adam(lr=0.003)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

