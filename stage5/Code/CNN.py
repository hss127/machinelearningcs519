from keras.layers import  Dense, Conv1D, MaxPooling1D,Flatten,Dropout
from keras.models import Sequential
from parserf import range2,range1
model=Sequential()
model.add(Conv1D(filters=256, kernel_size=30,strides=1 ,padding='valid', activation='relu', input_shape=(range2-range1,1)))
model.add(MaxPooling1D(pool_size=3))
model.add(Conv1D(filters=110, kernel_size=15,strides=1 ,padding='valid', activation='relu'))
model.add(Flatten())
model.add(Dense(256, activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer='adam', metrics=['accuracy'])
