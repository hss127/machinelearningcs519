from keras.layers import  Dense,Dropout
from keras.models import Sequential
from keras.optimizers import RMSprop
from parserf import range1,range2
model=Sequential()
model.add(Dense(450, input_dim=range2-range1, activation='relu'))
#model.add(Dropout(0.30))
model.add(Dense(350, activation='relu'))
model.add(Dense(256, activation='softmax'))
optimizer = RMSprop(lr=0.0010)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
