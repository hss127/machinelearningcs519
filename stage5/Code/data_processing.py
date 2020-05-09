import numpy as np
from parserf import range1,range2,label_byte
from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
textin_array=np.load('plaintext.npy')
keys=np.load('key.npy')
trace=np.load('trace.npy') #1400-2500
labels=np.load('labels.npy')



X=trace[:,range1:range2]
y=labels[:,label_byte]

X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.3, random_state=1, stratify=y)

plaintext_train, plaintext_test, y_train1, y_test1 = train_test_split(
      textin_array, y, test_size=0.3, random_state=1, stratify=y)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)




